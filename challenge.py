import time


def finish_date(func):
    def add_date(*args, **kwargs):
        func(*args, **kwargs)
        local_time = time.localtime()
        formated_time = time.strftime("%d/%m/%Y - %H:%M:%S", local_time)
        print(f'The function {func.__name__} ends at:{formated_time}')
    return add_date


@finish_date
def palindrome(string):
    string = string.replace(' ', '').lower()
    return string == string[::-1]


@finish_date
def long_function():
    for _ in range(1000000):
        pass


def run():
    palindrome('Ana')
    long_function()


if __name__ == '__main__':
    run()
