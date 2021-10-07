
def bounded_ratio(a, l, r):
    # a[i] = (i + 1) * x such that l <= x <= r

    b = list()
    for index, element in enumerate(a):
        top = (element // (index + 1))
        rem = (element % (index + 1))
        print(top, rem)
        
        if (
            top
            and rem == 0
            and top <= r
            and top >= l
        ):
            b.append(True)
        else:
            b.append(False)
    
    return b


b = bounded_ratio([8,5,6,16,5], 1, 3)

print(b)