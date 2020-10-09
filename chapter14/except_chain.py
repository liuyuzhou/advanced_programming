def example():
    try:
        int('N/A')
    except ValueError as e:
        raise RuntimeError('A parsing error occurred') from e

example()


try:
    example()
except RuntimeError as e:
    print("It didn't work:", e)

    if e.__cause__:
        print('Cause:', e.__cause__)


def example2():
    try:
        int('N/A')
    except ValueError as e:
        print(f"Couldn't parse: {err}")

example2()


def example3():
    try:
        int('N/A')
    except ValueError:
        raise RuntimeError('A parsing error occurred') from None

example3()


try:
   ...
except SomeException as e:
   raise DifferentException() from e


try:
   ...
except SomeException:
   raise DifferentException()