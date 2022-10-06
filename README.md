# Cory (Scriptable Python Based GUI Bot) 
Cory is a python based interpreter for a very simple yet flexible GUI automation scripting language (CoryScript). 

The CoryScript scripting language is very human readable and looks something like SQL. A command to move the mouse to a given position is like this:

```
GOTO 100,200
```

This will move the mouse to the screen coordinates x=100, y=200.

The goal of Cory is to to decrease the cognitive load and onboarding required to write simple GUI automation scripts. In theory, just about anyone with basic computer knowledge should be able to create a bot with CoryScript. 

The secondary goal of Cory is to provide "free" humanization to your automation scripts. Cory makes it easy to ensure that the bots your create will appear like human users to anyone monitoring the app/website that it is used on. This happens by injecting small amount of randomization into the actions preformed. 

# Running a CoryScript (Setup)
Before you can use Cory, you need to ensure you have Python3 installed then you need to install the Python dependencies:

```
pip install -r requirements.txt
```

```
python cory.py someScript.txt
```

# Running Example Scripts
There are several example scripts in the `/examples` directory. You can run them like this:
```
python cory.py examples/someExample.txt
```

For instance, to run the alert example do:
```
python cory.py examples/alert.txt
```

# CoryScript Syntax
CoryScript has a very simple syntax. Each line of a script file must contain exactly one command. 

Any empty line will result in a syntax error. Each line must contain a command

A command can have anywhere between 0 and 2 arguments supplied

```
COMMAND ARGUMENT1,ARGUMENT2
```


**NOTE: Tying the commands in uppercase is not required but it is recommended.** 

Some commands have a default argument. If you are using a command with a default argument, you can omit the argument from the line.

Some commands require and argument (no default). If you are using a command that requires an argument and you do not supply one, the script will quit on that line. 

A simple CoryScript might look like this:
```
ALERT Running a new script!
GOTO 100, 100
WAIT 2
CLICK 
```

This script will show an alert box with the text "Running a new script!". Once the user clicks "OK" the mouse will be moved to 100, 100. Then the script will wait for 2 seconds and send a mouse click to the current mouse location.

Cory features basic runtime error handling for CoryScript. If your script contains a syntax error, the script will run up until that point and then quit with an error message shown in your command line output. 

CoryScript also supports comments. These follow python `#` syntax. 

```
# This is a comment
GOTO 100,100
```

# Cory Utility (Script Helper Tool)
When writing CoryScripts, you will often need to know your current screen resolution and mouse position.

To make this easier, there is a python script called `/util.py` that contains a simple helper tool to provide this info.

Run the utility:
```
python util.py
```

# CoryScript Commands
## Cheat Sheet
```
EXPECT <X>,<Y>
GOTO <X>,<Y>
CLICK <N=1>
WAIT <N=1>
HOTKEy <KEY1>,<KEY2>
NEWLINE <N=1>
SELECTALL
FULLSCREEN
ALERT <ALERT TEXT>
CONFIRM <CONFIRM TEXT>
DEBUG <DEBUG TEXT>
PYTHON <SOME PYTHON>
PYTHONFILE <SOMEFILE>
PRESS <KEY>
```

## EXPECT
```
EXPECT 640,480
EXPECT <X>,<Y>
```
Expects the screen size match the given values. If the screen size does not match the script will quit. This is useful for ensuring that the GOTO coordinates you enter will be accurate. 

X = Screen X resolution

Y = Screen Y resolution

## GOTO
```
GOTO <X>,<Y>
```
Moves the mouse to the given coordinates.

X = X Position

Y = Y Position

**NOTE: In computer software, the origin (0,0) is the top left corner of your screen. This is opposed to traditional graphing math, where the origin is the bottom left.**

```
 0 1 2 3 . . .
0
1
2
3
.
.
.
```
## SCROLL
```
SCROLL
SCROLL <N=1>
```
Scrolls the active window up or down by N scroll "clicks". This behavior will vary on each OS. A negative value scrolls down and positive scrolls up. 

N = Amount of scroll "clicks". (Default = 1)
## CLICK
```
CLICK
CLICK <N=1>
```
Sends a left mouse click at the current mouse position. 

N = Amount of times to click. (Default = 1)
## WAIT
```
WAIT
WAIT <N=1>
```
Waits for N seconds.

N = Seconds to wait. (Default = 1)
## WRITE
```
WRITE <SOME TEXT>
WRITE Hello World
```
Types out the given text. Make sure you have your text box selected with CLICK before typing
## HOTKEY
```
HOTKEY <KEY1>,<KEY2>
HOTKEY ctrl,a
```
Presses the given key combination. 

KEY1 = First key top press and hold

KEY2 = Second key to press

## NEWLINE
```
NEWLINE <N=1>
```
Creates a new line in the current text field (shift+enter).

N = Number of new lines. (Default = 1)
## SELECTALL
```
SELECTALL
```
Selects all of the text currently available (ctrl+a).
## FULLSCREEN
```
FULLSCREEN
```
Puts the active window into full screen mode if possible (f11).
## ALERT
```
ALERT <Some Alert Message>
```
Shows an alert message popup window on the screen with the given text. 

Waits for the user to press "OK" before the script continues.
## DEBUG
```
DEBUG <Some DEBUG Message>
```
Prints the given message to the command line.

Does not wait for the user to accept. 
## PYTHON
```
PYTHON <SOME PYTHON CODE>
PYTHON sum([1,2,3,4])
```
Executes the given Python code.

**NOTE: Use with caution!**
## PYTHONFILE
```
PYTHON <SOMEFILE>
PYTHON someFile.py
```
Executes the given Python file.

**NOTE: Use with caution!**
## PRESS
```
PRESS <KEY>
PRESS esc
```
Presses the given key. 

KEY  = Key to press

-------

# Available Keys
This is a list of acceptable inputs for the HOTKEY and PRESS commands
```
['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
'8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
'browserback', 'browserfavorites', 'browserforward', 'browserhome',
'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
'command', 'option', 'optionleft', 'optionright']
```

# How Does It Work?
Cory is essentially a wrapper for the PyAutoGUI module. It works by reading a script file and breaking that file into new lines. 

Each line is then broken into a command and argument. 

Using the commands `listing` dictionary created in `/commands.py`, Cory checks to see if the current line represents a valid command. 

If it does it will execute that command (usually a wrapper for some PyAutoGUI calls) and move on to the next line. 

The logic for reading and parsing the scripts is in `/cory.py`. The logic for each available command (as well as the definition of the commands listing dictionary) is in `/commands.py`. 

-------

## Freeze Requirements
`pip freeze > requirements.txt`

## Install Requirements
`pip install -r requirements.txt`