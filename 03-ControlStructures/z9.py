tasks = int(input("Enter number of tasks:"))
correct = int(input("Enter number of correct tasks: "))
if correct >= (tasks/2):
    print(f" Tasks: {tasks} \n Correct: {correct} \n Passed!")
else:
    print(f" Tasks: {tasks} \n Correct: {correct} \n Unpassed")