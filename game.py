import sys
import time

speed = 0

def main():
    print("\n", end='')
    global speed
    while True:
        speed = (input("enter speed from 1 to 10 or type 'exit': ")) 
        if speed.lower() == 'exit':
            sys.exit()
        try:
            speed = float(speed) / 100
        except ValueError:
            continue
        if speed < .01 or speed > 1:
            continue
        
        
        print("\n", end='')
        if slowinput("Welcome to the Dark Forest. (press) Enter, if you dare. ", end="") != "":
            sys.exit()

        new()
        slowprint("You see  before you a darkened tunnel that disappears amid the skeletal branches", end='')
        ellipse()
        slowprint("The ground is littered with decaying leaves. You hear a *CRACK*!!!")

        r2 = slowinput("Do you (a) run, or (b) look for the source? ", end='').strip().lower()
        if r2 == "a":
            new()
            slowprint("You run for your life, kicking up leaves, sending birds squawking through the air.\n\nThe blood pounds in your ears drowning out the sound of pursuit.\n\nA hissing like an enraged steam engine grows in your peripheral until it consumes you in a vicious slash of sound and violence.\n\nAll goes dark. \n\nYou died a horrible death. Restarting", end='')
            ellipse()
            continue
        elif r2 == "b":
            new()
            slowprint("next decision")
            break
        else:
            continue

def ellipse():
    for _ in range (4):
        print(".", end="", flush=True)
        time.sleep(speed * 5)
    print("\n")

def slowprint(text, end="\n\n"):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print(end=end)

def slowinput(text, end="\n"):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print(end=end)
    return input()

def new():
    line = "+-----------------------------------------------------------------------------------+"
    print("\n", line, "\n")
    

if __name__ == "__main__":
    main()
