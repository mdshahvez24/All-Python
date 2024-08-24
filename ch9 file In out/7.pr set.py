#  wap to print 1-20 table in a folder

for i in range(2, 21):
    with open(f"table/Multiplication_table_of_{i}this.text", 'w') as f:

        for j in range(1, 11):
            f.write(f"{i}X{j}={i*j}")
            if j!=10:
                f.write('\n')
