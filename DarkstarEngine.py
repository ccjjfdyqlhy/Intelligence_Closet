print('[DE][INFO]USE ANOTHER VERSION OF THIS')
print('[DE][INFO]Type "help" for help file.')
import os
def Crash():
    print('Stopping the App.')
    import App_Crasher
def Restart():
    print('Restarting the App.')
    os.system('choice /t 5 /d y /n start python App.py')
    import App_Crasher
def ClearConfig():
    print('Delating config.ICset.')
    os.system('del config.ICset')
def UploadErrors():
    print('Uploading log file.')
    print('ERR:Nothing to upload')
def fuck():
    print('weird.')
def website():
    print('Starting web browser.')
    os.system('open https://github.com/ccjjfdyqlhy')
while True:
    a=input('>>>')
    if a == 'help':
        print('[DE]Help File\ncrash - crash the App.\nrestart - restart the App.\nclearconfig - delate the config file.\nuploaderrors - upload the error log.\nwebsite - open the website of the creator of DE.\nfuck - weird.\nhelp - show this help file.\nquit - quit the prompt.')
    elif a == 'quit':
        quit()
    elif a == 'crash':
        b=input('[DE][WAIT][WARN]Are you SURE to crash python.exe? This will end this engine too!(Y/Other):')
        if b == 'Y':            
            Crash()
        else:
            print('[DE][INFO]Canceled.')
    elif a == 'restart':
        Restart()
    else:    
        print('[DE]No such command.')

