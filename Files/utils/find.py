def find(lines, expected):
    for line in lines:
        print(f"hi... finding {line}")
    raise NotFoundError(f'{expected} not found')

class NotFoundError(Exception):
    pass