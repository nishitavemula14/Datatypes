s = open('demo.txt', mode = 'r')
print(s.read())
s.close

#write
s = open('demo.txt',mode ='a')
s.write("bye bye write ")
s.close()

#r+
s = open('demo.txt', mode = 'r+')
print(s.read())
s.write("r+ mode")
s.seek(0)
s.close

#w+
s = open('demo.txt', mode = 'w+')
s.write("w+ mode")
print(s.read())
s.seek(2)
s.close

