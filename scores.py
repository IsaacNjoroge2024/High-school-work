import pickle

first_name = input("Please enter your name:")
score = input("Please enter your score:")

scores = []
high_scores = first_name, score
scores.append(high_scores)

file = open("high_scores.dat", "ab")
pickle.dump(scores, file)
file.close()

file = open("high_scores.dat", "rb")
scores = pickle.load(file)
print(scores)
file.close()