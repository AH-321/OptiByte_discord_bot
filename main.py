import os
import Discord_bot.logo as logo 

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()

    logo.displayLogo()

    print("\n\033[1m" + "Discord Bot" + "\033[0m")
    print("Please make selection:\n")


    # read for files inside Discord_bot and print them
    i = 1
    for file in os.listdir('Discord_bot'):
        if file.endswith('.py'):
            print(str(i) + ". Run " + file)
            i = i + 1
    
    print(str(i) + ". Exit")

    selection = input("\n\033[1m" + "Enter selection: " + "\033[0m")


    if int(selection) > i - 1:
        clear()
        exit()
    else:

        clear()
        os.system('python3 Discord_bot/' + os.listdir('Discord_bot')[int(selection)])

main()
