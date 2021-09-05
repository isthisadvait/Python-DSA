#replace Pi with 3.14  By -Raman Mehta
def replacePi(s):
    if len(s)==0 or len(s)==1:
        return s
    if s[0]=='p' and s[1]=='i':
        small=replacePi(s[2:])
        return '3.14'+small
    else:
        small=replacePi(s[1:])
        return s[0]+small
print(replacePi('abcppide'))
