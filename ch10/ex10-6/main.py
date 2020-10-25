import multiprocessing


def make_file():
    import random
    from time import sleep
    random.seed()
    wait = random.uniform(1, 5)
    sleep(wait)
    print(f'sleep {wait} done')


if __name__ == '__main__':
    for i in range(3):
        p = multiprocessing.Process(target=make_file)
        p.start()
