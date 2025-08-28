def DecodeMorse():
    Syntax = {
        "/" : " ",
        ".-" : "a",
        "-..." : "b",
        "-.-." : "c",
        "-.." : "d",
        "." : "e",
        "..-." : "f",
        "--." : "g",
        "...." : "h",
        ".." : "i",
        ".---" : "j",
        "-.-" : "k",
        ".-.." : "l",
        "--" : "m",
        "-." : "n",
        "---" : "o",
        ".--." : "p",
        "--.-" : "q",
        ".-." : "r",
        "..." : "s",
        "-" : "t",
        "..-" : "u",
        "...-" : "v",
        ".--" : "w",
        "-..-" : "x",
        "-.--" : "y",
        "--.." : "z",
        "-----" : "0",
        ".----" : "1",
        "..---" : "2",
        "...--" : "3",
        "....-" : "4",
        "....." : "5",
        "-...." : "6",
        "--..." : "7",
        "---.." : "8",
        "----." : "9"
    }

    try:
        EncodedMessage = input("Enter the encoded message : ") + " "
        decodedMessage = ""
        MessageToDecode = ""

        for i in range (0, len(EncodedMessage)):
            if EncodedMessage[i] != " " and EncodedMessage != "/":
                MessageToDecode += EncodedMessage[i]
            
            else:
                decodedMessage += Syntax.get(MessageToDecode)
                MessageToDecode = ""

        print(f"decoded message : {decodedMessage.capitalize()}")

    except KeyError():
        print("Wrong morse code syntax.")

def EncodeMorse():
    Syntax = {
        " " : "/",
        "a" : ".-",
        "b" : "-...",
        "c" : "-.-.",
        "d" : "-..",
        "e" : ".",
        "f" : "..-.",
        "g" : "--.",
        "h" : "....",
        "i" : "..",
        "j" : ".---",
        "k" : "-.-",
        "l" : ".-..",
        "m" : "--",
        "n" : "-.",
        "o" : "---",
        "p" : ".--.",
        "q" : "--.-",
        "r" : ".-.",
        "s" : "...",
        "t" : "-",
        "u" : "..-",
        "v" : "...-",
        "w" : ".--",
        "x" : "-..-",
        "y" : "-.--",
        "z" : "--..",
        "0" : "-----",
        "1" : ".----",
        "2" : "..---",
        "3" : "...--",
        "4" : "....-",
        "5" : ".....",
        "6" : "-....",
        "7" : "--...",
        "8" : "---..",
        "9" : "----." 
    }

    MessageToEncode = input("Enter the Message to encode : ").lower()
    EncodedMesage = ""

    for i in range(0, len(MessageToEncode)):
        EncodedMesage += Syntax.get(MessageToEncode[i]) + " "

    print(f"Encoded message : {EncodedMesage.strip()}")

def main():
    
    try:
        EncOrDec = int(input("Press 1 for encoding and press 2 to for decoding : "))

        if EncOrDec == 1:
            EncodeMorse()
        
        elif EncOrDec == 2:
            DecodeMorse()

        else:
            print("Wrong input !")
    
    except TypeError:
        print("Enter The correct value !!")
    
    except Exception:
        print("Something went wrong !")

if __name__ == "__main__":
    main()