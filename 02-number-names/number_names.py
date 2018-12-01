a = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    15: 'fifteen',
}

b = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
}

def number_name(n):
    s = [int(d) for d in str(n)]
    if n in a:
        return a[n]
    if n < 20:
        return f'{a[s[1]]}teen'
    if len(s) == 2:
        if s[0] in b:
            if s[1] == 0:
                return b[s[0]]
            return f'{b[s[0]]} {a[s[1]]}'
        return f'{a[s[0]]}ty {a[s[1]]}'
    if len(s) == 3:
        r = int(''.join(str(i) for i in s[1:]))
        if r == 0:
            return f'{a[s[0]]} hundred'
        return f'{a[s[0]]} hundred and {number_name(r)}'
    if len(s) < 7:
        t = int(''.join(str(i) for i in s[:-3]))
        r = int(''.join(str(i) for i in s[-3:]))
        return f'{number_name(t)} thousand, {number_name(r)}'
    m = int(''.join(str(i) for i in s[:-6]))
    r = int(''.join(str(i) for i in s[-6:]))
    return f'{number_name(m)} million, {number_name(r)}'
