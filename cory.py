import pyautogui
import sys
import commands


state = {
    "scriptLocation": "SCRIPT.txt",
    "script":""
}

def readScript():
    f = open(state["scriptLocation"], "r")
    content = f.read()
    state["script"] = content

def executeScript():
    # Split the script into lines
    lines = state["script"].split('\n')
    # Go through each line of the script
    for line in lines:
        # We need to extract the command and the arg from the line
        cmd = 'NA' # Placeholder value
        arg = 'NA' # Placeholder value
        # Split the line into the command and the argument
        split = line.split(' ')
        # Get the command
        cmd = split[0]
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
            res = commands.listing[cmd](arg)
            if(res != True):
                print('ERROR: THERE WAS A PROBLEM WITH  YOUR LAST '+cmd+' COMMAND')
                print('READ: '+cmd+' '+arg)
                return
        else:
            print('ERROR: UNKNOWN COMMAND '+cmd)
            return
    print('SCRIPT COMPLETE!')

def setup():
    if(len(sys.argv) > 1):
        state["scriptLocation"] = sys.argv[1]
    readScript()
    executeScript()
setup()
