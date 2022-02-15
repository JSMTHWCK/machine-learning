def even_or_odd(n):
    x = [int(a) for a in str(n)]
    x = x[:1][0]
    if x == 0:
        return 'even'
    elif x == 1:
        return 'false'
    elif x == 2:
        return 'even'
    elif x == 3:
        return 'odd'
    elif x == 4:
        return 'even'
    elif x == 5:
        return 'odd'
    elif x == 6:
        return 'even'
    elif x == 7:
        return 'odd'
    elif x == 8:
        return 'even'  
    elif x == 9:
        return 'odd'
print(even_or_odd(2))

