#!/usr/bin/env python3
import pathlib
import asyncio
from heimdall import Message


async def handle_message(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info("peername")

    print(f"Received message from {message!r} from {addr!r}")
    print(f"Sending: {message!r}")
    writer.write(data)
    await writer.drain()
    print("Closing connection")
    writer.close()


async def main():
    server = await asyncio.start_server(handle_message, "localhost", 8888)
    addrs = ", ".join(str(sock.getsockname()) for sock in server.sockets)
    print(f"Serving on {addrs}")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
