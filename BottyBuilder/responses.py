import random

def get_response(message: str) -> str:
    # just for convenience in case someone types in a command with upper case but will remove
    # p_message = message.lower()

    if message == 'hello' or p_message == 'hi':
        return 'Hello! My name is BottyBuilder. I will help you achive your fitness goals!'

    if message == '!help':
        return 'Here is the list of commands.\nTo find out your maintenance calorie level, type "!calories".\nFor exercises you can do at the gym, type "!gym".\nFor exercises you can do at home, type "!home".\nTo see a list of foods to facilitate bulking, type "!bulk".\nTo see a list of foods to facilitate cutting, type "!cut".\nFor encouragement, type "!motivation".'

    # Handle user input for calculating calories
    if message == '!calories':
        return 'Please enter your height in cm.'
    
    # figure out how to get bot to retrieve info through discord





    return 'Sorry, I didn\'t get that. Try typing "!help".'

