import subprocess
import os

# Alias should be: conn_scr='history -a; python3 $connect_script_path'

FILE_NAME = 'connect.sh'

output = subprocess.check_output(['bash', '-i', '-c', 'history -r; history'])
last_five_commands = [" ".join(command.strip().split()[1:]) for command in output.decode().splitlines()[-6:-1]]

last_command = last_five_commands[-1]

if os.path.isfile(FILE_NAME):
	inp = raw_input(f"{FILE_NAME} already exist!\nDo you want to overwrite(y/n)?")
	if "y" not in inp.lower():
		print("OK! exiting")
		exit()

with open(FILE_NAME, 'w') as h:
	h.write("#!/bin/bash\n\n")
	h.write(last_command + "\n")
	os.chmod(FILE_NAME, 0o755)
