import os, sys

import pygame
from pygame.locals import *

from system.extras import RESPONSE


# A Directory Path
# %SystemRoot%\System32\SHELL32.dll

RESPONSE("Loading Required Entries", "OK")

username = "Ravin" # Change the username for yourself
allDirectories = [
    "V:\\",
    "V:\\Users",
    "V:\\Users\\{0}".format(username.lower()),
    "V:\\Users\\{0}\\desktop".format(username.lower()),
    "V:\\Users\\{0}\\downloads".format(username.lower())
]
path = "V:\\Users\\{0}\\desktop".format(username.lower())
response = ""
registers = []
definite_values = []
bufferline = []


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

RESPONSE("Initializing Pygame...", "OK")

pygame.init()
pygame.font.init()
pygame.display.init()


width = 1000
height = 600
screen = pygame.display.set_mode((width, height))


arcane_image_location = "./system/shell32/arcane.png"
system_image_index_location = "./system/shell32/index.json"
storage_accounts_location = "./system/storage/accounts.json"
storage_directories_location = "./system/storage/directories.arcane"


# START (Extra CommandLines)

lines = ["", "", "", "", "",""]

linesSize = 32
linesFont = pygame.font.Font(None, linesSize)
linesColour = (0, 255, 255)

starting_area = 128
areas = []
next_pos = 32
for x in range(len(lines)):
    next_num = starting_area + (next_pos * x)
    areas.append(next_num)
size_one = 128
size_two = 32
default_pos_x = 32 # Keeps it all in line

linesRect = pygame.Rect(default_pos_x, areas[0], size_one, size_two)


# END

# START (Display / Buffer Display)
"""
The display is used to show information that you write.

The display is tied to the command

display on
display off
display colour {colour name}
"""

display_toggle = False
display_colour = WHITE
display_y_offset = 200
display_x_offset = 0
display_x_offset_2 = 0
display_y_offset_2 = 0
display_size_y = (height - display_y_offset)
display_size_x = (width - display_x_offset)
display_x = (0 + display_x_offset_2)
display_y = (0 + display_y_offset_2)
displayRect = pygame.Rect(display_x, display_y, display_size_x, display_size_y)

# END


textSize = 32
textFont = pygame.font.Font(None, textSize)
textColour = BLUE
textRect = pygame.Rect(32, height - 64, 128, 32)

responseSize = 32
responseFont = pygame.font.Font(None, responseSize)
responseColour = GREEN
responseRect = pygame.Rect(32, height - 120, 128, 32)

pathSize = 32
pathFont = pygame.font.Font(None, pathSize)
pathColour = RED
pathRect = pygame.Rect(32, 64, 128, 32)


if os.path.exists(arcane_image_location):
    arcane_image_destination = "./system/shell32/arcane.png"
    arcane_image = pygame.image.load(arcane_image_destination)
    pygame.display.set_caption("Arcane Engine", arcane_image_destination)
    pygame.display.set_icon(arcane_image)
else:
    arcane_image = None
    pygame.display.set_caption("Arcane Engine")


running = True
text = ""
previous_texts = []
show_previous_texts = True


RESPONSE("Starting Operating System", "OK")


class Directory:
    def Change(Entered: str):
        global response, path
        foundDir = False
        if Entered[0:2] == ".\\":
            if path == "V:\\":
                Entered = path + Entered[2:]
            else:
                Entered = path + "\\" + Entered[2:]
        for n in allDirectories:
            if n == Entered:
                foundDir = True
            else:
                continue

        if foundDir:
            path = Entered
            response = "Directory: FOUND"
        else:
            response = "Directory: [{0}] NOT FOUND".format(Entered)
        return

    def Make(Entered: str):
        global response
        allowMake = True
        for n in allDirectories:
            if n == Entered:
                allowMake = False
            else:
                continue

        if allowMake:
            allDirectories.append(Entered)
            response = "Directory: CREATED"
        else:
            response = "Directory: ALREADY EXISTS"
        return

    def Delete(Entered: str):
        global response
        foundDir = False
        for n in allDirectories:
            if n == Entered and n not in ["V:\\", "V:\\Users", "V:\\Users\\{0}".format(username.lower())]:
                foundDir = True
            elif n in ["V:\\", "V:\\Users", "V:\\Users\\{0}".format(username.lower())]:
                response = "Directory: IS REQUIRED"
                return
            else:
                continue

        if foundDir:
            allDirectories.remove(Entered)
            response = "Directory: DELETED"
        else:
            response = "Directory: DOSEN'T EXIST"
        return

def RunBuffer():
    for line in bufferline:
        if line[0:4] == "echo":
            response = "{0}".format(line[5:])
            responseResult = responseFont.render(response, True, responseColour)
            screen.blit(responseResult, responseRect)


def ProcessCommand(Input: str):
    global response, running, path, allDirectories, lines, display_toggle, text, previous_texts, show_previous_texts
    running = True
    if Input[0:2] == "cd":
        Directory.Change(Input[3:])
    elif Input[0:5] == "mkdir":
        Directory.Make(Input[6:])
    elif Input[0:3] == "del":
        Directory.Delete(Input[6:])
    elif Input[0:12] == "arcane.close":
        running = False
    elif Input[0:3] == "ild":
        sammon = Input[4:6]
        value = Input[7:9]
        if sammon.startswith("@"):
            registers.append([sammon, value])
        elif sammon.startswith("$"):
            definite_values.append([sammon, value])
        response = "Created SYS Variable: {0}::{1}".format(sammon, value)
    elif Input[0:1] == "$":
        sammon = Input[0:3]
        for n in definite_values:
            if n[0] == sammon:
                response = "Stored SYS Variable: {0}::{1}".format(n[0], n[1])
            else:
                continue
    elif Input[0:1] == "@":
        sammon = Input[0:3]
        for n in registers:
            if n[0] == sammon:
                response = "Stored SYS Register: {0}::{1}".format(n[0], n[1])
            else:
                continue
    elif Input[0:4] == "call":
        LINE = 0
        CONTENTS = ""
        LINE = Input[4:6]
        CONTENTS = Input[7:]
        response = "[{0}] {1}".format(LINE, CONTENTS)
        bufferline.insert(int(LINE), CONTENTS)
    elif Input[0:6] == "buffer":
        RunBuffer()
    elif Input[0:3] == "run":
        line = Input[4:]
        if line[0:4] == "echo":
            response = "{0}".format(line[5:])
    elif Input[0:5] == "bunny":
        allDirectories = []
        registers = []
        definite_values = []
        path = "V:\\"
        bufferline = []
        text = ""
        previous_texts = []
        allDirectories.append("V:\\")
        allDirectories.append("V:\\Users")
        response = "Arcane engine restarted... All channels reset...  No Users Available... * adduser *"
    elif Input[0:7] == "adduser":
        username = Input[8:]
        low_username = username.lower()
        allDirectories.append("V:\\Users\\{0}".format(low_username))
        allDirectories.append("V:\\Users\\{0}\\desktop".format(low_username))
        allDirectories.append("V:\\Users\\{0}\\downloads".format(low_username))
    elif Input[0:10] == "display on":
        display_toggle = True
        response = "Display: ON"
    elif Input[0:11] == "display off":
        display_toggle = False
        response = "Display: OFF"
    elif Input[0:5] == "clear":
        previous_texts = []
        response = "Cleared the console"
    elif Input[0:24] == "console_log.render False":
        show_previous_texts = False
    elif Input[0:23] == "console_log.render True":
        show_previous_texts = True
    else:
        response = "Entered Command Dosen't Exist"
    return



while running:
    responseResult = responseFont.render(response, True, responseColour)
    textResult = textFont.render(">> "+ text, True, textColour)
    screen.blit(textResult, textRect)
    screen.blit(responseResult, responseRect)
    if len(previous_texts) > 5:
        previous_texts.pop(0)

    if display_toggle:
            pygame.draw.rect(screen, display_colour, displayRect, 5)

    elif not display_toggle:
        pathResult = pathFont.render(path, True, pathColour)
        screen.blit(pathResult, pathRect)
        for x in range(len(previous_texts)):
            linesRect = pygame.Rect(default_pos_x, areas[x], size_one, size_two)
            linesResult = linesFont.render(">> " + previous_texts[x], True, linesColour)
            screen.blit(linesResult, linesRect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if len(text) > 0:
                    text = text[:-1]
            elif event.key == 13:
                ProcessCommand(text)
                if show_previous_texts:
                    if not text[0:5] == "clear":
                        previous_texts.append(text)
                text = ""
            else:
                text += event.unicode
    
    pygame.display.update()
    screen.fill(BLACK)

RESPONSE("Stopping Operating System", "OK")

RESPONSE("Uninitializing Pygame", "OK")
pygame.display.quit()
pygame.font.quit()
pygame.quit()

RESPONSE("Operating System Offline", "OK")

sys.exit()
