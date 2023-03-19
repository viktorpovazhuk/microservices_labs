import hazelcast

def show_distributed_map(client):
    my_map = client.get_map("my_map").blocking()
    for i in range(int(1e3)):
        my_map.put(i, i)

def show_get_element(client):
    my_map = client.get_map("my_map").blocking()
    value = my_map.get(1)
    print(value)

client = hazelcast.HazelcastClient()
show_get_element(client)