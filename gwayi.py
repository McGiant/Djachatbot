import os
# Open the file with write permit
f = open('/home/lawrence/Documents/gwayi.txt')
rem_domain = []
for line in f.readlines():
    x = f.readline()
    y = os.system('dig MX {}'.format(line))
    zebb = os.popen('dig MX {}'.format(line)).read()
    if 'yoafrica' not in zebb:
        rem_domain.append(line)

    print(line)
    print(rem_domain)



f.close()
