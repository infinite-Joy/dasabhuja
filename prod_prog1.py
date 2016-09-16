import asyncio
import time

def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('%s function took %0.3f ms' % (f.__name__, (time2-time1)*1000.0))
        return ret
    return wrap

# Borrowed from http://curio.readthedocs.org/en/latest/tutorial.html.

def simple_countdown(number, n):
    while n > 0:
        print('T-minus', n, '({})'.format(number))
        yield
        n -= 1


@asyncio.coroutine
def countdown(number, n):
    while n > 0:
        print('T-minus', n, '({})'.format(number))
        yield from asyncio.sleep(2)
        n -= 1


@timing
def async_main():
	loop = asyncio.get_event_loop()
	tasks = [
	    asyncio.ensure_future(countdown("A", 2)),
	    asyncio.ensure_future(countdown("B", 3))]
	loop.run_until_complete(asyncio.wait(tasks))
	loop.close()



@timing
def simple_main():
	inst = simple_countdown("A", 2)
	for x in inst:
		time.sleep(2)
		x


	inst = simple_countdown("B", 3)
	for x in inst:
		time.sleep(2)
		x

if __name__ == '__main__':
	simple_main()
	print("####################################")
	async_main()
