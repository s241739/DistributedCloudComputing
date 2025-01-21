## Distributed Cloud Computing / Distributed Systems
## Lab 04.01.02 Experimenting with a Publish Subscribe Architectures in Python 3
##              _Using Python's threading module_
## Last updated: Jan 2025, Dr Kakia Chatsiou

#
# The example below demonstrates a basic implementation of the Publisher-Subscriber 
# pattern using **threading**, allowing for asynchronous message delivery to multiple 
# subscribers based on topics.
#
# Here is what happens in the code in more detail:
#
# 1. **Threading**: The code uses the threading module to manage concurrent execution. 
# Each subscriber has an Event object that allows them to wait for a message from the 
# publisher.
# 
# 2. Publisher Class:
# 
# -- Initialization: The Publisher class initializes an empty dictionary called 
#    subscribers, where each key is a topic and the value is a list of subscribers 
#    interested in that topic.
# -- Subscribe Method: This method allows a subscriber to subscribe to a specific 
#    topic. It checks if the topic exists in the dictionary; if not, it creates a 
#    new list for that topic and appends the subscriber.
# -- Publish Method: This method sends a message to all subscribers of a specified 
#    topic. It sets the event for each subscriber, indicating that a message is 
#    available, and assigns the message to the subscriber's message attribute.
#
# 3. Subscriber Class:
# 
# -- Initialization: The Subscriber class initializes with a name, an Event object 
#    for synchronization, and a message attribute set to None.
# -- Receive Method: This method waits for the event to be set (indicating a message 
#    is available). Once the event is set, it prints the received message, then clears 
#    the event to prepare for the next message.
# 
# 4. Creating Instances: The code creates a Publisher instance and several Subscriber 
#    instances. It subscribes each subscriber to specific topics.
# 
# 5. Publishing and Receiving Messages: Finally, the publish method is called to send 
#    a message to the "sports" topic, and subscriber_1 calls its receive method to 
#    print the received message.

## TASKS:

# 1. Study the code and understand the logic, as well as the steps that are followed for the PUB/SUB
#    system to work. Compare it with PUB/SUB system 1 in lab-04-01-01.py
# 2. Define a couple of additional subscribers to the publishers' subscriber's list (such as yourself 
#    the people sitting around you)
# 3. Subscribe each subscribers to different topics.
# 4.  Define and publish a couple of more additional messages for your new topics

import threading  # Import the threading module to work with threads and events.

# Define the Publisher class
class Publisher:
    def __init__(self):
        # Initialize a dictionary to hold subscribers for different topics
        self.subscribers = {}

    # Method to subscribe a subscriber to a specific topic
    def subscribe(self, subscriber, topic):
        # If the topic does not exist in the subscribers dictionary, create a new list for it
        if topic not in self.subscribers:
            self.subscribers[topic] = []
        # Append the subscriber to the list of subscribers for that topic
        self.subscribers[topic].append(subscriber)

    # Method to publish a message to a specific topic
    def publish(self, message, topic):
        # Check if the topic has any subscribers
        if topic in self.subscribers:
            # Iterate over each subscriber for the given topic
            for subscriber in self.subscribers[topic]:
                # Set the event for the subscriber, indicating that a message is available
                subscriber.event.set()
                # Assign the message to the subscriber's message attribute
                subscriber.message = message

# Define the Subscriber class
class Subscriber:
    def __init__(self, name):
        # Initialize the subscriber with a name
        self.name = name
        # Create an Event object for synchronization
        self.event = threading.Event()
        # Initialize message attribute to None
        self.message = None

    # Method to receive messages from the publisher
    def receive(self):
        # Wait until the event is set by the publisher
        self.event.wait()
        # Print the received message
        print(f"{self.name} received message: {self.message}")
        # Clear the event after receiving the message
        self.event.clear()

# Create an instance of Publisher
publisher = Publisher()

# Create instances of Subscriber
subscriber_1 = Subscriber("Subscriber 1")
subscriber_2 = Subscriber("Subscriber 2")
subscriber_3 = Subscriber("Subscriber 3")
subscriber_4 = Subscriber("Connor")
subscriber_5 = Subscriber("Oliver")
subscriber_6 = Subscriber("Josh")
subscriber_7 = Subscriber("Joe")

# Subscribe subscribers to different topics
publisher.subscribe(subscriber_1, "sports")          # Subscriber 1 subscribes to "sports"
publisher.subscribe(subscriber_2, "entertainment")   # Subscriber 2 subscribes to "entertainment"
publisher.subscribe(subscriber_3, "sports")          # Subscriber 3 subscribes to "sports"
publisher.subscribe(subscriber_4, "library")
publisher.subscribe(subscriber_5, "podcast")
publisher.subscribe(subscriber_6, "music")
publisher.subscribe(subscriber_7, "entertainment")

# Publish a message to the "sports" topic
publisher.publish("Soccer match result", "sports")
publisher.publish("I'm back", "music")
publisher.publish("May you find your book in this place", "library")
publisher.publish("Talk to you", "podcast")
publisher.publish("Drama Alert", "entertainment")
# Call the receive method of subscriber_1 to process the message
subscriber_1.receive()
subscriber_2.receive()
subscriber_3.receive()
subscriber_4.receive()
subscriber_5.receive()
subscriber_6.receive()
subscriber_7.receive()
