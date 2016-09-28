import os
from os import path
from sys import argv
import re
import pytest
import asyncio


def exclude(string):
    if "py" in string and\
        "pyc" not in string:
        return string


def get_files(mypath):
    """generator to get all the files under mypath"""
    for path, subdirs, files in os.walk(mypath):
        for name in files:
            name = exclude(name)
            if name:
                if "test" in name:
                    yield os.path.join(path, name)


def get_paths(mypath):
    """a generator expr to get the md5 hash and filepath"""
    #if path.isfile(mypath): return mypath
    return ( x for x in get_files(mypath) )


def get_test_functions(file):
    pattern = re.compile("def\s+(test.*)\(\):")

    with open(file) as test_fh:
        for line in test_fh:
            m = pattern.match(line)
            if m:
                yield "%s::%s" % (file, m.groups(0)[0])



# async def slow_operation(n):
#     await asyncio.sleep(1)
#     pytest.main(["-qq", mod])


# async def main(mypath):
#     await asyncio.wait([
#         list(map(lambda x: pytest.main(["-qq", x]),
#             map(lambda y: get_test_functions(y), get_paths(mypath))
#             ))
#     ])

async def slow_operation(n):
    #await asyncio.sleep(1)
    print("Slow operation {} complete".format(n))


async def main(mypath):
    async_list = [1, 2, 3]
    await asyncio.wait(
        map(slow_operation, async_list)
    )


# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())



# def main(mypath):
#     for file in get_paths(mypath):
#         for mod in get_test_functions(file):
#             pytest.main(["-qq", mod])


if __name__ == '__main__':
    mypath = argv[1]
    #main(mypath)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(mypath))
