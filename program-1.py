def sentence_maker(phrase):
    captial = phrase.capitalize()
    if phrase.startswith(("how","what","why" )):
        return f"{captial}?"
    else:
        return f"{captial}."

results = []
while True:
    user_input = input("Enter something : ")
    if user_input == "\stop" :
        break
    else:
        results.append(sentence_maker(user_input))


print(" ".join(results))


