title = input()
content = input()
comments = []

print(f"""<h1>
    {title}
</h1>""")

print(f"""<article>
    {content}
</article>""")

while True:
    comment = input()
    if comment == "end of comments":
        break
    print(f"""<div>
    {comment}
</div>""")