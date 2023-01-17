def loopWhile():
    x = 0
    nums = []
    while x < 5:
        nums.append(x)
        x += 1
    print(f"Loop while x < 5: {nums}")
    
def loopForRange():
    nums = []
    for i in range(5,10):
        nums.append(i)
    print(f"Loop for i in range (5,10): {nums}")
    

def loopForArray():
    dias = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
    for i in dias:
        print(i)
    
def loopEnumerate():
    dias = ["seg", "ter", "qua", "qui", "sex", "sab", "dom"]
    for i, d in enumerate(dias):
        print(i, d)
    
if __name__ == '__main__':
    loopWhile()
    loopForRange()
    loopForArray()
    loopEnumerate()