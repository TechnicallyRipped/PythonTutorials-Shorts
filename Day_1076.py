

from rich.prompt import Confirm

answer = Confirm.ask("Continue?")

print(answer)

if answer:
    print('Continuing...')
else:
    print('Ending...')











# while True:
#     answer = input('Continue? [y/n] ').lower()
#     if answer == 'y':
#         print('Continuing...')
#         break
#     elif answer == 'n':
#         print('Ending...')
#         break
#     else:
#         print('Invalid response')