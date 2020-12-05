N = int(input())

group_check = 0

for _ in range(N):
    word = input()
    check = 0
    for i in range(len(word)-1):  # 0부터 단어글자수-1까지 
        if word[i] != word[i+1]:  # i번째와 i+1번째 문자가 다르면
            check_w = word[i+1:]  # i+1번째~마지막까지의 문자로 새로운 단어 check_w 생성
            if check_w.count(word[i]) > 0:  # check_w 에서 i번째 문자가 있으면
                check += 1  # check 1 증가
    if check == 0:  # check가 0이면
        group_check += 1 #group_check 1 증가

print(group_check) # group_word의 수 출력
