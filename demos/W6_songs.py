#Open file for reading
f = open("file/song.txt")
#print(f.readline(), end="")
#print(f.readline(), end="")
#Print full content of the file
#print(f.read())
#Grab conent of txt file and save it as a list
lista = f.readlines()
print(lista)
print(lista[2])
f.close()  #Close file to make it availeble again
g = open("files/song.txt", "a")
#Write a single line into the end os the file
g.write.lines("\nAnd it's everlasting, infinite\n")
#Write multiple lines into a file
g.write.lines(["It goes on and on, you can't measure it", "Can't quench your love"])
g.close()
