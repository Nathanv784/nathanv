f1=open("data.txt","w+")

f1.write("this is Nathan V")
print(f1.tell())
f1.seek(10,0)
print(f1.read())
f1.write("\ndeleteddd")
print(f1.tell())