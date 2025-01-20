## 🧪 Distributed Cloud Computing Labs 🧪

Welcome to the Distributed Systems Lab Page! Here, you will find all the essential labs for the module I teach on distributed systems, designed to enhance your understanding of key concepts and practical applications. Each lab is structured to provide hands-on experience with real-world scenarios, fostering critical thinking and problem-solving skills. Explore the various topics, from communication protocols to consistency models, and engage with the materials to deepen your knowledge in this exciting field!

First prefix of labs corresponds to lecture number for ease of reference.

* Lab 04.01: Experimenting with a Publish Subscribe Architecture in Python
* Lab 04.02: Experimenting with a Client-Server Architecture in Python
* Lab 04.03: Creating a messaging application using RabbitMQ - Hello World
* Lab 04.04: Creating a messaging application using RabbitMQ - Publish/Subscribe

* Lab 05.01: Creating a messaging application using RabbitMQ - Work queues
* Lab 05.02: Creating a messaging application using RabbitMQ - Routing (receiving messages selectively)
* Lab 05.03: Creating a messaging application using RabbitMQ - Topics (receiving messages matching a pattern)
* Lab 05.04: Creating a messaging application using RabbitMQ - RPC

### Getting started with working on the labs in this space

The lab files in this module will most likely involve you creating a github account (if you do not have one already), logging in and forking this repository (= making a copy in your own space) to do further work. 

Below I have included some step by step instructions on how to do some of these steps before you can start working on the labs. 

#### a. Register/Create a github username

#### b. 

#### c. How to Fork and Run a Python 3 File in GitHub Codespaces

##### Step 1: Fork the Repository
1. **Log in to GitHub**: Go to [GitHub](https://github.com) and log in to your account.
2. **Navigate to the Repository**: Go to the public repository that contains the Python file you want to work on.
3. **Fork the Repository**:
   - Click on the **"Fork"** button located in the top right corner of the repository page. This creates a copy of the repository in your own GitHub account.

##### Step 2: Set Up GitHub Codespaces
1. **Open Your Forked Repository**: Navigate to your GitHub profile and open the newly forked repository.
2. **Launch Codespaces**:
   - Click on the **"Code"** button (green button) above the repository files.
   - Select **"Codespaces"** from the dropdown menu.
   - Click on **"New codespace"** to create a new Codespace environment. Wait a moment for the setup to complete.

##### Step 3: Locate and Open the Python File
1. **Explore the File Tree**: In the Codespaces environment, locate the Python file (e.g., `publisher_subscriber.py`) that you want to edit. It should be visible in the file explorer on the left side.
2. **Open the File**: Click on the file to open it in the editor.

##### Step 4: Modify the Code (if needed)
1. **Edit the File**:
   - Make any changes or additions to the code as needed for your practice.
2. **Save the File**: Don’t forget to save your changes (you can use `Ctrl + S` or `Cmd + S` on Mac).

##### Step 5: Install Python (if not already available)
1. **Check Python Installation**:
   - In the terminal, type `python3 --version` to check if Python 3 is installed. If it’s not installed, you can install it by running:
     ```bash
     sudo apt-get update
     sudo apt-get install python3
     ```

##### Step 6: Run the Python File
1. **Run the Script**:
   - In the terminal, ensure you are in the directory where your Python file is located (if necessary).
   - Type the following command to run your script:
     ```bash
     python3 publisher_subscriber.py
     ```
2. **View the Output**: You should see the output of your program in the terminal, displaying the message received by each subscriber.

#### Step 7: Commit and Push Your Changes
1. **Stage Your Changes**:
   - In the terminal, run:
     ```bash
     git add publisher_subscriber.py
     ```
2. **Commit Your Changes**:
   - Run:
     ```bash
     git commit -m "Modify publisher-subscriber code"
     ```
3. **Push to Your Fork**:
   - Run:
     ```bash
     git push origin main
     ```

#### Conclusion
Now you’ve successfully forked a public repository, run a Python script in GitHub Codespaces, and made modifications! If you have any questions or need further assistance, feel free to reach out during the lectures. Enjoy! 🚀