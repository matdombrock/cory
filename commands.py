import pyautogui
import time # Used for waiting
import os # Used for executing system commands
import subprocess # Used for executing system commands as a subprocess
import commandsUtil # command utilities


def expect(arg):
    # Expect a specific screen resolution
    # Return error if expectation is not met
    print('EXPECT: '+arg)
    commandsUtil.requireArg(arg)
    screenX, screenY = pyautogui.size()
    expectX, expectY = commandsUtil.getXY(arg)
    passed = True
    if screenX != expectX:
        passed = False
    if screenY != expectY:
        passed = False
    if passed == False:
        alertText = 'Expected: '+str(expectX)+'x'+str(expectY)+'. Got: '+str(screenX)+'x'+str(screenY)
        pyautogui.alert(text=alertText, title='SCREEN RESOLUTION ISSUE', button='OK')
        return 0
    return 1

def goto(arg):
    # Move the mouse to the given coords
    print('GOTO '+arg)
    commandsUtil.requireArg(arg)
    x, y = commandsUtil.getXY(arg)
    # Create and initial mouse movement to emulate someone grabbing the mouse
    startingOffsetX = commandsUtil.randomOffset(100)
    startingOffsetY = commandsUtil.randomOffset(100)
    moveTime = commandsUtil.randomSeconds(25,100)
    pyautogui.move(startingOffsetX,startingOffsetY, moveTime)
    # Move the mouse in randomized chunks towards the target
    chunks = 3
    for chunk in range(chunks):
        # Get the current mouse position
        curX, curY = pyautogui.position()
        # Calculate the difference between the current location and the destination
        diffX = x - curX
        diffY = y - curY
        if diffX == 0 and diffY == 0:
            # We reached the target
            return 1
        # Get our current chunk number
        # Used to divide the difference into our next target
        chunkNum = chunks - chunk
        # Build our random offset
        offsetX = 0
        offsetY = 0
        if(chunk < chunks-1):# Dont randomize the last chunk
            offsetX = commandsUtil.randomOffset(300)
            offsetY = commandsUtil.randomOffset(300)
        # Generate the next target
        targetX = (diffX/chunkNum)+offsetX
        targetY = (diffY/chunkNum)+offsetY
        # Move to the next target over a random amount ms between 250 and 1000
        moveTime = commandsUtil.randomSeconds(25,100)
        pyautogui.move(targetX,targetY, moveTime)
    return 1

def click(arg):
    # Send a click at the current mouse position
    # The value of arg determines the amount of clicks
    print('CLICK '+arg)
    arg = commandsUtil.defaultArg(arg, 1)
    arg = commandsUtil.safeInt(arg)
    for i in range(arg):
        pyautogui.click() 
    return 1

def wait(arg):
    # Wait for the given amount of time in seconds
    print('WAIT '+arg)
    arg = commandsUtil.defaultArg(arg, 1)
    arg = commandsUtil.safeInt(arg)
    time.sleep(arg)
    return 1

def write(arg):
    # Type of the given string of text
    # Can not handle new lines
    print('WRITE '+arg)
    commandsUtil.requireArg(arg)
    pyautogui.write(arg, interval=0.05)
    return 1

def hotkey(arg):
    print('NEWLINE '+arg)
    commandsUtil.requireArg(arg)
    arg = arg.lower() # All key names are lowercase
    key1, key2 = _getAB(arg)
    commandsUtil.verifyKey(key1)
    commandsUtil.verifyKey(key2)
    pyautogui.hotkey(key1, key2)
    return 1

def newLine(arg):
    print('NEWLINE '+arg)
    arg = commandsUtil.defaultArg(arg, 1)
    arg = commandsUtil.safeInt(arg)
    for i in range(arg):
        pyautogui.hotkey('shift', 'enter')
    return 1

def selectAll(arg):
    print('SELECTALL '+arg)
    pyautogui.hotkey('ctrl', 'a')
    return 1

def fullScreen(arg):
    print('FULLSCREEN '+arg)
    pyautogui.press('f11')
    return 1

def alert(arg):
    print('ALERT '+arg)
    pyautogui.alert(text=arg, title='ALERT', button='OK')
    return 1

def confirm(arg):
    print('CONFIRM '+arg)
    res = pyautogui.confirm(text=arg, title='CONFIRM', buttons=['OK', 'Cancel'])
    if(res == 'Cancel'):
        print('The user ended the script!')
        quit()
    return 1

def debug(arg):
    print('DEBUG '+arg)
    return 1

def python(arg):
    print('EVAL '+arg)
    res = eval(arg)
    print('RES: '+str(res))
    return 1

def pythonFile(arg):
    print('EVAL '+arg)
    f = open(arg, "r")
    content = f.read()
    exec(content)
    return 1

def execute(arg):
    print('EXECUTE '+arg)
    commandsUtil.requireArg(arg)
    os.system(arg)
    return 1

def executeSub(arg):
    print('EXECUTESUB '+arg)
    commandsUtil.requireArg(arg)
    subprocess.Popen([arg])
    return 1

def press(arg):
    # Press the given key
    print('PRESS '+arg)
    commandsUtil.requireArg(arg)
    arg = arg.lower() # All key names are lowercase
    commandsUtil.verifyKey(arg)
    pyautogui.press(arg)
    return 1




listing = {
    "EXPECT": expect,
    "GOTO": goto,
    "CLICK": click,
    "WAIT": wait,
    "WRITE": write,
    "HOTKEY": hotkey,
    "NEWLINE": newLine,
    "SELECTALL": selectAll,
    "FULLSCREEN": fullScreen,
    "ALERT": alert,
    "CONFIRM": confirm,
    "DEBUG": debug,
    "PYTHON": python,
    "PYTHONFILE": pythonFile,
    "EXECUTE": execute,
    "EXECUTESUB": executeSub,
    "PRESS": press
}