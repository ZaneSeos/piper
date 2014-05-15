# -*- coding: utf-8 *-*
'''HTTP Server for PIPER, Version 1'''


import littlehttpserver
import os
import colorama

#Will run piper-http with the VERBOSE (learning) option
#Note that while this looks ugly, it's supposed to be simple
def run_verbose():
    print("PIPER Proof-Of-Concept HTTP Server (using LittleHTTPServer 0.1.4)")
    print("LittleHTTPServer created by Tetsuya Morimoto")
    print("Documents are located at http://bitbucket.org/t2y/littlehttpserver")
    print('')
    print('')
    print('Welcome to the PIPER HTTP Server Proof of Concept!')
    print('--------------------------------------------------')
    print('')
    print('')
    print('In this program, you can create an HTTP (Web) server that provides')
    print('web pages for what would be all the Internet to see. However, this')
    print('proof of concept is only for a small local area network. Make sure')
    print('this server is NOT connected to the Internet, and that you have')
    print('another computer to test this with.')
    print('')
    print('')
    input('Press Enter to get started!')
    print("\n" * 80)
    print('STEP ONE: Setting up the default directory')
    print('------------------------------------------')
    print('')
    print('First, you need to set up a default directory (folder) for your')
    print('web page files to be at! Usually the server will expect a file')
    print('named "index.html" as the first web page.')
    print('')
    #Asks for the file directory in which the server folder will be held
    filedir = input('Specify the full path name for the default directory: ')
    boole = input(filedir, ': Is this correct? Answer y/n: ')
    if boole == 'Y' | 'y':
        continue
    else:
            filedir = input('Specify the full path for the default folder:')
    input('Press Enter to continue.')
    print("\n" * 80)
    print('STEP TWO: Setting up any other directories')
    print('------------------------------------------')



run_verbose()