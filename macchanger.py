'''
Created By: Harshit Jain

This program uses subprocess module to run shell commands and re to match pattern.
'''

import re
import subprocess
from random import choice, randint
from oui import RandomOUI

#This following method fetches the current mac address
def get_current_mac(iface):

    pattern = r"([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}"
    command_output=(subprocess.check_output(["ifconfig", interface])).decode('utf-8')
    return (re.search(pattern, command_output).group())

#The following method changes the mac address to the desired mac 
def change_mac(iface, new_mac):
    #Switch the interface off using down.
    subprocess.call(["ifconfig "+str(iface)+ " down"], shell=True)
    print("Turning down your interface")
    subprocess.call(["ifconfig "+str(iface)+ " hw ether "+ str(new_mac)], shell=True)
    print("Assigning new mac")
    subprocess.call(["ifconfig "+str(iface)+ " up"], shell=True)
    return "PROCESS COMPLETED"

#Generate Random MAC ADDRESS
def random_mac():
    oui=RandomOUI()
    vendor, mac_address = oui.random_oui()
    for i in range(3):
        random_str=str(choice(str(randint(0,9))) + choice(str(randint(0,9))))
        mac_address.append(random_str)
    
    return vendor, ":".join(mac_address)


#Driver Code
if __name__ == "__main__":
    interface=input("Enter your network interface: ").strip()
    choice = int(input(('Select\n0.Check Current Mac Address \n1.Generate a Random Mac Address \n2.Custom Mac Address\n')))
    if choice == 0:
        print(get_current_mac(interface))

    elif choice == 1:
        vendor, mac = random_mac()
        print("The MAC ADDRESS CHOSEN FOR YOU IS : {} from vendor {}".format(vendor, mac),"\nChanging your mac address now")
        print(change_mac(interface, mac))        
    
    elif choice == 2:
        new_mac_address=input("Enter your desired mac address in the format AA:BB:CC:DD:EE:FF :").strip()
        change_mac(interface, new_mac_address)

    else:
        print("Current Mac Address is: ",get_current_mac(interface))
        exit()
