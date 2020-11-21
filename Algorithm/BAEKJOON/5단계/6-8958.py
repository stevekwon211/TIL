num_case = int(input())
score = 0
count = 0
score_list = []

for i in range(num_case):
    case_list = input()
    for j in range(len(case_list)):
        if case_list[j] == 'O':
            count += 1
            score += count
        elif case_list[j] == 'X':
            score += 0
            count = 0
    score_list.append(score)
    score = 0
    count = 0

for i in range(num_case):
    print(score_list[i])

