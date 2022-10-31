def get_line(i, n, char='*'):
    spaces_count = n - 1 - i
    stars_count = i + 1
    return ' ' * spaces_count + (f'{char} ' * stars_count)


def get_rhombus(n):
    return [get_line(i, n) for i in range(n)]+\
    [get_line(i, n) for i in range(n - 2, -1, -1)]


def print_rhombus(n):
    [print(row) for row in get_rhombus(n)]


print_rhombus(int(input()))
