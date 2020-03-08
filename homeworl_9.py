import datetime


class Timer:
    def __init__(self, path):
        self.start_time = datetime.datetime.now()
        print(f'Время запуска кода: {self.start_time}')
        self.path = path

    def __enter__(self):
        self.file = open(self.path, encoding='utf-8')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close_time = datetime.datetime.now()
        self.total_time = self.close_time - self.start_time
        print(f'Время окончания кода: {self.close_time}')
        print(f'Время работы кода: {self.total_time}')


if __name__ == '__main__':
    with Timer('test.txt') as test:
        file = test.read()