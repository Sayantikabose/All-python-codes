with open("file1.txt") as f1:
    new1=(f1.readlines())



with open("file2.txt") as f2:
     new2 =(f2.readlines())


new=[int(n) for n in new1 if n in new2]
print(new)

