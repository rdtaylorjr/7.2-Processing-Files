# Use words.txt as the file name
count = 0
total = 0
fname = input("Enter file name: ")
fhand = open(fname)
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count = count + 1
    zero = line.find('0')
    num = line[zero:]
    flo = float(num)
    total = total + flo
    avg = total/count

print('Average spam confidence:',avg)    
