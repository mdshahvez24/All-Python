# with open("sample.text") as f:
#     content = f.read()

#     if 'python' in content.lower():  # must be in lower case
#         print("yes Python is present")
#     else:
#         print("Python is not present")


content = True
i = 1
with open("sample.text") as f:
    while content:
        content = f.readline()
        if 'python' in content.lower():
            print(content)
            print(f"Yes python is present on line number {i}")
        i+=1