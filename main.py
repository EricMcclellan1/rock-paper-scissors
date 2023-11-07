import random #the random module so we can use randomness for our computer to play rock, paper, scissors with us and not use the same responses

#ascii art below for each piece of game
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#👇

game_images = [rock, paper, scissors] #Putting the images/art in a list in order of how we'll get the input from users with 0 being rock and so on.


user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n")) #We're going to get the input from users in int form, so we can play the game

if user_choice >=3 or user_choice <0: #If user puts in a number above 2 or lower than 0, we will end the game and say they lost
  print ("You typed invalid number, so you lost sucker! lol ;-P")
else:
  print(game_images[user_choice]) #if they put in a number within our set, then we will print image of the users choice
  
  
  computer_choice = random.randint(0, 2) #Getting a random choice for the computer between 0 and 2
  print ("Computer chose:")
  print (game_images [computer_choice]) #print out the image on what the random computer choice was
  
  
  if user_choice == 0 and computer_choice == 2: 
    print ("You Win!") #if user plays rock and computer play scissors, we win!
  elif computer_choice == 0 and user_choice ==2:
      print("YOu lose") #if computer plays rock and users plays scissors,we lose
  elif computer_choice > user_choice:
    print ("You Lose!") #else if computer plays a # bigger than user choice (since the images are in order of strength) then we lose
  elif user_choice > computer_choice:
    print ("You win bro!") #else if user plays a #bigger than computer choice (since images are in order of strength) then we win
  elif computer_choice == user_choice: 
    print ("It's a Draw! You lucked out this time bud") #if user and computer pick the same thing, then it's a draw!
  