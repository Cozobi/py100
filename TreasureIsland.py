import os
import platform

def clear_screen():
  """Clears the terminal screen."""
  system = platform.system()
  if system == "Windows":
    os.system('cls')
  elif system == "Linux" or system == "Darwin":
    os.system('clear')
  else:
    print("Operating system not supported.")

def gameover():
    print('''
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
      ''')

def intro():
        
    print("=============================================================")
    print("\n\nWelcome to Treasure Island.\nYour mission is to find the treasure\n\n")
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
    /______/______/______/______/______/______/______/______/______/______/______/
    *******************************************************************************
    ''')
    input("Press any key to continue")
    clear_screen()
    print("=============================================================")

def start():
    print(f'''
                                                   .       .
                                                    \     /
                                                 ._  '   '  _.
                                                   '  o@o  '
                                                     o@@@o
                                                 .-'  o@o  '-.
                                                     .   .
                                                    /     \
                                                   .       .

                             'Xx  xX*,
                          ,*xXXx_xXx
                            _xXXXXXxx*,
                          ,*XXx@x@Xx
                            X @|@@ `x
                            '  ||    '
                               ||
                               ||
                               ||
                               ||
                            /ssssssss.
                      /sssssssSSSSssssssssss.
        /\         /sssssSSSSSSSSSSSSSSSssssssssssss.              Dani
~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
 ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
''')
    print("\n\nYou step onto the sandy shores of Treasure Island, the air alive with the screech of unseen birds and the rustling of leaves in the dense canopy. \n\nAn ancient, weathered signpost stands before you, its wooden arms pointing in two directions. \n\nTo the left, a narrow path snakes into the shadowy depths of the jungle, promising mystery and perhaps peril.\nTo the right, the jungle looms like a solid green wall, hinting at a more direct, though potentially treacherous, route.\n")
    a=input("Which way do you choose to venture? Type 'Left' or 'right': ")
    clear_screen()
    return a

def waiting():
    print('''
          ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣤⣴⣶⣶⣶⣦⣤⣀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣶⣄⡀⠀⠀
⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀
⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀
⠀⣿⣿⠿⠿⠿⠿⠟⠛⠛⠛⠀⠛⠛⠛⠛⠛⠛⠛⠻⠿⠿⠿⠿⠿⠿⠿⠿⠿⠀
⠀⠀⠀⠀⠀⠀⠀⢠⣤⣶⣶⣶⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣶⣶⣦⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣀⣀⣤⣤⣤⣽⣿⣿⣿⣿⡿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣤⣶⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠙⠛⠿⢿⣯⣭⣝⡛⠻⢿⣿⣿⣷⣶⣶⣦⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠿⢶⣾⣿⣿⣿⣿⣿⣿⣿⡿⣿⣷⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣾⣿⣿⢿⣿⣿⢟⣡⣼⣿⠟⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣶⣿⣿⣿⠟⣡⣾⣿⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⣿⠹⣿⣿⣄⠻⣿⣿⣿⠻⣿⣿⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⠛⠛⠓⠈⠛⠛⠛⠊⠛⠛⠓⠀⠙⠛⠛⠛⠛⠓⠒⠀⠀⠀⠀  
          ''')
    
    print("\nYou decide to take the left path.\n\nThe sunlight fades as you delve deeper into the jungle's embrace. \n\nThe air grows heavy with humidity, and the sounds of the island intensify.\n\nSoon, the path opens up to the bank of a wide, swiftly flowing stream.\n\nThe opposite bank seems within reach, but the current looks strong.\n\nYou could attempt to swim across, braving whatever lurks beneath the surface, or you could wait and see if another way presents itself.\n\n")
    a= input("What will you do? Swim or wait?")
    clear_screen()
    return a

def red():
    print('''
                         (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
          ''')
    print("\nYou cautiously push open the red door. \n\nA searing wave of heat blasts you, followed by a rush of roaring flames!\n\n")
    input("Press any key to continue")
    gameover()
    
def blue():
    print("With a deep breath, you open the blue door. \n\nThe ground beneath your feet immediately gives way, and you plummet into a dark, echoing abyss. \n\nYou hear the snapping and growling of unseen beasts below.")
    input("Press any key to continue")
    gameover()
    
    
    
def yellow():
    print("You gently push open the yellow door. \n\nA golden light spills out, illuminating a chamber filled with glittering treasure! \n\nChests overflowing with gold coins, sparkling jewels, and ancient artifacts lie before you. \n\nYou've found the treasure!")

def colors():
    print('''
          
._______.    .________.     ._______.
| ┌───┐ |     | ┌───┐ |     | ┌───┐ |
| │ R │ |     | │ B │ |     | │ Y │ |
| └───┘ |     | └───┘ |     | └───┘ |
|       |     |       |     |       |
| ╔══╗  |     | ╔══╗  |     | ╔══╗  |
| ║◙ ║  |     | ║◙ ║  |     | ║◙ ║  |
| ╚══╝  |     | ╚══╝  |     | ╚══╝  |
|       |     |       |     |       |
|       |     |       |     |       |
|═══════|     |═══════|     |═══════|
‾‾‾‾‾‾‾‾      ‾‾‾‾‾‾‾‾      ‾‾‾‾‾‾‾‾
          ''')
    
    print("\nYou decide to wait by the stream. \n\nTime passes, marked by the buzzing of insects and the calls of exotic creatures. \n\nSuddenly, your attention is drawn to three ancient-looking doors built into the face of a rocky cliff nearby. \n\nEach door is a different color: one is a deep red, another a vibrant blue, and the last a sunny yellow. \n\nAn inscription above them reads: 'Choose wisely, for one path leads to fortune, the others to despair.' \n\n")
    lang = input("Which door do you choose to open? Red, blue, or yellow?")
    clear_screen()
    match lang.upper():
        case "RED":
            print("=============================================================")
            red()
        case "BLUE":
            print("=============================================================")
            blue()
        case "YELLOW":
            print("=============================================================")
            yellow()
        case _:
            print("=============================================================")
            print("You should have choosen a correct answer.")
            gameover()

if __name__ == "__main__":
    intro()
    if start().upper() == "LEFT":
        if waiting().upper() == "WAIT":
            colors()
        else:
            print("=============================================================")
            print("You plunge into the cool water of the stream.\n\nThe current tugs at you, stronger than it appeared. \n\nSuddenly, you feel sharp nips and see flashes of silver as a school of aggressive trout attacks!\n\n")
            input("Press any key to continue")
            gameover()
    else:
        print("=============================================================")
        print ("\n\nYou decide to brave the dense jungle to the right.\n\n Almost as soon as you step off the signposted area, the ground beneath your feet feels loose. \n\nBefore you can react, you stumble and fall into a hidden hole, the darkness swallowing you whole.\n")
        input("Press any key to continue")
        gameover()