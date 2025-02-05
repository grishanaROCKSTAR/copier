import os
import sys

print('\n\n\nWelcome to copier! Enter a path to the file!')
path = input('\n/PATH/TO/THE/FILE: ')
fname = path.split('/')[-1]

if path == ('~~rmall/all'):
    print('\nStarted a work on deleting "output" directory..')
    os.system('rm -rf output')
    print('[DONE]')
    print('\nAll copied files has been deleted')
    sys.exit()

number = input('File number (Press enter for 1): ')

if number == (''):
    number = 1

elif number == ('~~nn'):
    number = ''
else:
    number = int(number)

cp= f'cp {path} output/{fname}{number}'
sure= input('\nAre you sure? [y], [n]: ')
permission= f'chmod 777 ./output; chmod 777 output/*'

if sure== ('y'):
    print('\nMaking an "output" directory..')
    os.makedirs('output', exist_ok=True)
    print('[Done]')
    print('Started a work on copying..')
    os.system(cp)
    print('[DONE]')
    print('Giving permissions..')
    print('[DONE]')
    os.system(permission)
    print('Copying finished!\n')

elif sure== ('n'):
    print('\nCopying aborted!')
