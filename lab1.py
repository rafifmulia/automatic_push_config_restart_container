import asyncio
from watchfiles import awatch, Change

async def main():
  async for changes in awatch('/Volumes/Macintosh HD - Data/STT-NF/semester6/Pemrograman Sistem Jaringan/UAS'):
    for change in changes:
      # only work when the file has been added when the program run
      if (Change.modified == change[0]):
        print(change[1])

asyncio.run(main())
