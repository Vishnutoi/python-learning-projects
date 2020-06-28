#Make a morse code translator
#Test your knowledge of dictionaries with a dictionary that compares
# {"letter":"more_code"}. Then loop through an inputted string and convert it into morse

def to_morse(text):
    eng_to_morse = {
    'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..', 'e' : '.', 'f' : '..-.', 'g' : '--.', 'h' : '....', 'i' : '..', 'j' : '.---', 'k' : '-.-', 'l' : '.-..', 'm' : '--', 'n' : '-.', 'o' : '---', 'p' : '.--.', 'q' : '--.-', 'r' : '.-.', 's' : '...', 't' : '-', 'u' : '..-', 'v' : '...-', 'w' : '.--', 'x' : '-..-', 'y' : '-.--', 'z' : '--..', '.' : '.-.-.-', '?' : '..--..', ',' : '--..--', ' ' : '/'}

    morse_code = ""

    for x in text:
        morse_code += eng_to_morse[x.lower()]
        return morse_code

text = input("please input : ")

print(to_morse(text))