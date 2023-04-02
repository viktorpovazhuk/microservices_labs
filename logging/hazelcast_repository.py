import hazelcast

def add(msg):
    my_map = client.get_map("my_map").blocking()
    my_map.put(msg.uuid, msg.text)

def get_all():
    my_map = client.get_map("my_map").blocking()
    messages = my_map.values()
    return str(list(messages))

client = hazelcast.HazelcastClient()