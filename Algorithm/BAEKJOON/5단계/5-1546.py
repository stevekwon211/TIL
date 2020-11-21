sub_num = int(input())
sub_score = list(map(int, input().split()))
max_score = max(sub_score)
new_score = []

for i in range(0, sub_num):
    a = (sub_score[i]/max_score)*100
    new_score.append(a)

print(sum(new_score)/len(new_score))
