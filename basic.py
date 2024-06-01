import os
from groq import Groq


api_key = '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'


client = Groq(api_key=api_key)


def get_response(user_input):

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

def programming_module():
    print("Welcome to Programming Module!")
    print("This module covers programming topics such as Python, Java, C++, etc.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting Programming Module.")
            break

        response = get_response(user_input)
        print("Programming Tutor AI:", response)

def databases_module():
    print("Welcome to Databases Module!")
    print("This module covers topics related to database management systems.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting Databases Module.")
            break
        response = get_response(user_input)
        print("Databases Tutor AI:", response)

def algorithms_module():
    print("Welcome to Algorithms Module!")
    print("This module covers topics related to Algorithms.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting Algorithm Module.")
            break
        response = get_response(user_input)
        print("Algorithms Tutor AI:", response)

def operatingsystem_module():
    print("Welcome to Operating System Module!")
    print("This module covers topics related to Operating System.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting Operating System Module.")
            break
        response = get_response(user_input)
        print("Operating System Tutor AI:", response)

def computernetwork_module():
    print("Welcome to Computer Network Module!")
    print("This module covers topics related to Computer Network.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting Computer Network Module.")
            break
        response = get_response(user_input)
        print("Computer Network Tutor AI:", response)

def datastructure_module():
    print("Welcome to Data Structure Module!")
    print("This module covers topics related to Data Structure.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting Data Structure Module.")
            break
        response = get_response(user_input)
        print("Data Structure Tutor AI:", response)

def artificialintelligence_module():
    print("Welcome to Artificial Intelligence Module!")
    print("This module covers topics related to Artificial Intelligence.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Exiting Artificial Intelligence Module.")
            break
        response = get_response(user_input)
        print("Artificial Intelligence Tutor AI:", response)

def main():
    print("Hello, I am Eavy AI")
    print("I'm here to assist students with computer science topics. Please choose a module:")
    print("1. Programming")
    print("2. Databases")
    print("3. Algorithm")
    print("4. Operating System")
    print("5. Computer Network")
    print("6. Data Structure")
    print("7. Artificial Intelligence")

    while True:
        choice = input("Enter the module number you want to explore (or 'exit' to quit): ")
        if choice.lower() == "exit":
            print("Goodbye!")
            break
        elif choice == "1":
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
        else:
            print("Invalid choice. Please select a valid module.")

if __name__ == "__main__":
    main()
