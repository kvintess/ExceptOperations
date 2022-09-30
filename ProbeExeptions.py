try:

    i = v
    print('done')
except (ZeroDivisionError, NameError) as exc:
    print(f'{exc}')