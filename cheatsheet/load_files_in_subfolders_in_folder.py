import os

print('Loading cogs...\n') #intialize cogs loading
for fldr in os.listdir('cogs'): 
    print(fldr + '\n') #logs loading nicely

    for filename in os.listdir(('./cogs/' + fldr)): 
        print(f'- {filename[:-3]}') #logs filename nicely
        
        if filename.endswith('.py'): #if it is a python file
            bot.load_extension(f'cogs.{fldr}.{filename[:-3]}') #load extension 