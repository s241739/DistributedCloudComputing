## Distributed Cloud Computing / Distributed Systems
## Lab 04.01 Experimenting with a Publish Subscribe Architecture in Python 3
##            Using Python's built-in queue module
## Last updated: Jan 2025, Dr Kakia Chatsiou

# The example below shows an example of the **Observer Pattern**, where the PUBLISHER notifies 
# all its SUBSCRIBERS whenever a new message is published.
#  
# Here is what happens in the code in more detail:
 
# 1. Publisher Class:
# -- Manages a list of subscribers and a message queue.
# -- Has methods to subscribe new subscribers and publish messages to all subscribed entities.
#
# 2. Subscriber Class:
# -- Represents an individual subscriber that can receive messages.
# -- Contains a method to handle the received messages and print them.
#
# 3. Main Code:
# -- Creates instances of the Publisher and Subscriber classes, 
# -- subscribes the subscribers to the publisher, and 
# -- publishes a message, demonstrating the publish-subscribe pattern.

### 

import queue  # Importing the queue module to use Queue class for message handling

class Publisher:
    def __init__(self):
        # Initializes a new Publisher object
        self.message_queue = queue.Queue()  # Creates a message queue to store messages
        self.subscribers = []  # Initializes an empty list to hold subscribers

    def subscribe(self, subscriber):
        # Method to add a subscriber to the list
        self.subscribers.append(subscriber)  # Appends the subscriber to the subscribers list

    def publish(self, message):
        # Method to publish a message to all subscribers
        self.message_queue.put(message)  # Puts the message in the message queue
        for subscriber in self.subscribers:  # Iterates through each subscriber
            subscriber.receive(message)  # Calls the receive method of each subscriber with the message


class Subscriber:
    def __init__(self, name):
        # Initializes a new Subscriber object with a name
        self.name = name  # Sets the name of the subscriber

    def receive(self, message):
        # Method to receive messages from the publisher
        print(f"{self.name} received message: {message}")  # Prints the message received by the subscriber


# Creating an instance of Publisher
publisher = Publisher()

# Creating instances of Subscribers with unique names
subscriber_1 = Subscriber("Subscriber 1")
subscriber_2 = Subscriber("Subscriber 2")

# Subscribing the two subscribers to the publisher
publisher.subscribe(subscriber_1)  # Adding subscriber_1 to the publisher's subscribers list
publisher.subscribe(subscriber_2)  # Adding subscriber_2 to the publisher's subscribers list

# Publishing a message to all subscribers
publisher.publish("Hello World")  # This will send "Hello World" to both subscribers

## TASKS:

# 1. Study the code and understand the logic, as well as the steps that are followed for the PUB/SUB
#    system to work.
# 2. Modify the message to be "I like distributed systems" or something else of your choice
# 3. Define an additional subscriber to the publishers' subscriber's list with variable name 
#    subscriber_3 and name "suffolk".