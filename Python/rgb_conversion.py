def dec2hex(hexnum):
    hexstring = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    counter = 0
    remainder = []
    answer = ""
    if hexnum>255:
        answer = "FF"
    elif hexnum==1:
        while hexnum > 0:
            remainder.append(hexnum % 16)
            hexnum = hexnum // 16
            counter = counter + 1
        for reverse in remainder[::-1]:
            print(reverse)
            answer =answer + "0"+hexstring[reverse]
    elif 1<hexnum<9:
        while hexnum > 0:
            remainder.append(hexnum % 16)
            hexnum = hexnum // 16
            counter = counter + 1
        for reverse in remainder[::-1]:
            print(reverse)
            answer =answer + "0"+hexstring[reverse]
    elif hexnum > 0:
        while hexnum > 0:
            remainder.append(hexnum % 16)
            hexnum = hexnum // 16
            counter = counter + 1
        for reverse in remainder[::-1]:
            answer = answer + hexstring[reverse]
    else:
        answer = "00"
    return answer
def rgb(r, g, b):
    if r <10 and g<10 and b<10 :
        return (dec2hex(r)+dec2hex(g)+dec2hex(b))
        
    else:
        return(dec2hex(r)+dec2hex(g)+dec2hex(b)).upper()