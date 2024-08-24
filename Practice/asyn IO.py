# Asynchronous I/O or async for short 
#It is a programing pattern that allows for high performance in a concurrent and non blocking manner.

import time
import asyncio
import requests

async def function1():
    async def function1():
  print("func1")
  URL = 
"https://instagram.com/favicon.ico"
  response = requests.get(URL)
  open("instagram1.ico", "wb").write(response.content)
   
  
    

async def function2():
  print("func2")
  URL = 
"https://instagram.com/favicon.ico"
  response = requests.get(URL)
  open("instagram2.ico", "wb").write(response.content)
   
    # await asyncio.sleep(1)

async def function3():
  print("func3")
  URL = 
"https://instagram.com/favicon.ico"
   response = requests.get(URL)
  open("instagram3.ico", "wb").write(response.content)
    # await asyncio.sleep(3)

# # Make a task 
# async def main():
#     task = asyncio.create_task(function1())
#     await function2()
#     await function3()
# asyncio.run(main())
 
async def main():
  L = await asyncio.gather(
       function1(),
       function2(),
       function3(),
    )
  print(L)

asyncio.run(main())

