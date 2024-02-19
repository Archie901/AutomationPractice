import asyncio

async def fetch_data(url):
    print("Начало загрузки данных")
    await asyncio.sleep(3)  # Имитация задержки при загрузке
    print("Данные загружены")
   
async def something():
    tasks = [fetch_data("http://example.com") for _ in range(5)]
    await asyncio.gather(*tasks)
        
if __name__ == "__main__":
    asyncio.run(something())