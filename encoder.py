# @Author : Farhood Ghanbari (@FarhoodGH) & Ali Javadi (@javadimoghadam)
# @Version : 1.0.1 Released 
# @License : MIT


from os import system
import base64
from colorama import Fore
#custom encode
def rot13(phrase):
   abc = "abcdefghijklmnopqrstuvwxyz"
   out_phrase = ""
   for char in phrase:
       out_phrase += abc[(abc.find(char)+13)%26]
   return out_phrase

# encode
def encode(data:str,originaldata:str):
    data.lower()
    try:
        encodedbyte = base64.b64encode(data.encode("utf-8"))
        print(Fore.GREEN + "Encoded Successfully :) \n " + "Data : " + originaldata + "\n Encoded version : " + str(encodedbyte,"utf-8")  +"\n" + Fore.RESET)
    except Exception as e:
        print(Fore.RED + "Encoded Failed :( \n Error :" + e + Fore.RESET)
        
# decode
def decode(data:str):
    try:
        decodedbyte = base64.b64decode(data)
        print(Fore.GREEN + "Decode Successfully :) \n " + "Data : " + data + "\n Decoded version : " + rot13(str(decodedbyte,"utf-8")).replace("z"," ")  +"\n" + Fore.RESET)
    except Exception as e:
        print(Fore.RED + "Decode Failed :( \n Error :" + e + Fore.RESET)

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
    d = (input(Fore.WHITE + "Please enter your Method( [D]ecode ,  [E]ncode , [e]xit ) -> " +Fore.RESET))
    if d is "e": 
        system("cls")
        print(Fore.GREEN + "Exit Successfully ! " + Fore.RESET)
        exit()
    elif d is "D":
        Dcode = (input(Fore.BLUE  +  "Please enter your code -> "  + Fore.RESET))
        decode(Dcode)
        
    elif d is "E":
        Ecode = (input(Fore.BLUE + "Please enter your text -> " + Fore.RESET))
        custom = rot13(Ecode)
        encode(custom,Ecode)
    else:
        print(Fore.RED + "Wrong argument !" +Fore.RESET) 