def factorial(number):
    if number == 1:
        return 1 
    else:
        return number*factorial(number-1)
print(factorial(100))        

def addition(n2):
    if n2 == 0:
       return 0 
    else:
        return n2+addition(n2-1)
print(addition(3))    

def fibonacci(n1):
    if n1 == 0 or n1 == 1:
        return n1
    else:
        return fibonacci(n1-1)+fibonacci(n1-2)    
    
print(fibonacci(10))

#def palindrome():
    #question = input("Write your text: ")
    #if question == question[::-1]:
        #print("It's a palindrome!")
    #else:
        #print("It's not a palindrome.")
    

#while True:
    #palindrome()

def power(base,exp):
    if exp == 0:
        return 1
    if exp < 0:
        return 1/power(base,-exp)    
    return base*power(base,exp-1)    
print(power(4,-2))    

def generate_subsets(current,remaining):
    if not remaining: 
        return [current]
    without_current = generate_subsets(current,remaining[1:])
    with_current = generate_subsets(current+[remaining[0]],remaining[1:])
    return without_current+with_current

elements = [1,2,3,4,5]
all_subsets = generate_subsets([],elements)
print("subsets",all_subsets)
    
