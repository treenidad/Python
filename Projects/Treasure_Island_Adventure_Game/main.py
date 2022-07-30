print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice_1 = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'.: ")

if choice_1.lower() == "left":
  #Continue the game.
  choice_2 = input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.: ")
  if choice_2.lower() == "wait":
    #Continue the game.
    choice_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?: ")
    if choice_3.lower() == "red":
      #Death by fire.
      print("You enter and a Pokemon Trainer Red wants to battle. He sends out Pikachu. You are out of usable Pokemon. Game Over.")
    elif choice_3.lower() == "blue":
      #Death by blue beasts.
      print("You enter a room of blue beasts, none of which are Guy Sensei or Bushy Brows. The blue beasts maul you to death. Game Over.")
    elif choice_3.lower() == "yellow":
      #GAME WON!!!
      print("You found the One Piece! You are now King of the Pirates! You Win!")
    else:
      #Death by indecisiveness
      print("You can't decide which door to go through so you die of starvation. GAME OVER.")
  else:
    #Death by hungry animals.
    print("You get attacked by some very hungry, yet colorful hippos. GAME OVER.")
else:
  #Death by fall.
  print("You fall into a deep hole. GAME OVER.")
