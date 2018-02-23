import asyncio
import aiohttp
import async_timeout
from aiohttp import FormData

async def post(session, url):
	with async_timeout.timeout(60):
		data = FormData()
		data.add_field('file', open('lamb.jpg', 'rb'), filename='lamb.jpg', content_type='image/jpeg')
		data.add_field('action[]', 'post1')
		data.add_field('action[]', 'post2')

		async with session.post(url, data=data) as response:
			return await response.text()

async def main(loop):
	async with aiohttp.ClientSession(loop=loop) as session:
		url = 'http://172.17.0.1:8000/index.php'
		resp = await post(session, url)
		print(resp)

loop = asyncio.get_event_loop()
loop.run_until_complete(main(loop))
loop.close()