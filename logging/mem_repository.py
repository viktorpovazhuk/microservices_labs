MESSAGES_MAP = {}

def add(msg):
    MESSAGES_MAP[msg.uuid] = msg.text

def get_all():
    return str(list(MESSAGES_MAP.values()))