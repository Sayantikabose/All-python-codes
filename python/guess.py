
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.

# If they run out of turns, provide feedback to the player. 
import random 

print("Welcome to the guessing game")
a=[1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,100] 

actual_no = random.choice(a)

user = int(input("Choose a number from 1 to 100"))
level = input("Choose the level of difficulty,easy or hard")
easy_ch = 10
hard_ch=5
if(level=="easy"):
   print("You have 10 attempts to guess the right answer") 
   
   while(easy_ch>0):
       if(user >actual_no):
           easy_ch=easy_ch-1
           print("Too high")
           print("You have",easy_ch,"attempts left")
           user=int(input("Guess another number"))
       elif(user<actual_no):
            easy_ch=easy_ch-1
            print("Too low") 
            print("You have",easy_ch,"attempts left")
            user=int(input("Guess another number"))
       else:
          print("You have won, the correct answer is",actual_no) 
          break


elif(level=="hard"):
    print("You have 5 attempts to guess the right answer")
    while(hard_ch>0):
       if(user >actual_no):
           hard_ch=hard_ch-1
           print("Too high")
           print("You have",easy_ch,"attempts left")
           user=int(input("Guess another number"))
       elif(user<actual_no):
            hard_ch=hard_ch-1
            print("Too low") 
            print("You have",easy_ch,"attempts left")
            user=int(input("Guess another number"))
       else:
          print("You have won, the correct answer is",actual_no) 
          break


if(easy_ch==0 or hard_ch==0):
    print("You ran out of guesses, YOU LOSE")

