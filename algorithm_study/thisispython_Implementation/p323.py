def solution(s):
    answer = len(s)
    d = 1
    while d != len(s) // 2 + 1:
        temp = s[0:d]
        ss = ""
        num = 1
        for i in range(d, len(s), d):
            if temp == s[i:i+d]:
                num += 1
            else:
                if num >= 2:
                    ss += str(num) + temp
                else:
                    ss += temp
                temp = s[i:i+d]
                num = 1

        if num >= 2:
            ss += str(num) + temp
        else:
            ss += temp

        answer = min(len(ss), answer)
        
        d += 1
                
    return answer