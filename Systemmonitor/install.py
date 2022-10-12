#import the required modules
import sys
import subprocess

#ask which moduke to install
print("Which module do you want to install?")
#get the input
module = input("Module: ")

#instll the module
subprocess.call([sys.executable, "-m", "pip", "install", module])

# check if the user wants to install another module
while True:
    # ask the user if he wants to install another module
    install_another_module = input("Do you want to install another module? (y/n): ")
    # if the user wants to install another module
    if install_another_module == "y":
        # ask the user which module he wants to install
        module_to_install = input("Which module do you want to install? (name): ")
        # install the module
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', module_to_install])
    # if the user doesn't want to install another module
    elif install_another_module == "n":
        # exit the program
        sys.exit()
    # if the user enters something else
    else:
        # ask the user again to enter a valid input
        continue

# exit the program
sys.exit()