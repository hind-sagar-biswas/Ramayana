import os
import subprocess

DEBUG = 0

command = ["python", "-u", "main.py"]
install = input("$_INSTALL [y/N] ?\n>")
loc = "src"


if DEBUG: loc = "dev"
if install.lower == "y":
    command = ["pyinstaller"]
    if not DEBUG: command.append("--noconsole")
    command.append(f"--icon=./{loc}/images/logo.ico")
    command.append(f"--add-data=./{loc}/images;images")
    command.append(f"--add-data=./{loc}/fonts;font")
    command.append(f"--add-data=./{loc}/book;book")
    command.append(f"./{loc}/main.py")
else:
    os.chdir(f".\{loc}")

subprocess.run(command, shell=True)