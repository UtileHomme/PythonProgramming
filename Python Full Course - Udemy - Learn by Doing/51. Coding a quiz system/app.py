questions = open('questions.txt', 'r')

questions_list = [line.strip() for line in questions]
questions.close()

score = 0

total = len(questions_list)

for line in questions_list:
    q,a = line.split("=")

    ans = input(f"{q} = ")

    if a==ans:
        score += 1

result = open('result.txt', 'w')
result.write(f"Your final score is {score/total}")
result.close()