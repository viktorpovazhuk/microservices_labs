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

Run Management Center from Hazelcast directory to view changes on nodes.

```
$ cd hazelcast
$ management-center/bin/hz-mc start
```

Start Kafka and prepare "messages" topic.

```
$ cd kafka
$ bin/zookeeper-server-start.sh config/zookeeper.properties
$ bin/kafka-server-start.sh config/server.properties
$ bin/kafka-topics.sh --create --topic messages --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1
```

To view topic content install Offset Explorer and connect to cluster.

Then run 3 instancees of logging service, 2 instances of messages service and facade service from corresponding project directories.

```
$ cd microservices_labs
$ cd facade
$ uvicorn controller:app --reload --port 8000

$ cd ../messages
# repeat 2 times, for ports: 8004, 8005
$ uvicorn controller:app --reload --port 8004

$ cd ../logging
# repeat 3 times, for ports: 8001, 8002, 8003
$ uvicorn controller:app --reload --port 8001
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

 

