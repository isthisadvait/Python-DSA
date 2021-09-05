# Problem: Remove x from string
def helper(string):
    if len(string)==0:
        return ""
    small=helper(string[1:])
    if string[0]!='x':
        small=string[0]+small
    return small
    

def removeX(string): 
     return helper(string)
    

# Main
string = input()
print(removeX(string))
