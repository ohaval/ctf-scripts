import subprocess
import os

# Alias should be: get_flag='history -a; python3 $get_flag_path'

FILE_NAME = 'get_flag.sh'

challenge_name = "- ".join(os.getcwd().split("/")[-2:])

output = subprocess.check_output(['bash', '-i', '-c', 'history -r; history'])
last_five_commands = [" ".join(command.strip().split()[1:]) for command in output.decode().splitlines()[-6:-1]]

last_command = last_five_commands[-1]

if os.path.isfile(FILE_NAME):
	inp = raw_input("get_flag.sh already exist!\nDo you want to overwrite(y/n)?")
	if "y" not in inp.lower():
		print("OK! exiting")
		exit()

with open(FILE_NAME, 'w') as h:
	h.write("#!/bin/bash\n\n")
	h.write("# Challenge_name: {}\n\n".format(challenge_name))
	h.write(last_command + "\n")
	os.chmod(FILE_NAME, 0o755)

output = subprocess.check_output(['./get_flag.sh'])

with open('flag.md', 'wb') as h:
	h.write(output)
