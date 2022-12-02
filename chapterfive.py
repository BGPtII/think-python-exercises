import time
import turtle


def time_since_epoch():
    sec_since_epoch = time.time()
    min_since_epoch = sec_since_epoch / 60
    sec_since_epoch = sec_since_epoch % 60
    hour_since_epoch = min_since_epoch / 60
    min_since_epoch = min_since_epoch % 60
    day_since_epoch = hour_since_epoch / 24
    hour_since_epoch = day_since_epoch % 24
    print('Since "the epoch", it has been...')
    print(day_since_epoch, 'days,', hour_since_epoch, 'hours,',
          min_since_epoch, 'minutes &', sec_since_epoch, 'seconds.')


def check_fermat(a, b, c, n):
    """Takes four parameters — a, b, c and n—and checks to see if Fermat’s theorem holds. If n is greater than 2
    and a^n + b^n = c^n the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program
    should print, “No, that doesn't work.”
    """
    if n > 2 and a ** n + b ** n == c ** n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print("No, that doesn't work.")


def fermat_values():
    """Prompts the user to input values for a, b, c and n, converts them to integers,
    and uses check_fermat to check whether they violate Fermat’s theorem
    """
    a = int(input('Enter the value for a: '))
    b = int(input('Enter the value for b: '))
    c = int(input('Enter the value for c: '))
    n = int(input('Enter the value for n: '))
    check_fermat(a, b, c, n)


def koch(t, length):
    t = turtle.Turtle()
    t.fd(length/3)
    t.lt(60)
    t.fd(length/3)
    t.rt(120)
    t.fd(length/3)
    t.lt(60)
    t.fd(length/3)


def snowflake(t, length):
    t = turtle.Turtle()
    t.lt(60)
    koch(t, length)
    t.rt(120)
    koch(t, length)
    t.rt(120)
    koch(t, length)


def koch_snowflake_i3(t, length):
    t = turtle.Turtle()
    t.lt(120)
    koch(t, length)
    t.rt(120)
    koch(t, length)
    for i in range(5):
        t.lt(60)
        koch(t, length)
        t.rt(120)
        koch(t, length)
