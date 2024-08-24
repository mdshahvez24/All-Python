#  wap to make a copy of a text file 

with open("this.text") as f:
    content = f.read()

    with open("copy.text", "w") as f:
        f.write(content)
