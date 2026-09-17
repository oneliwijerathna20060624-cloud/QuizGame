count=0
while True:
    
    print(
    ''' PYTHON QUIZ 
    1. Start Quiz
    2. View Score
    3. Exit  '''
 )
    x=int(input("What's your choice : "))
    if x==1 :
        count = 0
        print (''' 1. Which planet is known as the Red Planet?
    A) Venus
    B) Mars
    C) Jupiter
    D) Mercury ''')
        ans = (input("What's the answer : "))
        if ans == 'B ':
            count=count+1
            print("Correct answer!")
        else:
            print("Wrong answer!")
        print(''' 2. What is the capital city of Australia?
    A) Sydney
    B) Melbourne
    C) Canberra
    D) Brisbane''')    
        ans = (input("What's the answer : "))
        if ans == 'C':
            count=count+1  
            print("Correct answer!")
        else:
            print("Wrong answer!")
        print(''' 3. What is the largest ocean in the world?
    A) Atlantic Ocean
    B) Indian Ocean
    C) Pacific Ocean
    D) Arctic Ocean''')
        ans = (input("What's the answer : "))
        if ans == 'C':
            count=count+1  
            print("Correct answer!")
        else:
            print("Wrong answer!")
        print('''4. Which country is famous for the ancient pyramids of Giza?
    A) Egypt
    B) Greece
    C) Mexico
    D) India''')
        ans = (input("What's the answer : "))
        if ans == 'A':
            count=count+1  
            print("Correct answer!")
        else:
            print("Wrong answer!")
        print('''5. Who painted the famous painting “Mona Lisa”?
    A) Vincent van Gogh
    B) Leonardo da Vinci
    C) Pablo Picasso
    D) Michelangelo''')
        ans = (input("What's the answer : "))
        if ans == 'B':
            count=count+1  
            print("Correct answer!")
        else:
            print("Wrong answer!")
    if x==2 :
        print(f''' RESULT 
        Correct Answers : {count}
        Wrong Answers : {5-count}
        Score : {count}/5

        ''')
    if x==3 :
        print("Thanks for playing!")
        break
    