def val(s):
    value = 0
    for letter in s:
        value += ord(letter) - 64
    return value
names = open('p022_names.txt').read().replace('"', '').split(',')
names.sort()

total = 0
for name in names:
    total += val(name)*int(names.index(name) + 1)
print(total)
        
