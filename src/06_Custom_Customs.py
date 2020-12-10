groups = open("input").read().split("\n\n")

count1, count2 = (0,0)

for group in groups:
    questions = set([person for person in group.replace("\n","")])
    count1 += len(questions)

for group in groups:
    list_questions = [set(person) for person in group.split("\n")]
    count2 += len(set.intersection(*list_questions))

print("First puzzle:", count1)
print("Second puzzle:", count2)

