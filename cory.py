import pyautogui
import sys
import commands


state = {
    "scriptLocation": "SCRIPT.txt",
    "script":"",
    "human":False,
    "curLine":0,
    "loops": []
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
    while state['curLine'] < len(lines):
        line = lines[state['curLine']]
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
        # Check if we have a loop command
        if cmd == 'LOOP':
            # Look for an existing loop
            loopExists = False
            for loop in state['loops']:
                matchTag = loop['tag'] == arg
                matchLine = loop['line'] != state['curLine']
                if matchTag and matchLine: # found
                    print('FOUND EXISTING LOOP: '+arg)
                    state['curLine'] = loop['line']
                    loopExists = True
                    break
            if loopExists: 
                # We have set the line number to the desired loop point
                continue # return to start of while loop
            # Loop doest exist so append it
            state['loops'].append({'tag':arg, 'line':state['curLine']})
            print('CREATED NEW LOOP: '+arg)
            # Move to next line
            nextLine()
            # Loop is a special command do not run it as a normal command
            continue # return to start of while loop
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
                return # Quit
        else:
            print('ERROR: UNKNOWN COMMAND '+cmd+' AT LINE '+str(state['curLine']))
            return # Quit
        # Move to next line
        nextLine()
    print('SCRIPT COMPLETE!')

def nextLine():
    state['curLine'] = state['curLine']+1

def setup():
    if len(sys.argv) > 1 :
        state["scriptLocation"] = sys.argv[1]
    if len(sys.argv) > 2 :
        if sys.argv[2].lower() == 'human':
            state["human"] = True
    readScript()
    executeScript()
setup()
