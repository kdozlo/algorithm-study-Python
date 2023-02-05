import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())

fnum = 0
tnum = 0

if n % 5 == 0:
    fnum = n // 5
    print(fnum)
elif n == 4 or n == 7:
    print(-1)
elif n % 5 == 1:
    tnum = 2
    n -= tnum*3
    fnum = n //5
    print(tnum+fnum)
elif n % 5 == 2:
    tnum = 4
    n -= tnum*3
    fnum = n //5
    print(tnum+fnum)
elif n % 5 == 3:
    tnum = 1
    n -= tnum*3
    fnum = n //5
    print(tnum+fnum)
elif n % 5 == 4:
    tnum = 3
    n -= tnum*3
    fnum = n //5
    print(tnum+fnum)
else:
    print(-1)


'''
#훨씬 좋은 코드

kg = int(input())              # 총 설탕 킬로그램 입력받기

cnt = 0                        # 3 빼줄 횟수 셀 변수선언 (즉, 3킬로 봉지량) 

while kg >= 0:                 # kg가 0보다 클때 동안만 도는 반복문
	if kg % 5 == 0:            # 만약 5의 배수면 바로 출력!!!
		print(kg // 5 + cnt)   # 5로 나눈 몫과 3킬로 봉지수 출력
		break                  # else문 안걸리게 탈출
	kg = kg - 3                # 3킬로 빼줘라
	cnt += 1                   # 빼준 횟수 하나씩 증가
else:
	print(-1)                  # 다 돌았는데도 없음 -1 !!


'''