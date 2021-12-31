import asyncio

async def get_chat_id(name):
    await asyncio.sleep(3)
    print("In get_chat_id")
    return "chat-%s" % name


def get_chats(name):
    #await asyncio.sleep(3)
    print("In get_chat_id")
    return "chat-%s" % name

#@sync_to_async
def get_chat_id_v1(name):
    return "chat-%s" % name 


async def main():
    result = await get_chat_id("django")
    print(result)
    result=get_chats("SSS")
    print(result);
    print("In Main")
    for i in range(0,1):
        import time
        time.sleep(11);
        print("Ram");
    for i in range(0,1):
        print("Shiv");
      


if __name__ ==  '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
#main();