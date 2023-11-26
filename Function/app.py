# def greet_user(first_name, last_name):
#     print(f"Hi {first_name} {last_name}!")
#     print("Welcome aboard")


# print("start")
# greet_user("John", "Smith")
# print("finish")

# def square(number):
#     return number * number


# result = square(3)
# print(result)

def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "😒"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

msg = input("> ")
print(emoji_converter(msg))

