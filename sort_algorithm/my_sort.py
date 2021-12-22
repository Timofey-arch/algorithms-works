import pygame


def insertion_sort(array, key, visualization):
    for x in range(1, len(array)):
        for i in range(x, 0, -1):
            if cmp(key(array[i]), key(array[i - 1])) == 1:
                array[i - 1], array[i] = array[i], array[i - 1]
                if visualization:
                    visualize(array)
            else:
                if visualization:
                    visualize(array)
                break
    return array


def merge_sort(a_array, b_array, key):
    a = 0
    b = 0
    c_array = []
    while a < len(a_array) and b < len(b_array):
        if cmp(key(a_array[a]), key(b_array[b])) == 1:
            c_array.append(a_array[a])
            a += 1
        elif cmp(key(a_array[a]), key(b_array[b])) == 0:
            c_array.append(b_array[b])
            b += 1
        else:
            c_array.append(a_array[a]), c_array.append(b_array[b])
            a, b = a + 1, b + 1
    while a < len(a_array):
        c_array.append(a_array[a])
        a = a + 1
    while b < len(b_array):
        c_array.append(b_array[b])
        b = b + 1
    return c_array


def tim_sort(array, run, key, visualization):
    for x in range(0, len(array), run):
        array[x: x + run] = insertion_sort(array[x: x + run], key, visualization)
        if visualization:
            visualize(array)
    run_inc = run
    while run_inc < len(array):
        for x in range(0, len(array), 2 * run_inc):
            array[x: x + 2 * run_inc] = merge_sort(array[x: x + run_inc],
                                                   array[x + run_inc: x + 2 * run_inc], key)
        if visualization:
            visualize(array)
        run_inc = run_inc * 2


def cmp(x, y):
    if x > y:
        return 0
    if x < y:
        return 1
    if x == y:
        return 2


def visualize(array, final=False):
    pygame.init()
    pygame.time.delay(500)
    window_height = 400
    window_width = 600
    win = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Timsort")
    margin_bottom = window_height * 0.1
    width = window_width // ((len(array) + 1) * 2)
    pygame.font.init(), win.fill((0, 0, 0))
    min_number = abs(min(array)) + 1
    multiply, max_number = 1, max(array)
    if max_number <= 25:
        multiply = 10
    for i in range(len(array) + 1):
        if i == 0:
            continue
        else:
            rect_height = (array[i - 1] + min_number) * multiply
            if not final:
                pygame.draw.rect(win, (255, 0, 0), (width * 2 * i, window_height - rect_height - margin_bottom,
                                                    width, rect_height))
            else:
                pygame.draw.rect(win, (0, 255, 0), (width * 2 * i, window_height - rect_height - margin_bottom,
                                                    width, rect_height))
            num_font = pygame.font.SysFont('Arial', 15)
            num_next = num_font.render(str(array[i - 1]), False, (255, 255, 255))
            win.blit(num_next, ((width * 2 * i), window_height - margin_bottom // 1.5))
    pygame.time.delay(500)
    pygame.display.update()


def my_sort(array, reverse=False, key=None, visualization=False):
    key = key if key is not None else lambda x: x
    tim_sort(array, 4, key, visualization)
    return array if not reverse else list(reversed(array))

