# ArcaneEngine
The ArcaneEngine is designed to be a python created virtual machine runner, that allows the creation and running of a custom created operating system using the built in tools

- Note: Currently unable to create custom operating systems. will come soon


# Command Processing
#### Aka CommandLine

- cd
Allows the changing of directories. Usage: cd {directory} /or/ cd {./next_directory}

- mkdir
Allows the creation of new directories. Usage: mkdir {directory} /NOTE: Cannot be used like cd's second option/

- del
Allows the deletion of directories. Usage: del {directory} /NOTE: Cannot be used like the cd's second option/

- arcane.close /or/ Click [X]
Allows the shutdown of the system

-ild
Allows the creation of register variables and definite variables. Usage: ild ${HexValues (2) 0-F} {HexValues (2) 0-F} /and/ ild @{HexValues (2) 0-F} {HexValues (2) 0-F}

-$
Allows you to get the values stored under a definite values. Usage: ${HexValues (2) 0-F}

-@
Allows you get the values stored under a register. Usage: @{HexValues (2) 0-F}

-call
Allows the running of system code. Usage: call {HexValues (2) 0-F} {Arcane Assembly Language}

-bunny
Allows the complete reset of the arcane engine. Usage: bunny /NOTE: Only use if needed/

-adduser
Allows the creation of a new user account. Usage: adduser {username 0-1 A-Z a-z}

-display on
Turns on the custom display. Usage: display on

-display off
Turns off the custom display. Usage: display off

-clear
Clears the consoles log on the display. Usage: claer

-console_log.render True
Turns on the render of the console log. Usage: console_log.render True

-console_log.render False
Turns off the render of the console log. Usage: console_log.render False
