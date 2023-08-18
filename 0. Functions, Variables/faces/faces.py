emoji = {
    ":)": "🙂",
    ":(": "🙁"
}
message = input("")
words = message.split(' ')
new_text = ""
for word in words:
    new_text += emoji.get(word, word) + " "
print(new_text)
