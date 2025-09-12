
import asyncio

async def greet1():
    print("Starting greet1...")
    await asyncio.sleep(5)
    print("Greet1 finished")

async def greet2():
    print("Starting greet2...")
    await asyncio.sleep(2)
    print("Greet2 finished")

async def main():
    await asyncio.gather(greet1(),greet2())

asyncio.run(main())