#by mahi sokhary (Qoqnus-master)
#Qoqnus-master.netlify.app
#github.com/mahisokhary/html-cloner

import aiohttp
import asyncio
import os

async def html(x):
	async with aiohttp.ClientSession() as session:
	       	async with session.get(x) as response:
        			print(await response.text())

async def js_css(url):
	os.system(f"wget {url}")
	file = url.split("/")[len(url.split("/")) - 1]
	if file.split(".")[1] == "js" or file.split(".")[1] == "css":
		os.system(f"cat {file}")
	else:
		print("EROR: file is not js or css")
	
async def other(url):
	os.system(f"wget {url}")
	
async def requirements():
	os.system("apt-get install wget -y")

async def main():
	while True:
		print("what do u want to do??")
		print("check requirements: 1")
		print("download html: 2")
		print("download js or css file: 3")
		print("download file: 4")
		print("exit: 5")
		print("")
		print("enter a code:")
		x = int(input(">>"))
	
		if x == 1:
			await requirements()
		elif x == 2:
		     print("enter a url:")
		     y = input(">>")
		     await html(y)
		elif x == 3:
		     print("enter a url:")
		     y = input(">>")
		     await js_css(y)
		elif x == 4:
		     print("enter a url:")
		     y = input(">>")
		     await other(y)
		elif x == 5:
			exit()
		else:
			print("EROR: unknown code")

if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main())