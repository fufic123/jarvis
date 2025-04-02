import asyncio

async def main():
    from core.jarvis import JarvisCore
    
    jarvis = JarvisCore()
    
    while True:
        user_input = input("$ ")
        if user_input in ['exit', 'quit']:
            break
        
        response = await jarvis.process_input(user_input)
        print(response)

if __name__ == '__main__':
    asyncio.run(main())