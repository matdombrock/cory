import pyautogui
import sys
import commands


state = {
    "scriptLocation": "SCRIPT.txt",
    "script":"",
    "human":False,
    "curLine":0
}

def readScript():
    f = open(state["scriptLocation"], "r")
    content = f.read()
    state["script"] = content

def executeScript():
    # Split the script into lines
    lines = state["script"].split('\n')
    if(state["human"]):
        print('Running in Human mode!')
    # Go through each line of the script
    for line in lines:
        state['curLine'] = state['curLine']+1
        print(str(state['curLine'])+': '+line)
        # We need to extract the command and the arg from the line
        cmd = 'NA' # Placeholder value
        arg = 'NA' # Placeholder value
        # Split the line into the command and the argument
        split = line.split(' ')
        # Get the command
        cmd = split[0]
        if line[0]=="#":
            # This line is a comment
            continue # Move to the next line of the script
        # Make sure the command is in uppercase
        cmd = cmd.upper()
        # Only some commands take an argument
        if len(split) > 1: # Check to see if we have an argument
            # Get the arg
            arg = split[1:]
            arg = ' '.join(arg)
        # Check that we have a valid command
        foundCmd = False
        for availableCmd in commands.listing:
            if availableCmd == cmd:
                foundCmd = True
        if foundCmd:
            res = commands.listing[cmd](arg, state)
            if(res != True):
                print('ERROR: THERE WAS A PROBLEM WITH  YOUR LAST '+cmd+' COMMAND AT LINE '+str(state['curLine']))
                print('READ: '+line)
                return
        else:
            print('ERROR: UNKNOWN COMMAND '+cmd+'AT LINE '+str(state['curLine']))
            return
    print('SCRIPT COMPLETE!')

def setup():
    if len(sys.argv) > 1 :
        state["scriptLocation"] = sys.argv[1]
    if len(sys.argv) > 2 :
        if sys.argv[2].lower() == 'human':
            state["human"] = True
    readScript()
    executeScript()
setup()
