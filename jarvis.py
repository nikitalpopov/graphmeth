def rotate(a, b, c):

    # Вспомогательная функция для определения положения точки 'c'
    # относительно вектора 'ab'.
    # Возвращает положительное значение, если точка лежит слева,
    # отрицательное – справа

    return (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])


def jarvis(a, counts):

    # Функция, реализующая метод Джарвиса
    # построения минимальной выпусклой оболочки (мво)
    # На вход подается:
    # a - матрица координат точек множества
    # counts - количество точек
    # На выходе получаем
    # h - последовательность обхода точек для построения мво

    n = len(a)
    p = list(range(counts))
    # start point
    for i in range(1, n):
        if a[p[i]][0] < a[p[0]][0]:
            p[i], p[0] = p[0], p[i]
    h = [p[0]]
    del p[0]
    p.append(h[0])
    while True:
        right = 0
        for i in range(1, len(p)):
            if rotate(a[h[-1]], a[p[right]], a[p[i]]) < 0:
                right = i
        if p[right] == h[0]:
            break
        else:
            h.append(p[right])
            del p[right]

    return h
