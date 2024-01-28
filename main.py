# import time
#
#
# def red():
#     print("Горит красный свет")
#     time.sleep(5)
#
#
# def yellow():
#     print("Горит желтый свет")
#     time.sleep(2)
#
#
# def green():
#     print("Горит зеленый свет")
#     time.sleep(3)
#
#
# red()
# yellow()
# green()
#
# import asyncio
#
#
# async def red():
#     print("Горит красный свет")
#     await asyncio.sleep(5)
#
#
# async def yellow():
#     print("Горит желтый свет")
#     await asyncio.sleep(2)
#
#
# async def green():
#     print("Горит зеленый свет")
#     await asyncio.sleep(3)
#
#
# async def main():
#     await asyncio.gather(red(), yellow(), green())
#
#
# asyncio.run(main())
#
# import threading
# import time
#
#
# def red():
#     print("Горит красный свет")
#     time.sleep(5)
#
#
# def yellow():
#     print("Горит желтый свет")
#     time.sleep(2)
#
#
# def green():
#     print("Горит зеленый свет")
#     time.sleep(3)
#
#
# t1 = threading.Thread(target=red)
# t2 = threading.Thread(target=yellow)
# t3 = threading.Thread(target=green)
#
# t1.start()
# t2.start()
# t3.start()
#
# t1.join()
# t2.join()
# t3.join()
