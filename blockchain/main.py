#! /usr/bin/env python3
# -*- coding:utf-8 -*-

"""

    Enviando mensajes encriptados a travez de la red



# import asyncio
import struct
import blockchain

header_struct = struct.Struct('!I')  # messages up to 2**32 - 1 in length


async def recvall(reader, length):
    blocks = []
    while length:
        block = await reader.read(length)
        if not block:
            raise EOFError('socket closed with {} bytes left'
                           ' in this block'.format(length))
        length -= len(block)
        blocks.append(block)
    return b''.join(blocks)


async def get_block(reader):
    data = await recvall(reader, header_struct.size)
    (block_length,) = header_struct.unpack(data)
    data = await recvall(reader, block_length)
    return data.decode('ascii')


async def put_block(writer, message):
    encoded_message = message.encode('ascii')
    block_length = len(encoded_message)
    writer.write(header_struct.pack(block_length))
    writer.write(encoded_message)


async def handle_conversation(reader, writer):
    address = writer.get_extra_info('peername')
    print("Accepted connection from {}".format(address))

    await put_block(writer, "******Welcome to NOMAD'S Server******")
    await put_block(writer, "Please send your firstname and lastname")

    name = await get_block(reader)
    print("name sent is {}".format(name))


global n
n = 0


def make_account(first_name, last_name):
    n += 1
    acc = blockchain.Account(first_name, last_name, n)
    return acc


if __name__ == "__main__":
    acc = blockchain.Account(1, "Gilberto", "Dominguez")
    acc2 = blockchain.Account(2, "Etien", "Dominguez")


    address = ("192.168.100.32", 8080)
    loop = asyncio.get_event_loop()

    coro = asyncio.start_server(handle_conversation, *address, reuse_port=True)
    server = loop.run_until_complete(coro)
    print("Listening at {}".format(address))

    try:
        loop.run_forever()
    finally:
        server.close()
        loop.close()
    """
# EOF
