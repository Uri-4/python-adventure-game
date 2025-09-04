import sys
import time

speed = 0

def main():
    print("\n", end='')
    global speed
    while True:
        speed = (input("enter speed from 0 to 10 or type 'exit': ")) 
        if speed.lower() == 'exit':
            sys.exit()
        try:
            speed = float(speed) * .005
        except ValueError:
            continue
        if speed < 0 or speed > 1:
            continue
        
        
        print("\n", end='')
        if slowinput("Welcome to the Dark Forest. (press) Enter, if you dare. ") != "":
            continue

        new()
        slowprint("You see  before you a darkened tunnel that disappears amid the skeletal branches", end='')
        ellipse()
        slowprint("The ground is littered with decaying leaves. You hear a *CRACK*!!!")

        r2 = slowinput("Do you (a) run, or (b) look for the source? ").strip().lower()
        if r2 == "a":
            new()
            slow_print_ellipse("You run for your life, kicking up leaves and sending birds squawking through the air.\n\nThe blood pounds in your ears, drowning out the sound of pursuit.\n\nA hissing like an enraged steam engine grows in your peripheral until it consumes you in a vicious slash of sound and violence.\n\nAll goes dark. \n\nYou die a horrible death. Restarting")
            continue
        elif r2 != "b":
            continue

        new()
        slow_print_ellipse("As you turn to investigate the noise, a small shape darts through the underbrush.\n\nIt skitters away from you in disjointed bounds, leaving the impression of a large, wounded rodent. Except")
        slow_print_ellipse("That sound")
        slowprint("The chitinous insectoid scurrying which pervades your mind, that unholy sensation of fetid, invasive.... miasma")
        r3 = slowinput("(a) crash out. (b) stay calm. (c) scream. ")
        if r3 == ('a'):
            new()
            slowprint("next")
            sys.exit()
            

        else:
            continue



def slowprint(text, end="\n\n"):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print(end=end)

def slow_print_ellipse(text, end="\n\n"):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(speed)
    print(end='')
    for _ in range (4):
        print(".", end="", flush=True)
        time.sleep(speed * 5)
    print(end=end)

def slowinput(text, end=""):
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
