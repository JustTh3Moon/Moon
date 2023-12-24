from datetime import datetime

now = datetime.now()
dt = now.strftime("%d/%m/%Y %H:%M:%S")

print(f"Current date and time:\n{dt}")