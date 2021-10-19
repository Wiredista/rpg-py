import rpg_utils

mapa   = rpg_utils.Map(30, 30)
player = rpg_utils.Player(mapa)
print(mapa)

def walk(dir: str = "") -> bool:
    global player
    global mapa
    dir = dir.lower()
    x = False
    if dir == "n" or dir == "north":
        x = player.move(rpg_utils.north)
    elif dir == "s" or dir == "south":
        x = player.move(rpg_utils.south)
    elif dir == "e" or dir == "east":
        x = player.move(rpg_utils.east)
    elif dir == "w" or dir == "west":
        x = player.move(rpg_utils.west)
    else:
        print(f"Unknown direction \"{dir}\" . Known values: north, south, east, west")
        return False
    print( mapa)
    if not x:
        print(" Can't move! ")  
    return x


def help(*args):
    print(" NOT IMPLEMENTED ")
    return True

commands = {
    "walk": walk,
    "move": walk,
    "mv":   walk,
    "help": help,
    "?":    help
}

def repl():
    while True:
        command = input("> ")
        try:
            args = command.split()[1:]
            command = command.split()[0]
            if command not in commands:
                print(f" Unknown command {command}")
                print(f" Use 'help' or '?' for help")

            response = commands[command](*args)
            if response:
                print(" Ok! ")
            elif response == None:                
                print(" Ok? ")
            else:
                print(" Uh. ")
        
        except Exception as err:
            print(" ??? ")

repl()
