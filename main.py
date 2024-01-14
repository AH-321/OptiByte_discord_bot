import os
import src.logo as logo 

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()

    logo.displayLogo()

    print("\n\033[1m" + "Discord Bot" + "\033[0m")
    print("Please make selection:\n")


    # read for files inside source dir and print them
    i = 1
    for file in os.listdir('src'):
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
        os.system('python3 src/' + os.listdir('src')[int(selection)])

main()
