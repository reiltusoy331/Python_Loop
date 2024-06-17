iter_obj = iter(range(5))


while True:
    try:
        i = next(iter_obj)
        print(i)
    except StopIteration:
        break