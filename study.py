
message = input(">")
words = message.split()
emojis = {
    ":)":"🙂",
    ":(":"☹️",
    ":|":"😐",
    "B)":"😎",
    "<3":"💖"
}
[print(emojis.get(word,word), end = " ") for word in words]
