
def check():
    vowels = ['a','e','i','o','u', 'A','E','I','O','U']
    for i in statement:
        if i in vowels: #checking if a character is a vowel using the list
            print("Vowel exists")
            return  
    print("Vowel does not exist")

while True:
    statement = input("Enter your statement or press Enter to exit: ")
    if statement:
        check()
    
    elif statement == "":  
        print("Goodbye")
        break
    
    

