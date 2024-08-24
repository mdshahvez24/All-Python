#  n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     marks=student_marks[query_name]
#     print(format(sum(marks)/3,'.2f'))

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
arr = student_marks[query_name]
sum = 0
for i in arr:
    sum+=i
res = sum/len(arr)
print("%.2f"%res)



# marks=student_marks[query_name]
# print(format(sum(marks)/3,'.2f'))


