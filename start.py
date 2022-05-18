
from main import users


async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await users.start()
    print("[INFO]: STARTING PYTGCALLSS CLIENT")
    await users.stop()


loop = asyncio.get_event_loop()
loop.run_until_complete(start_bot())
