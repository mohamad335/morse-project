morse_code_dict = {
    'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',    'E': '.',     
    'F': '..-.',   'G': '--.',    'H': '....',   'I': '..',     'J': '.---',  
    'K': '-.-',    'L': '.-..',   'M': '--',     'N': '-.',     'O': '---',   
    'P': '.--.',   'Q': '--.-',   'R': '.-.',    'S': '...',   'T': '-',     
    'U': '..-',    'V': '...-',  'W': '.--',    'X': '-..-',   'Y': '-.--',   
    'Z': '--..',   
    '1': '.----',  '2': '..---',  '3': '...--',  '4': '....-',  '5': '.....', 
    '6': '-....',  '7': '--...',  '8': '---..',  '9': '----.',  '0': '-----', 
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', 
    '/': '-..-.',  '(': '-.--.',  ')': '-.--.-', '&': '.-...',  ':': '---...', 
    ';': '-.-.-.', '+': '.-.-.',  '-': '-....-',  '=': '-...-',  '"': '.-..-.', 
    '$': '...-..-', '@': '.--.-.', ' ': '/'
    }

def morse_project():
    type=input("Encode or Decode? ").lower()
#encode the text to morse code
    def morse_code(text):
        for letter in text:
            if letter in morse_code_dict:
                print(morse_code_dict[letter], end=" ")
            else:
                print("Invalid character", end=" ")
#decode the morse code to the text
    def decode_morse(text):
        text=text.split(" ")
        for letter in text:
            for key, value in morse_code_dict.items():
                if letter == value:
                    print(key.lower(), end="")
#check if the user choose encode or decode and if he want to continue
    if type=="encode":
        text = input("Enter Text: ").upper()
        morse_code(text)

    elif type == "decode":
        text = input("Enter Morse Code: ")
        decode_morse(text)  
    else:
        print("Invalid input!")
    again=input("\nDo you want to continue? Y/N: ").lower()
    if again=="y":
        morse_project()
    else:
        print("Goodbye!")   
morse_project()
