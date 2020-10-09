# try:
#    ...
# except Exception as e:
#    ...
#    log('Reason:', e)


def parse_int(s):
    try:
        n = int(v)
    except Exception:
        print("Couldn't parse")


parse_int('n/a')
parse_int('30')


def parse_int(s):
    try:
        n = int(v)
    except Exception as e:
        print("Couldn't parse")
        print('Reason:', e)


parse_int('30')