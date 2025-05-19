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

#Write your code below this line 👇
direction = input("Do you wanna go left or right?\n").lower()

if direction== "left":
  swim = input("Do you wanna swim or wait?\n").lower()
  if swim == "wait":
    door = input("Which door will you go through? Yellow,Red,Blue?\n").lower()
    if door == "yellow":
      Fight = input("Now you have two choices the game is at stake either choose blue pill or red pill each has its drawback but only one pill will grant you the \npower to win the treasure from the mythical beast guarding it!\n Only type red or blue\n").lower()
      if Fight == "red":
        print("You win!!!!\n you have succesesfully slayn the beast now the treausre is yours!!")
        print('''__     ___      _                   
\ \   / (_) ___| |_ ___  _ __ _   _ 
 \ \ / /| |/ __| __/ _ \| '__| | | |
  \ V / | | (__| || (_) | |  | |_| |
   \_/  |_|\___|\__\___/|_|   \__, |
                              |___/ ''')
      else:
        print("Try again you have been slayn by the beast")
    elif door == "Red":
      print("Burned by fire.\nGame over!")
    elif door == "blue":
      print("Eaten by beasts.\nGame over!")
    else:
      print("Game over!")
  else:
    print("Attacked by trout.\nGame over!")
else:
  print("You fell into a hole.\nGame over!")
  

  

