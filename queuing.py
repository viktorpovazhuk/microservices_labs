import hazelcast
import time
from threading import Thread

def write_queue(client, thread_num):
    print(f'Starting {thread_num}')
    queue = client.get_queue("qqq").blocking()
    for i in range(30):
        queue.put(i)
        print(f'Producing {i}')
        time.sleep(10 * 1e-3)

def read_queue(client, thread_num):
    print(f'Starting {thread_num}')
    queue = client.get_queue("qqq").blocking()
    for i in range(10):
        item = queue.take()
        print(f'Taking {thread_num} {item}')
        # time.sleep(10 * 1e-3)

# client = hazelcast.HazelcastClient()
# thread = Thread(target=write_queue, args=(client, 0))
# thread.start()

for i in range(3):
    client = hazelcast.HazelcastClient()
    thread = Thread(target=read_queue, args=(client, i + 1))
    thread.start()