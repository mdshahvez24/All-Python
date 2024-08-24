# A file continue a word "donkey multiple" times you need to write a program which replace this word with #### by updating the same file.

with open ("sample.text") as f:
    content = f.read()

    content = content.replace("donkey", "####")

    with open("sample.text", "w") as f:
        f.write(content)