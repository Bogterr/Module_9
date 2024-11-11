# Генераторы


def all_variants(text):
    len_txt = len(text)
    list = []
    for run in range(len_txt):
        for stop in range(run + 1, len_txt + 1):
            list.append(text[run:stop])
            # yield text[run:stop]

    qsort(list)
    return list


def qsort(a):
    stop = False
    while stop == False:
        count = 0
        for i in range(len(a) - 1):
            if len(a[i]) > len(a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                count += 1
            elif count == 0 and i == len(a) - 2:
                stop = True
    return a


a = all_variants("abc")
for i in a:
    print(i)
