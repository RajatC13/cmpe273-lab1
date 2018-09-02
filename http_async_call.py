import asyncio
import requests

async def get_date(name, timeout):
    await asyncio.sleep(timeout)
    r = requests.get('https://webhook.site/dbf057be-8834-464d-a48b-531a2be264a5')
    print(f'Process {name}: '+r.headers['Date'])


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(
    get_date("A", 5.0),
    get_date("B", 1.0),
    get_date("C", 3.0),
))
loop.close()
