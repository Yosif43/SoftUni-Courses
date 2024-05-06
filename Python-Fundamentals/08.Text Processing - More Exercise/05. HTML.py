title = input()
content = input()
comments = []

while True:
    comment = input()
    if comment == "end of comments":
        break
    comments.append(comment)

print(f"<h1>\n    {title}\n</h1>")

print(f"<article>\n    {content}\n</article>")

for comment in comments:
    print(f"<div>\n    {comment}\n</div>")