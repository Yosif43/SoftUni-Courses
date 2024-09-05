def kwargs_length(**kwargs):

    return len(kwargs)


dictionary = {}
print(kwargs_length(**dictionary))

dictionary = {'name': 'Peter', 'age': 25}
print(kwargs_length(**dictionary))
