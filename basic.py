import os
from groq import Groq

# Color codes for questions and answers
QUESTION_COLOR = '\033[91;1m' # Red
ANSWER_COLOR = '\033[94;1m'    # Blue
END_COLOR = '\033[92m'           # End color
cyan_COLOR = '\033[96;3m'
NEW_COLOR = '\033[93;3m'
RESET_COLOR = '\033[0m'



# Directly use the API key
api_key = 'your_API_Key_here'

try:
    # Initialize the Groq client with the API key
    client = Groq(api_key=api_key)
    print("Client initialized successfully.")
except Exception as e:
    print("Error initializing client:", e)
    client = None

def get_response(user_input):
    if client is None:
        return "Client initialization failed. Cannot process the request."

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model="llama3-8b-8192",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        print("Error during API request:", e)
        return "An error occurred while processing your request. Please try again later."

def print_question(question):
    print(QUESTION_COLOR + question)

def print_answer(answer):
    print(ANSWER_COLOR + answer )

def programming_module():
    print("\n"+ NEW_COLOR + "Welcome to Programming Module!" + QUESTION_COLOR )
    print( NEW_COLOR+ "This module covers programming topics such as Python, Java, C++, etc." + QUESTION_COLOR+ "\n")
    while True:
        user_input = input( QUESTION_COLOR +"You: " + QUESTION_COLOR)
        if user_input.lower() == "exit":
            print(NEW_COLOR+ "Exiting Programming Module.\n")
            break

        response = get_response(user_input)
        print_answer("Programming Tutor AI: " + response + "\n")

def databases_module():
    print("\n"+ NEW_COLOR + "Welcome to Database Module!" + QUESTION_COLOR )
    print( NEW_COLOR+ "This module covers Database management system" + QUESTION_COLOR + "\n")
    while True:
        user_input = input( QUESTION_COLOR +"You: " + QUESTION_COLOR)
        if user_input.lower() == "exit":
            print(NEW_COLOR+ "Exiting Database Module.\n")
            break

        response = get_response(user_input)
        print_answer("Database Tutor AI: " + response + "\n")

def algorithms_module():
    print("\n"+ NEW_COLOR + "Welcome to Algorithm Module!" + QUESTION_COLOR )
    print( NEW_COLOR+ "This module covers topics related to Algorithm " + QUESTION_COLOR + "\n")
    while True:
        user_input = input( QUESTION_COLOR +"You: " + QUESTION_COLOR)
        if user_input.lower() == "exit":
            print(NEW_COLOR+ "Exiting Algorithm Module.\n")
            break

        response = get_response(user_input)
        print_answer("Algorithm Tutor AI: " + response + "\n")

def operatingsystem_module():
    print("\n"+ NEW_COLOR +"Welcome to Operating System Module!" + QUESTION_COLOR )
    print( NEW_COLOR+ "This module covers Database management queries" + QUESTION_COLOR+ "\n")
    while True:
        user_input = input( QUESTION_COLOR +"You: " + QUESTION_COLOR)
        if user_input.lower() == "exit":
            print(NEW_COLOR+ "Exiting Operating System Module.\n")
            break

        response = get_response(user_input)
        print_answer("Operatinf System Tutor AI: " + response + "\n")

def computernetwork_module():
    print("\n"+ NEW_COLOR + "Welcome to Computer Network Module!" + QUESTION_COLOR )
    print( NEW_COLOR+ "This module covers topic related to Computer Network" + QUESTION_COLOR + "\n")
    while True:
        user_input = input( "\n"+ QUESTION_COLOR +"You: " + QUESTION_COLOR)
        if user_input.lower() == "exit":
            print(NEW_COLOR+ "Exiting Computer Network Module.\n")
            break

        response = get_response(user_input)
        print_answer("Computer Network Tutor AI: " + response + "\n")

def datastructure_module():
    print("\n"+ NEW_COLOR + "Welcome to Data Structure Module!" + QUESTION_COLOR )
    print( NEW_COLOR+ "This module covers topics related to Data Structure." + QUESTION_COLOR + "\n")
    while True:
        user_input = input( QUESTION_COLOR +"You: " + QUESTION_COLOR)
        if user_input.lower() == "exit":
            print(NEW_COLOR+ "Exiting Data Structure Module.\n")
            break

        response = get_response(user_input)
        print_answer("Data Structure Tutor AI: " + response + "\n")


def artificialintelligence_module():
    print("\n"+ NEW_COLOR + "Welcome to Artificial Intelligence Module!" + QUESTION_COLOR )
    print( NEW_COLOR+ "This module covers topics related to Artificial Intelligence." + QUESTION_COLOR+ "\n")
    while True:
        user_input = input( QUESTION_COLOR +"You: " + QUESTION_COLOR)
        if user_input.lower() == "exit":
            print(NEW_COLOR+ "Exiting Artificial Intelligence Module.\n")
            break

        response = get_response(user_input)
        print_answer("Artificial Intelligence Tutor AI: " + response + "\n")




def main():
    print(cyan_COLOR + "Hello, I am Genny AI" + QUESTION_COLOR )
    print(cyan_COLOR + "I'm here to assist students with computer science topics. Please choose a module:" + QUESTION_COLOR )
    print(cyan_COLOR + "1. Programming" + QUESTION_COLOR  )
    print(cyan_COLOR + "2. Databases" + QUESTION_COLOR )
    print(cyan_COLOR + "3. Algorithm"+ QUESTION_COLOR  )
    print(cyan_COLOR + "4. Operating System" + QUESTION_COLOR )
    print(cyan_COLOR + "5. Computer Network" + QUESTION_COLOR )
    print(cyan_COLOR + "6. Data Structure" + QUESTION_COLOR )
    print(cyan_COLOR + "7. Artificial Intelligence" + QUESTION_COLOR  + "\n")
    print(cyan_COLOR + "8. EXIT" + QUESTION_COLOR  + "\n")

    

    while True:
        choice = input(END_COLOR + "Enter the module number you want to explore (or 'exit' to quit): " + QUESTION_COLOR  )
        if choice == "1":
            programming_module()
        elif choice == "2":
            databases_module()
        elif choice == "3":
            algorithms_module()
        elif choice == "4":
            operatingsystem_module()
        elif choice == "5":
            computernetwork_module()
        elif choice == "6":
            datastructure_module()
        elif choice == "7":
            artificialintelligence_module()
        elif choice =="8":
            print(END_COLOR + "Goodbye!.\nHave a nice day." + RESET_COLOR)
            break
        else:
            print(  END_COLOR + "Invalid choice. Please select a valid module." + RESET_COLOR )

if __name__ == "__main__":
    main()

