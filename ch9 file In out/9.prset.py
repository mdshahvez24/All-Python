#Repeat a program to for a  list of such word to be censored

words = ["very", "is", "and"]

with open("sample.text") as f:
    content = f.read()

    for word in words:
        content = content.replace(word, "####")

        with open("sample.text", "w") as f:
            f.write(content)