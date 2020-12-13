from os import system
import base64
from colorama import Fore

# encode
def encode(data):
    try:
        encodedbyte = base64.b64encode(data.encode("utf-8"))
        print(Fore.GREEN + "Encoded Successfully :) \n " + "Data : " + data + "\n Encoded version : " + str(encodedbyte,"utf-8")  +"\n" + Fore.RESET)
    except Exception as e:
        print(Fore.RED + "Encoded Failed :( \n Error :" + e + Fore.RESET)

# decode
def decode(data):
    try:
        decodedbyte = base64.b64decode(data)
        print(Fore.GREEN + "Decode Successfully :) \n " + "Data : " + data + "\n Decoded version : " + str(decodedbyte,"utf-8")  +"\n" + Fore.RESET)
    except Exception as e:
        print(Fore.RED + "Decode Failed :( \n Error :" + e + Fore.RESET)

#Switch for validate



# Start a Software  
if __name__ == "__main__":
    system("cls")
    print(Fore.YELLOW + """
            
 _____            _____                                 _ 
|  __ \          / ____|                               | |
| |  | |  ___   | (___    ___   ___  _   _  _ __  ___  | |
| |  | | / _ \   \___ \  / _ \ / __|| | | || '__|/ _ \ | |
| |__| || (_) |  ____) ||  __/| (__ | |_| || |  |  __/ |_|
|_____/  \___/  |_____/  \___| \___| \__,_||_|   \___| (_)

        Coded By @javadimoghadam & @FarhoodGH
                                                          
                                                          
    """ + Fore.WHITE)


while True:
    d = (input(Fore.WHITE + "Please enter your Method( [D]ecode ,  [E]ncode , [e]xit ): " +Fore.RESET))

    if d is "e": 
        exit()
    if d is "D":
        Dcode = (input(Fore.BLUE  +  "Please enter your code: "  + Fore.RESET))
        decode(Dcode)
    if d is "E":
        Ecode = (input(Fore.BLUE + "Please enter your text:  " + Fore.RESET))
        encode(Ecode)
