def DecodeMorse(EncodedMessage):
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

def EncodeMorse(MessageToEncode):
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

    EncodedMesage = ""

    for i in range(0, len(MessageToEncode)):
        EncodedMesage += Syntax.get(MessageToEncode[i]) + " "

    print(f"Encoded message : {EncodedMesage.strip()}")

def main():
    
    try:
        EncOrDec = input("Enter the message (Encoded or Decoded): ")

        if EncOrDec[0] == "." or EncOrDec[0] == "-" or EncOrDec[0] == "/":
            DecodeMorse(EncOrDec + " ")

        else:
            EncodeMorse(EncOrDec.lower())
    
    except Exception:
        print("Something went wrong !")

if __name__ == "__main__":
    main()