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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to Treasure Island!!!"
      "\nYour mission is to find the treasure. So make you make the right choices"
      "\nMay The Luck Lady Be With You.")
direction_choice = input("\nYou arrived at Cross Roads"
                         "\nEither go left or go right."
                         "\nMake a choice: ").lower()
if direction_choice == "left":
    task_choice = input("\nYou made the correct Choice.  "
                        "\nNow you arrived at a river.  Either Swim or Wait"
                        "\nMake a choice. (Hope you are a good swimmer ;)").lower()
    if task_choice == "wait":
        door_choice = input("\nWell done.  You arrived at the treasure place safely."
                            "\nThe treasure is in one of the door.  Which one do you want to go in?"
                            "\nYour choices are: Red, Blue or Yellow: ").lower()
        if door_choice == "red":
            print("\nSorry you were so close but Bad Choice Boy!!! You opened the door of fire."
                  "\nYou got burnt.  GAME OVER !!")
        elif door_choice == "blue":
            print("\nSorry you were so close but Bad Choice Boy!!! You opened the door of beasts."
                  "\nYou got eaten.  GAME OVER !!")
        elif door_choice == "yellow":
            print("\nCONGRATULATIONS!!!!!!!"
                  "\nYou found the hidden treasure !!")
        else:
            print("\nYou Opened a door that did not exist."
                  "\nYou fell in the Oblivion.  Sorry - GAME OVER !!")
    else:
        print("\nBad Choice Boy!!! You got eaten by hungry crocodiles"
              "\nGAME OVER")
else:
    print("\nBad Choice Boy!!! You fell in a hole"
          "\nGAME OVER")