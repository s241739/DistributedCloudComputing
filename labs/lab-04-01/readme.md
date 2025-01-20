
## 🟡🧪 Lab 04.01: Experimenting with Publish Subscribe Architectures in Python
Distributed Cloud Computing / Distributed Systems ⏺️ Last updated: Jan 2025, Dr Kakia Chatsiou

### PUB/SUB System 1: Using Python's built-in `queue` module

The example below shows an example of the **Observer Pattern**, where the `PUBLISHER` notifies 
 all its `SUBSCRIBERS` whenever a new message is published.
  
 Here is what happens in the code in more detail:

 1. `publisher` Class:
 -- Manages a list of subscribers and a message queue.
 -- Has methods to subscribe new subscribers and publish messages to all subscribed entities.

 2. `subscriber` Class:
 -- Represents an individual subscriber that can receive messages.
 -- Contains a method to handle the received messages and print them.

 3. Main Code:
 -- Creates instances of the Publisher and Subscriber classes, 
 -- subscribes the subscribers to the publisher, and 
 -- publishes a message, demonstrating the publish-subscribe pattern.


#### Lab Tasks:

**Task 1.** Study the code and understand the logic, as well as the steps that are followed for the PUB/SUB system to work.
**Task 2.** Modify the message to be `"I like distributed systems"` or something else of your choice
**Task 3.** Define an additional subscriber to the publishers' subscriber's list with variable name `subscriber_3` and name `"suffolk"`.

### Files
Code is copied below and is also available in [lab04-01-01.py](lab-04-01-01.py)


```python

import queue

class Publisher:
	def __init__(self):
		self.message_queue = queue.Queue()
		self.subscribers = []

	def subscribe(self, subscriber):
		self.subscribers.append(subscriber)

	def publish(self, message):
		self.message_queue.put(message)
		for subscriber in self.subscribers:
			subscriber.receive(message)

class Subscriber:
	def __init__(self, name):
		self.name = name

	def receive(self, message):
		print(f"{self.name}"+"received message:"
			+f"{message}")

publisher = Publisher()

subscriber_1 = Subscriber("Subscriber 1")
subscriber_2 = Subscriber("Subscriber 2")

publisher.subscribe(subscriber_1)
publisher.subscribe(subscriber_2)

publisher.publish("Hello World")

```
Here is the same code with some comments explaining the step by step process followed for this system.

```python

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


```

### PUB/SUB System 2:_Using Python's threading module_

This lab will get you working with another basic implementation of the Publisher-Subscriber 
 pattern using **threading**, allowing for asynchronous message delivery to multiple 
 subscribers based on topics.

Here is what happens in the code in more detail:

 1. **Threading**: The code uses the threading module to manage concurrent execution. 
 Each subscriber has an Event object that allows them to wait for a message from the 
 publisher.
 
 2. **Publisher Class:**
 
 -- **Initialisation**: The Publisher class initializes an empty dictionary called 
    subscribers, where each key is a topic and the value is a list of subscribers 
    interested in that topic.
 -- **Subscribe Method**: This method allows a subscriber to subscribe to a specific 
    topic. It checks if the topic exists in the dictionary; if not, it creates a 
    new list for that topic and appends the subscriber.
 -- **Publish Method**: This method sends a message to all subscribers of a specified 
    topic. It sets the event for each subscriber, indicating that a message is 
    available, and assigns the message to the subscriber's message attribute.

 3. **Subscriber Class**:
 
 -- **Initialisation**: The Subscriber class initializes with a name, an Event object 
    for synchronization, and a message attribute set to None.
 -- **Receive Method**: This method waits for the event to be set (indicating a message 
    is available). Once the event is set, it prints the received message, then clears 
    the event to prepare for the next message.
 
 4. **Creating Instances**: The code creates a Publisher instance and several Subscriber 
    instances. It subscribes each subscriber to specific topics.
 
 5. **Publishing and Receiving Messages**: Finally, the publish method is called to send 
    a message to the "sports" topic, and subscriber_1 calls its receive method to 
    print the received message.

#### Lab Tasks:
**Task 1.** Study the code and understand the logic, as well as the steps that are followed for the PUB/SUB system to work. Compare it with PUB/SUB system 1 in lab-04-01-01.py
**Task 2.** Define a couple of additional subscribers to the publishers' subscriber's list (such as yourself or the people sitting around you)
**Task 3.** Subscribe each subscriber to different topics.
**Task 4.**  Define and publish a couple of more additional messages for your new topics

### Files
Code is copied below and is also available in [lab04-01-02.py](./lab-04-01-02.py)

```python
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

# Subscribe subscribers to different topics
publisher.subscribe(subscriber_1, "sports")          # Subscriber 1 subscribes to "sports"
publisher.subscribe(subscriber_2, "entertainment")   # Subscriber 2 subscribes to "entertainment"
publisher.subscribe(subscriber_3, "sports")          # Subscriber 3 subscribes to "sports"

# Publish a message to the "sports" topic
publisher.publish("Soccer match result", "sports")
# Call the receive method of subscriber_1 to process the message
subscriber_1.receive()
```