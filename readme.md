# Microservices with Hazelcast

## Prerequisites

Create and activate virtual environment.

```
$ cd microservices_labs
$ python3 -m venv venv
$ . venv/bin/activate
```

Install necessary packages.

```
$ pip install -r requirements.txt
```

## Preparation

Start 3 instances of Hazelcast nodes from its directory.

```
$ cd hazelcast
# repeat 3 times
$ bin/start.sh
```

Then run 3 instancees of logging service and all other services from corresponding project directories.

```
$ cd microservices_labs
$ cd facade
$ uvicorn controller:app --reload --port 8000

$ cd ../messages
$ uvicorn controller:app --reload --port 8001

$ cd ../logging
# repeat 3 times for ports: 8002, 8003, 8004
$ uvicorn controller:app --reload --port 8002
```

Run Management Center from Hazelcast directory to view changes on nodes.

```
$ cd hazelcast
$ management-center/bin/hz-mc start
```

## Usage

There are 2 types of requests to facade server.

You can send requests from VS Code with extension *REST Client*.

### Add message

The request add message to distributed map.

```
POST http://localhost:8000/ HTTP/1.1
content-type: application/json

{
    "text": "hi"
}
```

### Get messages

The request retrieves all messages from both services: logging and messages.

```
GET http://localhost:8000/ HTTP/1.1
```

 

