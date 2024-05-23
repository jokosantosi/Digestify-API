import dotenv
import os
import asyncio
import json
import aiohttp
dotenv.load_dotenv()

thelazyAPI = os.getenv('THE_LAZY_BASE_API')
gptAPI = os.getenv('GPT_BASE_API')


async def getGamesNews():
    async with aiohttp.ClientSession() as session:
        async with session.get(thelazyAPI+"/api/games?page=2") as resp:
            return await resp.json(content_type="application/json")

async def getDetailNews(key):
    async with aiohttp.ClientSession() as session:
        async with session.get(thelazyAPI+"/api/detail/"+key) as resp:
            return await resp.json(content_type="application/json")

async def summarize(newsContent):
    body = {
        "model": "gpt-3.5-turbo-0125",
        "messages": [
            {
            "role": "user",
            "content": newsContent+"dari paragraft yang aku berikan tadi tolong rangkum dan carikan intisari dari paragraf tersebut dan balas hanya hasil dari rangkuman tersbut yang tidak lebih dari 1 paragraf"
            }
        ],
        "stream": False
    }
    async with aiohttp.ClientSession() as session:
        fullRespText = ""
        async with session.post(gptAPI+'/api/conversation', json=body) as resp:
            async for chunk in resp.content:
                data_str = chunk.decode("utf-8")
                json_str = data_str.replace("data: ", "")
                if json_str == "\n" or json_str.strip() == "[DONE]":
                    pass
                else:
                    data_dict = json.loads(json_str)
                    fullRespText = data_dict["message"]
        return fullRespText

async def main():
    newsList = await asyncio.create_task(getGamesNews())
    
    getNewsTask = []
    for news in newsList:
        getNewsTask.append(asyncio.ensure_future(getDetailNews(news["key"])))
        
    newsDetails = await asyncio.gather(*getNewsTask)
    
    summarizeTask = []
    
    for newsDetail in newsDetails[:4]:
        fullContent = ""
        
        for content in newsDetail["results"]["content"]:
            if content.find("https://") == -1:
                fullContent += content
        
        summarizeTask.append(asyncio.ensure_future(summarize(fullContent)))
    
    newsSummarize = await asyncio.gather(*summarizeTask)
    
    with open("dummyDB.json", "r") as f:
        db = json.load(f)
        
    for i in range(len(newsSummarize)):
        db["database"].append({
            "id": f'{len(db["database"])+1}',
            "title": newsDetails[len(db["database"])%10]["results"]["title"],
            "date": newsDetails[len(db["database"])%10]["results"]["date"],
            "image_url": newsDetails[len(db["database"])%10]["results"]["content"][0],
            "categories": newsDetails[len(db["database"])%10]["results"]["categories"],
            "original_url": "https://thelazy.media/"+newsList[len(db["database"])%10]["key"],
            "content": newsSummarize[i]
        })
    
    with open("dummyDB.json", "w") as f:
        json.dump(db, f, indent=4)

asyncio.run(main())