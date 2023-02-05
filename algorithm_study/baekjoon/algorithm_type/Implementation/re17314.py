import sys
input = lambda:sys.stdin.readline().rstrip()


s = input() + ' '
ss = ''
chk = False

for i in range(len(s)):
    if i != (len(s)-1):
        if s[i+1] == '<':
            ss += s[i]
            print(ss[len(ss)-1::-1], end='')
            ss =  ''
            continue

    if s[i] == '<':
        print(s[i], end='')
        chk = True
    elif chk:
        print(s[i], end='')
        if s[i] == '>':
            chk = False
    else:
        ss += s[i]
        if s[i] == ' ':
            print(ss[len(ss)-2::-1], end=' ')
            ss = ''
'''

word = input() + ' '
temp = ''
i = 0
while i < len(word):
    if word[i] == ' ':
        print(temp[::-1], end=' ')
        temp = ''
    elif word[i] == '<':
        print(temp[::-1], end='')
        temp = ''

        next_tag = word.find('>', i)
        print(word[i:next_tag + 1], end='')
        i = next_tag
    else:
        temp += word[i]


    i += 1

'''