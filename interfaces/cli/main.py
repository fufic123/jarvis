def main():
    from core.jarvis import JarvisCore
    
    jarvis = JarvisCore()
    
    while True:
        user_input = input("$ ")
        if user_input in ['exit', 'quit']:
            break
        
        response = jarvis.process_input(user_input)
        

if __name__ == '__main__':
    main()