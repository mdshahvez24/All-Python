sub1 = int(input("marks of first sub: "))
sub2 = int(input("marks of second sub: "))
sub3 = int(input("marks of  third sub: "))

if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail less then 33 percent")

elif(sub1+sub2+sub3)/3 <40:
    print("youare fail due to less percentage 40")
else:
    print("you are passed")