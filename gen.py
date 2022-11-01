# def gen_range(stop, start=1, step=1):
#     num = start
#     while num <= stop:
#         yield num
#         num += step

# generator = gen_range(5)
# print(generator)
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))


# generator = gen_range(10)
# print(list(generator))

# def gen_fib():
#     a, b = 0, 1
#     while True:
#         a, b = b, a + b
#         yield a

# fib = gen_fib()
# [next(fib) for _ in range(50)[-1]]


def char_range(start, stop, step=1)
    stop_modifier = 1
    start_code= ord(start)
    stop_code = ord(stop)
    
    if start_code > stop_code:
        stepp *= -1
    for value in range(start_code, stop_code + stop_modifier, step)
        yield chr(value)
    