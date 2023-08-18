cases = input("camelCase: ")


def camel2snake(camel):
    snake = []
    for char in camel[:]:
        if char.isupper():
            snake.append('_')
        snake.append(char.lower())
    return ''.join(snake)

print("snake_case:", camel2snake(cases))
