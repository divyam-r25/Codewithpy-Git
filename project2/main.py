import random
n = random.randint(1,100)
a = -1
guesses = 0
while(a != n):
    guesses +=1
    a = int(input("Guess a number:"))
    if(a > n):
        print("wrong ans! Try a lower number")
    elif(a < n):
        print("wrong ans! Try a higher number")
    else:
        print("yah! U get it right")
    
print(f"you have guessed the number {n} correctly in {guesses} attempts")
