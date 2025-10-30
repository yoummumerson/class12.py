"""file = open('codingal.txt','a')
file.write("I am Reyaansh and i love to play valorant and eat ramen")"""

file1 = open('codingal.txt','r')

file2 = open('codingalUpdated.txt','w')

for line in file1.readlines():
    if not (line.startswith('coding')):
        print(line)
        file2.write(line)

file2.close()
file1.close()