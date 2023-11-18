import asyncio
import time

async def brew_coffee():
    print('start brew_coffee()')
    await asyncio.sleep(3)
    print('end brew_coffee()')
    return 'Coffee ready'

async def toast_bagel():
    print('start toast_bagel()')
    await asyncio.sleep(2)
    print('end toast_bagel()')
    return 'Bagel toasted'



async def main():
    start = time.time()

    # batch = asyncio.gather(brew_coffee(), toast_bagel())
    # coffee, bagel = await batch

    coffee_task = asyncio.create_task(brew_coffee())
    bagel_task = asyncio.create_task(toast_bagel())
    coffee, bagel = await coffee_task, await bagel_task

    end = time.time()
    elapsed = end - start
    print(coffee)
    print(bagel)
    print(elapsed)

if __name__ == '__main__':
    asyncio.run(main())