# Trnaslates text file into skript messages to do in a minecraft chat

help_txt = """
Example:

Input text file:
&7This is a &o'cool'
&4red message
&b&lto send a player in chat with Skript!

The Output:
message "&7This is a cool"
message "&4red message"
message "&b&lto send a player in chat with Skript!"

Options:
debug - e.g. python debug <file name>
"""

import sys, time
# print(sys.argv)

# Help menu
def help():
    time.sleep(0.3)
    print("About: This program takes a text file's content and converts it into a Minecraft chat\nmessage that can be used in a Skript!")
    time.sleep(0.1)
    print(help_txt)
    sys.exit(0)


if sys.argv[1] == 'help':
    help()

# Welcome message!
print("This python script converts a text file full of words into a skript minecraft chat!")
print("Type 'help' for help!\n")
time.sleep(1)

isDebug = bool
input_file = sys.argv[1]

# Take file and help arguments
if sys.argv[1] == "--debug":
    if not sys.argv[2].endswith(".txt"):
        print("We only except .txt files to be coverted!")
        exit()
    else:
        isDebug = True
        input_file = sys.argv[2]
else:
    isDebug = False
    # Too much args
    if len(sys.argv) > 2:
        print("This takes only one argument!\nUsage: python <file name> | help\n")
        exit()

    # Not enough args
    elif len(sys.argv) == 1:
        print("This takes one argument!\nUsage: python <file name> | help\n")
        exit()
    else:
        if not sys.argv[1].endswith(".txt"):
            print("We only except .txt files to be coverted!")
            exit()

print(isDebug, sys.argv[1])


# Get file argument without any slashes by windows powershell tabbing or anything else
import re
input_file = re.sub(r'(/+|\\+)', '', input_file)

# Get rid of txt extension
file_name = input_file.split(".txt")[0].replace(".", "")

with open(file_name + '.txt', "r+") as text:
    text = text.readlines()

    # Makes new file with translated skript stuff
    new_file = open(f'{file_name}_skripted.txt', "w+")

    # Replace all double quotes to single quotes
    for count, i in enumerate(text):
        if '"' in i:
            i = i.replace('"', "'")
            text[count] = i

    line_count = count = 0
    for line in text:
        line_count += 1

        # Remove newlines, surround text files line with message "" for Skript's syntax
        line = line.replace("\n", "")
        msgd_line = f'message "{line}"'

        if isDebug:
            print(line_count, msgd_line)

        # Write to new file
        new_file.write(f'{msgd_line}\n')

    new_file.close()

    print(f"Finished! Output file is {file_name}_skripted.txt")
