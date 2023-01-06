def line_merge(a, b, crossings_a, crossings_b, len_a, len_b):
    list_c = [0 for i in range(len_a + len_b)]
    pointer_a = 0
    pointer_b = 0
    pointer_c = 0
    crossings_c = crossings_a + crossings_b


    while pointer_a < len_a and pointer_b < len_b:
    # L i s t e n w e r d e n n a c h q s o r t i e r t zusammen g e f u e g t .
        if a[pointer_a][2] <= b[pointer_b][2]:
# P o i n t e r w a e h l e n S t e l l e an d e n e n d i e
# E l e m e n t e n a c h q v e r g l i c h e n w e r d e n .
            list_c[pointer_c] = a[pointer_a]
            pointer_a += 1  # w a e h l e n a e c h s t e s El e m e n t
            pointer_c += 1
        else:
            list_c[pointer_c] = b[pointer_b]
    # q E i n t r a g i s t k l e i n e r a l s a l l e v e r b l e i b e n d e n E l e m e n t e von a
    # und s c h n e i d e t s o m i t a l l e v e r b l i e b e n e n L i n i e n i n a .
            crossings_c += len_a - pointer_a
            pointer_b += 1
            pointer_c += 1
    len_c = len_a + len_b
    for i in range(pointer_c, len_c):
    # E r s e t z e d i e a u s g e w a e h l t e n E l e m e n t e a u s a und b i n c .
        if pointer_a == len_a:
            list_c[i] = b[pointer_b]
            pointer_b += 1
        elif pointer_b == len_b:
            list_c[i] = a[pointer_a]
            pointer_a += 1

    list_c += a[pointer_a:] + b[pointer_b:]
    # f u e g e v e r b l e i b e n d e a und b i n c zusammen
    return list_c, crossings_c, len_c


def crossing_lines(line_list, n):


    if n < 2:  # L i s t e n mi t ei n em o d e r w e n i g e r E l e m e n t e n s i n d immer s o r t i e r t
# und k o e n n e n k e i n e S c h n i t t p u n k t e e n t h a l t e n
        return line_list, 0, 1
    else:
        len_a = int(n / 2)
        len_b = n - len_a
        a, crossings_a, len_a = crossing_lines(line_list[: len_a], len_a)
        # r e k u r s i v e r A u f r u f mi t h a l b i e r t e n L i s t e n
        b, crossings_b, len_b = crossing_lines(line_list[len_a:], len_b)
        return line_merge(a, b, crossings_a, crossings_b, len_a, len_b)

test_list = [(6, 0, 1), (3, 1, 2), (2, 2, 6), (5, 3, 0), (4, 4, 4), (7, 5, 5),
             (1, 6, 3)]
print("The sorted list : ", crossing_lines(test_list, 7)[0], "\n number of crosses : ", crossing_lines(test_list, 7)[1])
