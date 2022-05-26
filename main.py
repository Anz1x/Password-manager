import os
import colorama
from colorama import Fore
from cryptography.fernet import Fernet

colorama.init(autoreset=True)

clear = lambda: os.system("cls" if os.name== "nt" else "clear")

def load_key():
    file = open("secret.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

# def generate_key():
#     key = Fernet.generate_key()
#     with open("secret.key", "wb") as thekey:
#         thekey.write(key)

def view_passwd():
    
    password_file = str(input(Fore.GREEN + "[+] " + Fore.LIGHTYELLOW_EX + "Path to Password File: " + Fore.GREEN))

    with open(password_file, "r") as thefile:
        print("\n")
        for line in thefile.readlines():
            creds = (line.rstrip())
            usr, pwd = creds.split(" :: ")
            print("Username: " ,usr, " | Password: ",
            fer.decrypt(pwd.encode()).decode())

    print("\n")

def add_passwd():

    pass_file = str(input(Fore.GREEN + "[+] " + Fore.LIGHTYELLOW_EX + "Path to Password File: " + Fore.GREEN))

    username = input(Fore.GREEN + "[+] " + Fore.LIGHTYELLOW_EX + "Username/account/email: " + Fore.GREEN)
    password = input(Fore.GREEN + "[+] " + Fore.LIGHTYELLOW_EX + "Password: " + Fore.GREEN)

    with open(pass_file , "a") as thefile:
        thefile.write(f"{username} :: {fer.encrypt(password.encode()).decode()}\n")
        
def create_passwd_file():

    pass_file = str(input(Fore.GREEN + "[+] " + Fore.LIGHTYELLOW_EX + "Name of the Password File: " + Fore.GREEN))
    file = open(pass_file, "w")
    file.close()

clear()

print(f"""
{Fore.LIGHTYELLOW_EX}     _____________
{Fore.LIGHTYELLOW_EX}    /      _      \\
{Fore.LIGHTYELLOW_EX}    [] :: (_) :: []
{Fore.LIGHTYELLOW_EX}    [] ::::::::: []  {Fore.GREEN}Password Manager
{Fore.LIGHTYELLOW_EX}    [] ::::::::: []  =================
{Fore.LIGHTYELLOW_EX}    [] ::::::::: []  {Fore.GREEN}[1] {Fore.LIGHTYELLOW_EX}View passwords    
{Fore.LIGHTYELLOW_EX}    [] ::::::::: []  {Fore.GREEN}[2] {Fore.LIGHTYELLOW_EX}Add new passwords
{Fore.LIGHTYELLOW_EX}    [_____________]  {Fore.GREEN}[3] {Fore.LIGHTYELLOW_EX}Create a new password file
{Fore.LIGHTYELLOW_EX}        I     I      {Fore.GREEN}[4] {Fore.LIGHTYELLOW_EX}Quit
{Fore.LIGHTYELLOW_EX}        I_   _I      
{Fore.LIGHTYELLOW_EX}         /   \\       {Fore.GREEN}[+] {Fore.LIGHTYELLOW_EX}Type 'help' to view the options
{Fore.LIGHTYELLOW_EX}         \   /       
{Fore.LIGHTYELLOW_EX}         (   )       {Fore.GREEN}[>] {Fore.LIGHTYELLOW_EX}Password Manager made by Anz
{Fore.LIGHTYELLOW_EX}         /   \\       {Fore.GREEN}[>] {Fore.LIGHTYELLOW_EX}Github: https://github.com/Anz1x
{Fore.LIGHTYELLOW_EX}         \___/
""")

while True:

    choice = str(input(Fore.LIGHTYELLOW_EX + "[>>>] " + Fore.GREEN))

    if choice == "1":
        view_passwd()
    elif choice == "2":
        add_passwd()
    elif choice == "3":
        create_passwd_file()
    elif choice == "4":
        clear()
        break
    elif choice == "help":
        print(f"""
{Fore.LIGHTYELLOW_EX}     _____________
{Fore.LIGHTYELLOW_EX}    /      _      \\
{Fore.LIGHTYELLOW_EX}    [] :: (_) :: []
{Fore.LIGHTYELLOW_EX}    [] ::::::::: []  {Fore.GREEN}Password Manager
{Fore.LIGHTYELLOW_EX}    [] ::::::::: []  =================
{Fore.LIGHTYELLOW_EX}    [] ::::::::: []  {Fore.GREEN}[1] {Fore.LIGHTYELLOW_EX}View passwords    
{Fore.LIGHTYELLOW_EX}    [] ::::::::: []  {Fore.GREEN}[2] {Fore.LIGHTYELLOW_EX}Add new passwords
{Fore.LIGHTYELLOW_EX}    [_____________]  {Fore.GREEN}[3] {Fore.LIGHTYELLOW_EX}Create a new password file
{Fore.LIGHTYELLOW_EX}        I     I      {Fore.GREEN}[4] {Fore.LIGHTYELLOW_EX}Quit
{Fore.LIGHTYELLOW_EX}        I_   _I      
{Fore.LIGHTYELLOW_EX}         /   \\       {Fore.GREEN}[+] {Fore.LIGHTYELLOW_EX}Type 'help' to view the options
{Fore.LIGHTYELLOW_EX}         \   /       
{Fore.LIGHTYELLOW_EX}         (   )       {Fore.GREEN}[>] {Fore.LIGHTYELLOW_EX}Password Manager made by Anz
{Fore.LIGHTYELLOW_EX}         /   \\       {Fore.GREEN}[>] {Fore.LIGHTYELLOW_EX}Github: https://github.com/Anz1x
{Fore.LIGHTYELLOW_EX}         \___/
""")

    elif choice == "clear":
        clear()
    elif choice == "ls":
        os.system("dir" if os.name== "nt" else "ls")
    else:
        print(Fore.GREEN + "[!] " + Fore.RED + "Invalid Input")
        continue
