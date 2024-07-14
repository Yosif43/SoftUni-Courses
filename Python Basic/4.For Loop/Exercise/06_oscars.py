actor_name = input()
scores_academy = float(input())
n = int(input())

requred_scores = False
threshold = 1250.5
for i in range(n):
    name = input()
    scores = float(input())
    scores_academy = scores_academy + ((len(name) * scores) / 2)

    if scores_academy > threshold:
        requred_scores = True
        break
    else:
        requred_scores = False

if requred_scores:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {scores_academy:.1f}!")
else:
    print(f"Sorry, {actor_name} you need {threshold - scores_academy:.1f} more!")
