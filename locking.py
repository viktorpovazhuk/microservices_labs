import hazelcast
import time
from threading import Thread

def non_locking(client, thread_num):
    key = 1
    map = client.get_map("lock_map").blocking()
    map.put(key, 0)
    print(f'Starting {thread_num}')
    for k in range(int(1e3)):
        if k % 100 == 0:
            print(f'At {k}')
        value = map.get(key)
        time.sleep(10 * 1e-3)
        value = int(value) + 1
        map.put(key, value)
    print(f'Finished! Result = {map.get(key)}')

def pessimistic_locking(client, thread_num):
    key = 1
    map = client.get_map("lock_map").blocking()
    map.put(key, 0)
    print(f'Starting {thread_num}')
    for k in range(int(1e3)):
        map.lock(key)
        if k % 50 == 0:
            print(f'At {k}')
        try:
            value = map.get(key)
            time.sleep(10 * 1e-3)
            value = int(value) + 1
            map.put(key, value)
        finally:
            map.unlock(key)
    print(f'Finished! Result = {map.get(key)}')

def optimistic_locking(client, thread_num):
    key = 1
    map = client.get_map("lock_map").blocking()
    map.put(key, 0)
    print(f'Starting {thread_num}')
    for k in range(int(1e3)):
        if k % 50 == 0:
            print(f'At {k}')
        while True:
            value = map.get(key)
            value_new = value + 1
            time.sleep(10 * 1e-3)
            if map.replace_if_same(key, value, value_new):
                break
    print(f'Finished! Result = {map.get(key)}')

for i in range(3):
    client = hazelcast.HazelcastClient()
    thread = Thread(target=optimistic_locking, args=(client, i))
    thread.start()