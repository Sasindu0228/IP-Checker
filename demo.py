
import os
def main():
    def Number_Check(str):
        i = 0
        num = 0
        n = 0
        arr = [0] * 5
        num_valid = 1
        while i < len(str):
            num = 0
            while i < len(str) and str[i] != '.':
                num = num * 10 + int(str[i]) - int('0')
                i += 1
            if num >= 0 and num <= 255:
                arr[n] = 1
            else:
                arr[n] = 0
            n += 1
            i += 1
        for i in range(4):
            num_valid = num_valid and arr[i]
        return num_valid

    def Length_Check(str):
        length = len(str)
        if length >= 7 and length <= 15:
            return 1
        else:
            return 0

    def Dots_Check(str):
        dot_valid = 0
        for i in range(len(str)):
            if str[i] == '.':
                dot_valid += 1
        if dot_valid == 3:
            return 1
        else:
            return 0

    def String_Check(str):
        str_valid = 1
        for i in range(len(str)):
            if (str[i] >= '0' and str[i] <= '9') or str[i] == '.':
                str_valid = str_valid and 1
            else:
                str_valid = str_valid and 0
        return str_valid

    def Check_IP(str):
        str_valid = String_Check(str)
        dot_valid = Dots_Check(str)
        len_valid = Length_Check(str)
        num_valid = Number_Check(str)
        if not len_valid:
            print("\n-> Length of the IPv4 address is from 7 to 15 Characters.")
        if not dot_valid:
            print("\n-> IPv4 address can contain only 3 Dots.")
        if not str_valid:
            print("\n-> IPv4 address can contain only Digits and Dots.")
        if not num_valid:
            print("\n-> IPv4 address in Form of a.b.c.d \n\t\twhere a, b, c and d are integer values ranging from 0 to 255 inclusive.")
        if len_valid and dot_valid and str_valid and num_valid:
            return 1
        else:
            return 0

    address = input("Enter IP Number: ")
    print("Entered IP Address : " + address + "\n")
    if Check_IP(address):
        print("\n\n✔ Valid IP Address.")
    else:
        print("\n\n❌ Invalid IP Address.")
    return address

def main_ip_online():
    def Number_Check(str):
        i = 0
        num = 0
        n = 0
        arr = [0] * 5
        num_valid = 1
        while i < len(str):
            num = 0
            while i < len(str) and str[i] != '.':
                num = num * 10 + int(str[i]) - int('0')
                i += 1
            if num >= 0 and num <= 255:
                arr[n] = 1
            else:
                arr[n] = 0
            n += 1
            i += 1
        for i in range(4):
            num_valid = num_valid and arr[i]
        return num_valid

    def Length_Check(str):
        length = len(str)
        if length >= 7 and length <= 15:
            return 1
        else:
            return 0

    def Dots_Check(str):
        dot_valid = 0
        for i in range(len(str)):
            if str[i] == '.':
                dot_valid += 1
        if dot_valid == 3:
            return 1
        else:
            return 0

    def String_Check(str):
        str_valid = 1
        for i in range(len(str)):
            if (str[i] >= '0' and str[i] <= '9') or str[i] == '.':
                str_valid = str_valid and 1
            else:
                str_valid = str_valid and 0
        return str_valid

    def Check_IP(str):
        str_valid = String_Check(str)
        dot_valid = Dots_Check(str)
        len_valid = Length_Check(str)
        num_valid = Number_Check(str)
        if not len_valid:
            print("\n-> Length of the IPv4 address is from 7 to 15 Characters.")
        if not dot_valid:
            print("\n-> IPv4 address can contain only 3 Dots.")
        if not str_valid:
            print("\n-> IPv4 address can contain only Digits and Dots.")
        if not num_valid:
            print("\n-> IPv4 address in Form of a.b.c.d \n\t\twhere a, b, c and d are integer values ranging from 0 to 255 inclusive.")
        if len_valid and dot_valid and str_valid and num_valid:
            return 1
        else:
            return 0

    address = input("Enter IP Number: ")
    print("Entered IP Address : " + address + "\n")
    if Check_IP(address):
        print("\n\n✔ Valid IP Address.")
    else:
        print("\n\n❌ Invalid IP Address.")

    os.system("ping -c 10"+" "+address)
    
def banner():
    print("")
    print("\033[1;34m██╗██████╗       \033[1;33m █████╗ ██╗  ██╗███████╗ █████╗ ██╗  ██╗███████╗██████╗ ")
    print("\033[1;34m██║██╔══██╗      \033[1;33m██╔══██╗██║  ██║██╔════╝██╔══██╗██║ ██╔╝██╔════╝██╔══██╗")
    print("\033[1;34m██║██████╔╝█████╗\033[1;33m██║  ╚═╝███████║█████╗  ██║  ╚═╝█████═╝ █████╗  ██████╔╝")
    print("\033[1;34m██║██╔═══╝ ╚════╝\033[1;33m██║  ██╗██╔══██║██╔══╝  ██║  ██╗██╔═██╗ ██╔══╝  ██╔══██╗")
    print("\033[1;34m██║██║           \033[1;33m╚█████╔╝██║  ██║███████╗╚█████╔╝██║ ╚██╗███████╗██║  ██║")
    print("\033[1;34m╚═╝╚═╝           \033[1;33m ╚════╝ ╚═╝  ╚═╝╚══════╝ ╚════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝")
    print("\033[1;34m                                          Tool By - Sasindu Rashmika    ")
    print("")
    bar = "\n__________________________________________________________________________________\n"
    print(bar)
    print("\033[1;33m      [1] START                    [2] START WITH IP_ONLINER")
    print("\033[1;33m      [3] Update Tool              [4] Help Video")
    print("\033[1;33m      [5] Exit  ")
    print("")
    ch = int(input("\033[1;31m[*] \033[1;33mEnter Your Choice : >>> "))
    print("")

    if ch == 1:
        main()
    elif ch == 2:
        main_ip_online()
    elif ch == 3:
        pass
    elif ch == 4:
        print("Comming Soon...")
    elif ch == 5:
        exit
    else:
        print("Invalid Number!")
          
banner()



