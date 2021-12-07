import os

for filename in os.listdir('module'): #folder name
        if filename.endswith('.py'): #filename.py
            bot.load_extension(f'module.{filename[:-3]}') #module.filename