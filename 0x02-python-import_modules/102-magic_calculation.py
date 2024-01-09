def magic_calculation(g, h):
    add, sub = magic_calculation_102.add, magic_calculation_102.sub

    if g < h:
        c = add(g, h)

        for i in range(4, 6):
            c = add(c, i)

        return c

    return sub(g, h)

