with open('another.text', 'r') as f:
    a = f.read()
    with open('another.text', 'w') as f:
        a = f.write("me")
        print(a)
