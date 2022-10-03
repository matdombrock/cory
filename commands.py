import pyautogui
import time # Used for waiting
import os # Used for executing system commands
import subprocess # Used for executing system commands as a subprocess

def _safeInt(str):
    # Sometimes string do not convert to ints correctly
    # This gives a user-friendly error message when this happens
    try:
        res = int(str)
        return res
    except:
        print('Cannot convert: '+str+' to int!')
        quit()
        return False

def _getXY(arg):
    # Splits an arg into X and Y integer values
    argSplit = arg.split(',')
    x = int(argSplit[0])
    y = int(argSplit[1])
    return [x,y]

def _getAB(arg):
    # Splits an arg into A and B string values
    argSplit = arg.split(',')
    a = argSplit[0]
    b = argSplit[1]
    return [a,b]

def _defaultArg(arg, default):
    # Replaces an empty arg value ("NA") with a default argument
    # If the arg does not have an empty ("NA") value, we return the original arg
    if arg == "NA":
        return default
    return arg

def _requireArg(arg):
    # Requires that user supplies an arg for this command
    # If no arg is supplied the script will quit
    if arg == "NA":
        print('ERROR: This command requires an argument!')
        quit()

def _verifyKey(arg):
    # Verifies that the key the user supplied is a valid key
    # If its not the script will quit
    foundKey = False
    for key in pyautogui.KEY_NAMES:
        if key == arg:
            foundKey = True
    if foundKey == False:
        print('ERROR: Cant find a key to press with name: '+arg)
        print('Available Names: ')
        print(pyautogui.KEY_NAMES)
        quit()
    return True

def expect(arg):
    # Expect a specific screen resolution
    # Return error if expectation is not met
    print('EXPECT: '+arg)
    _requireArg(arg)
    screenX, screenY = pyautogui.size()
    expectX, expectY = _getXY(arg)
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
    _requireArg(arg)
    x, y = _getXY(arg)
    pyautogui.moveTo(x, y, 0.2)
    return 1

def click(arg):
    # Send a click at the current mouse position
    # The value of arg determines the amount of clicks
    print('CLICK '+arg)
    arg = _defaultArg(arg, 1)
    arg = _safeInt(arg)
    for i in range(arg):
        pyautogui.click() 
    return 1

def wait(arg):
    # Wait for the given amount of time in seconds
    print('WAIT '+arg)
    arg = _defaultArg(arg, 1)
    arg = _safeInt(arg)
    time.sleep(arg)
    return 1

def write(arg):
    # Type of the given string of text
    # Can not handle new lines
    print('WRITE '+arg)
    _requireArg(arg)
    pyautogui.write(arg, interval=0.05)
    return 1

def hotkey(arg):
    print('NEWLINE '+arg)
    _requireArg(arg)
    arg = arg.lower() # All key names are lowercase
    key1, key2 = _getAB(arg)
    _verifyKey(key1)
    _verifyKey(key2)
    pyautogui.hotkey(key1, key2)
    return 1

def newLine(arg):
    print('NEWLINE '+arg)
    arg = _defaultArg(arg, 1)
    arg = _safeInt(arg)
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
    _requireArg(arg)
    os.system(arg)
    return 1

def executeSub(arg):
    print('EXECUTESUB '+arg)
    _requireArg(arg)
    subprocess.Popen([arg])
    return 1

def press(arg):
    # Press the given key
    print('PRESS '+arg)
    _requireArg(arg)
    arg = arg.lower() # All key names are lowercase
    _verifyKey(arg)
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