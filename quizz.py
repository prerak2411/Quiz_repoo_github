import random
quiz_data = [
    {
        "question": "What does HTML stand for?",
        "options": ["A. Hyperlink Text Markup Language", "B. Hyper Transfer Markup Language", "C. Hypertext Markup Language", "D. High-Level Text Markup Language"],
        "answer": "C"
    },
    {
        "question": "Which programming language is often used for web development?",
        "options": ["A. Python", "B. Java", "C. Ruby", "D. JavaScript"],
        "answer": "D"
    },
    {
        "question": "What is the primary function of CSS in web development?",
        "options": ["A. Data storage", "B. Styling and layout", "C. Server-side scripting", "D. Database management"],
        "answer": "B"
    },
    {
        "question": "What does the acronym SQL stand for?",
        "options": ["A. Structured Query Language", "B. Simple Query Language", "C. Standard Query Language", "D. Sequential Query Language"],
        "answer": "A"
    },
    {
        "question": "Which programming language is often used for data analysis and scientific computing?",
        "options": ["A. JavaScript", "B. Java", "C. Python", "D. C++"],
        "answer": "C"
    },
    {
        "question": "What does API stand for in the context of web development?",
        "options": ["A. Application Programming Interface", "B. Advanced Programming Interface", "C. Automated Program Interaction", "D. All of the above"],
        "answer": "A"
    },
    {
        "question": "In Python, which keyword is used to define a function?",
        "options": ["A. define", "B. func", "C. def", "D. function"],
        "answer": "C"
    },
    {
        "question": "What is the output of the following code: `print(3 * 'Hello ')`?",
        "options": ["A. Hello Hello Hello Hello", "B. 9", "C. Hello Hello Hello", "D. Syntax Error"],
        "answer": "C"
    },
    {
        "question": "In JavaScript, how do you declare a variable?",
        "options": ["A. var", "B. variable", "C. let", "D. declare"],
        "answer": "A"
    },
    {
        "question": "Which data type in Python is used to represent a sequence of characters?",
        "options": ["A. int", "B. float", "C. str", "D. list"],
        "answer": "C"
    },
    {
        "question": "What is the primary purpose of version control systems like Git?",
        "options": ["A. To write code", "B. To run code", "C. To manage and track changes in code", "D. To execute code"],
        "answer": "C"
    },
    {
        "question": "What is the main advantage of object-oriented programming (OOP)?",
        "options": ["A. Simplicity", "B. Reusability", "C. Procedural nature", "D. No need for functions"],
        "answer": "B"
    },
    {
        "question": "What is the HTTP status code for a successful response?",
        "options": ["A. 200 OK", "B. 404 Not Found", "C. 500 Internal Server Error", "D. 302 Found"],
        "answer": "A"
    },
    {
        "question": "In Python, which library is commonly used for data visualization?",
        "options": ["A. NumPy", "B. Pandas", "C. Matplotlib", "D. TensorFlow"],
        "answer": "C"
    },
    {
        "question": "What is the purpose of a constructor method in object-oriented programming?",
        "options": ["A. To create objects", "B. To destroy objects", "C. To update objects", "D. To copy objects"],
        "answer": "A"
    },
    {
        "question": "Which of the following is not a valid Python data type?",
        "options": ["A. int", "B. double", "C. list", "D. tuple"],
        "answer": "B"
    },
    {
        "question": "What is the result of the following Python code: `3 + '3'`?",
        "options": ["A. 6", "B. '33'", "C. TypeError", "D. '6'"],
        "answer": "C"
    },
    {
        "question": "Which programming language is often used for developing mobile applications?",
        "options": ["A. Java", "B. Python", "C. C#", "D. PHP"],
        "answer": "A"
    },
    {
        "question": "What is the purpose of the `if` statement in programming?",
        "options": ["A. To perform a loop", "B. To declare a function", "C. To make decisions based on conditions", "D. To define a class"],
        "answer": "C"
    }
]

users_db = {}
def register():
    print("\n--- Registration ---")
    username = input("Enter a new username: ")
    if username in users_db:
        print("Username already exists. Try logging in or choose another username.")
    else:
        password = input("Enter a new password: ")
        users_db[username] = password
        print("Registration successful!")
def login():
    print("\n--- Login ---")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users_db and users_db[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False
def choose_quiz():
    print("\n--- Choose Quiz ---")
    print("1. Python")
    print("2. Java")
    print("3. Aptitude")

    
def conduct_quiz(questions):
    print("\n--- Quiz Started ---")
    selected_questions = random.sample(questions, 10)
    score = 0

    index = 1
    for i in selected_questions:
        print(f"\nQ{index}. {i['question']}")

        option_index = 1
        for option in i['options']:
            print(f"{option_index}. {option}")
            option_index += 1

        answer = input("Enter your answer (1/2/3): ")
        if i['options'][int(answer) - 1] == i['answer']:
            score += 1
        index += 1

    print(f"\nQuiz Completed! Your score is {score}/10.")
    return score
def main():
    while True:
        print("\n--- Welcome to the Quiz App ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        option = input("Enter your choice: ")

        if option == '1':
            register()
        elif option == '2':
            if login():
                while True:
                    questions = choose_quiz()
                    conduct_quiz(questions)
                    again = input("\nDo you want to attempt again? (yes/no): ")
                    if again.lower() != 'yes':
                        break
            else:
                print("Login failed. Try again.")
        elif option == '3':
            print("Exiting the quiz app. Goodbye!")
            break
        else:
            print("Invalid option. Please select again.")

