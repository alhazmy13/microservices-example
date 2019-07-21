# Microservices Example

*NOTE* This is just an example and is not ready yet

I'll use below technology, if you are interested on this example, please star and watch this repo, and come back later 😁



## System Architecture

![Untitled Diagram-2](https://user-images.githubusercontent.com/4659608/56154598-94209180-5fc1-11e9-99d6-776a47b238d4.png)


system is based upon in-process micro-services architecture to establish a simple way for system deployment.

Each Node or service is a standalone application that bundle one single service (Micro-service) which perform a small and specific job in the system, each service has no direct communication to another one, so services is loosely coupled from each other and communication is based on asynchronous event messages through using event bus (such as rabbitmq).

All the Micro-services considered as a private service inside the system except the API service which act as public service to the external world throw the Load Balancer, so the client applications or any external third parties can integrate or talk to the system through api service.

System has several micro-services, mainly each service can publish and/or subscribe to a specific events.

The following is a list for the services:

* API service:  has a public interface end-points (http restful and bi-directional websocket) for the system.
* User service: manage the user account operations.
* Email service: responsible for sending emails into a mail server. *(WORKING ON IT)*

# System Technology

The main technology for building this backend system.
* python:  a server development language for system micro-services.
* rabbitmq: is a message broker used as a message bus for events.
* docker: to build each service.

***NOTE:*** you can use any language or framework for each service, for example, you can create a post service with go and notification service with ruby.   

# System Database

Since each service are isolated, then you can use any database for each service based on the functionally of the service, however in this example we are used sqlite in user service.  


# Environment:
* Rabbitmq : follow instructions in the [link](https://www.rabbitmq.com/install-homebrew.html).
* Python 3.6 [link](https://stackoverflow.com/questions/51125013/how-can-i-install-a-previous-version-of-python-3-in-macos-using-homebrew)


# Run Example:

First you need to run `Rabbitmq` with command:

```
 brew services start rabbitmq
```

to stop `Rabbitmq`:

```
 brew services stop rabbitmq
```

then run from `api` folder command:

```
python3.6 app.py
```

then run from `user` folder command:

```
python3.6 app.py
```





