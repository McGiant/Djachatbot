import os
# Open the file with write permit
f = open('/home/lawrence/Documents/gwayi.txt')

for line in f.readlines():
    x = f.readline()
    y = os.system('dig MX {}'.format(line))
    print(line)

f.close()
