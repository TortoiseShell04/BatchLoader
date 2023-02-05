import os

#Links!!! Leave no tabs or new lines between links only ","
Links = open("Links.txt","r")
LinksText = Links.read()
Links_Array = LinksText.split(",")

for link in Links_Array:
    print(link)

# Files names!!! Leave no tabs or new lines between names only ","
FileNames = open("Names.txt","r")
FileNamesText = FileNames.read()
FileNamesArray = FileNamesText.split(",")
for fileName in FileNamesArray:
    print(fileName)

Length = len(Links_Array)
EndCycle = Length
Length-=1
Index = int(open("Index.txt","r").read())

if Index <= Length:
    Index+=1
    open("Index.txt","w").write(f"{Index}")
    os.system(f"wget -O {FileNamesArray[Index-1]} {Links_Array[Index-1]}")
    if Index != EndCycle:
        os.system("python3 app.py")



print("Done")
