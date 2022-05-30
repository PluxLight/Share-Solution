NUM_DIVIDE = 10007

def calc_num(a_num, b_num):
    a_num = list(map(str, a_num.split('+')))
    a = int(a_num[0])
    b = int(a_num[1][:-1])

    b_num = list(map(str, b_num.split('+')))
    c = int(b_num[0])
    d = int(b_num[1][:-1])

    # 두 입력값의 정수 부분을 추출한 후

    result = f'{a * c - b * d}+{a*d + b*c}i' # 문제에 있는 식으로 계산 후 값을 반환

    return result

def solution():
    n = int(input())
    num_list = list(map(str, input().split()))
    answer = num_list[0] # 첫번째 입력값을 저장

    for i in range(1, n): # 입력값이 2개 이상인 경우 순차적으로 계산
        answer = calc_num(answer, num_list[i])

    a, b = map(str, answer.split('+'))
    a = int(a)
    b = int(b[:-1]) # 최종적으로 계산한 값을 + 를 기준으로 분할 후

    if a < 0:
        a = abs(a) % NUM_DIVIDE
        a = -a
    else:
        a = a % NUM_DIVIDE

    if b < 0:
        b = abs(b) % NUM_DIVIDE
        b = -b
    else:
        b = b % NUM_DIVIDE

    # a, b 모두 10007로 나머지 연산을 수행
    # 단 음수인 경우 절대값으로 치환 후 나머지 연산하고 다시 음수 적용

    answer = f'{a}+{b}i'


    return answer


if __name__ == "__main__":
    print(solution())



"""
2
-1+-3i 2+-1i 
"""

"""
-5+-5i
"""