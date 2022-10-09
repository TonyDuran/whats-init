#!/usr/bin/env python3
import asyncio
import multiprocessing

async def send_message(message):
    reader, writer = await asyncio.open_connection(
        '127.0.0.1', 8888)

    print(f'Send: {message!r}')
    writer.write(message.encode())

    data = await reader.read(100)
    print(f'Received: {data.decode()!r}')

    print('Close the connection')
    writer.close()

def target(message):
    asyncio.run(send_message(message))

def main():
    # terrible example to test spamming server
    urls = ['google.com',
            'bing.com',
            'example.com'] * 100

    with multiprocessing.Pool(3) as p:
        p.map(target, urls)

if __name__ == '__main__':
    main()
