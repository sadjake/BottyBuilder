import random

def get_response(message: str) -> str:
    # just for convenience in case someone types in a command with upper case but will remove
    # p_message = message.lower()

    if message == 'hello' or p_message == 'hi':
        return 'Hello! My name is BottyBuilder. I will help you achive your fitness goals!'

    if message == '!help':
        return 'Here is the list of commands.\nTo find out your maintenance calorie level, type "!calories".\nFor exercises for each muscle group, type "!exercises".\nTo see a list of foods to facilitate bulking, type "!bulk".\nTo see a list of foods to facilitate cutting, type "!cut".\nFor encouragement, type "!motivation".'

    # Handle user input for calculating calories
    if message = '!calories':
        return 'Please enter your height in cm.'
    
    if message = '!exercises':
        return 'Here is a list of muscle groups to train with their commands.\nChest - "!chest"\nBack - "!back"\nArms - "!arm"\nShoulders - "!shoulders"\nLegs - "!legs"'
    
    if message = '!chest':
        return 'For chest exercises to do at the gym, type "!gymchest".\nFor chest exercises to do at home, type !homechest".'
    
    if message = '!gymchest':
        return 'lol'
    
    if message = '!homechest':
        return 'lol'

    if message = '!back':
        return 'For back exercises to do at the gym, type "!gymback".\nFor back exercises to do at home, type "!homeback".'
    
    if message = '!gymback':
        return 'lol'
    
    if message = '!homeback':
        return 'lol'
        
    if message = '!arms':
        return 'For arm exercises to do at the gym, type "!gymarms".\nFor arm exercises to do at home, type "!homearms".'
    
    if message = '!gymarms':
        return 'lol'
    
    if message = '!homearms':
        return 'lol'
        
    if message = '!shoulders':
        return 'For shoulder exercises to do at the gym, type "!gymshoulders".\nFor shoulder exercises to do at home, type "!homeshoulders".'
    
    if message = '!gymshoulders':
        return 'lol'
    
    if message = '!homeshoulders':
        return 'lol'

    if message = '!legs':
       return 'For back exercises to do at the gym, type "!gymlegs".\nFor leg exercises to do at home, type "!homelegs".'

    if message = '!gymlegs':
        return 'lol'
    
    if message = '!homelegs':
        return 'lol'
    
    if message = '!bulk':
        return 'Here are a list of foods that are high in calorie.\n'
    
    if message = '!cut':
        return 'Here are a list of foods that are low in calorie.\n"
    
    if message = '!motivation':
        return 'Reminder to drink plenty of water!'
    
    # figure out how to get bot to retrieve info through discord


    return 'Sorry, I didn\'t get that. Try typing "!help".'

