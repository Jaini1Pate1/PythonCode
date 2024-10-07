###################################
#
#   RUN AS 'ROOT' or USE 'SUDO'
#
###################################

import random as ran
import time
import os

# Just a time pass.
print ('''
	  
	   
	   
     ██  █████  ██ ███    ██ ██  ██ ██████   █████  ████████ ███████  ██ 
     ██ ██   ██ ██ ████   ██ ██ ███ ██   ██ ██   ██    ██    ██      ███ 
     ██ ███████ ██ ██ ██  ██ ██  ██ ██████  ███████    ██    █████    ██ 
██   ██ ██   ██ ██ ██  ██ ██ ██  ██ ██      ██   ██    ██    ██       ██ 
 █████  ██   ██ ██ ██   ████ ██  ██ ██      ██   ██    ██    ███████  ██ 
	   
	   

''')

# List of the character is MAC address. 
hex_bit = ['1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

# Asking user about some question I have.
change_interval = int(input('MAC should change is how many second(s) == '))
some_space_for_people_who_want_clean_output = print('\n\n')
interface = 'eth0'  # Just to make it default if someone press enter in next prompt.
interface = input('On which interface you want to change MAC address (like: eth0) == ').strip()

# Telling hacker how to come out of hacker character and be normal person
#	once they got the data they want.
print('Press "ctrl+c" to quit the hacker character and be normal again, hope you get what ever you want')

# Getting your original MAC address safe.
terminal_command = "ip link show " + interface + " | awk '/ether/ {print $2}'"
original_mac = os.popen(terminal_command).read().strip()

# Worker (funtion) which assign new MAC address every time you request.
def assign_new_mac(interface, new_mac):
	os.system(f'ifconfig {interface} down')
	out = os.popen(f'ifconfig {interface} hw ether {new_mac}').read().strip()
	os.system(f'ifconfig {interface} up')
	print(out)

# Final making you hacker. Make unstoppable loop without you entering 'ctrl+c' in terminal.
while True:
	# Creating MAC address variable to store random number and make a MAC address and because
	# 	I put it in while true loop it will be empty when the loop run again and that we want.
	mac_address = ''

	# Running a for loop for 6 time because we have MAC address in six part in linux.
	for i in range(1,7):
		mac_address += ':'
		for i in range(1,3):
			random_from_list = ran.choice(hex_bit)
			mac_address += random_from_list
	new_mac = mac_address.lstrip(':')
	assign_new_mac(interface, new_mac)
	print(f'New MAC has been set to == {new_mac}')
	time.sleep(change_interval)
