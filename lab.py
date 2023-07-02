import os
import json
import asyncio
from watchfiles import awatch, run_process



async def main():
  # Internally, run_process uses watch with raise_interrupt=False so the function exits cleanly upon Ctrl+C.
  async for changes in awatch('/Volumes/Macintosh HD - Data/STT-NF/semester6/Pemrograman Sistem Jaringan/UAS', raise_interrupt=False):
    print(changes)

asyncio.run(main())



# def callback(changes):
#   print('changes detected:', changes)

# def foobar(a, b):
#   print('foobar called with:', a, b)

# if __name__ == '__main__':
#   run_process('/Volumes/Macintosh HD - Data/STT-NF/semester6/Pemrograman Sistem Jaringan/UAS', target=foobar, args=(1, 2), callback=callback)



# def foobar(a, b, c):
#     # changes will be an empty list "[]" the first time the function is called
#     changes = os.getenv('WATCHFILES_CHANGES')
#     changes = json.loads(changes)
#     print('foobar called due to changes:', changes)
#     if (len(changes) > 0):
#       print(changes[0][0])

# if __name__ == '__main__':
#     run_process('/Volumes/Macintosh HD - Data/STT-NF/semester6/Pemrograman Sistem Jaringan/UAS', target=foobar, args=(1, 2, 3))