# -*- coding: utf-8 *-*
'''HTTP Server for PIPER, Version 1'''


import littlehttpserver
import os
#TODO: Double check colorama functions to integrate usage
from colorama import *


#Will run piper-http with the VERBOSE (learning) option
#Note that while this looks ugly, it's supposed to be simple
class run_verbose():
    def  __init__(self):
        def run_verbose():
            print(Fore.WHITE + "PIPER Proof-Of-Concept HTTP Server" +
            Fore.GREEN + "(on LittleHTTPServer 0.1.4)")
    print(Fore.YELLOW + "LittleHTTPServer created by Tetsuya Morimoto")
    print(Fore.YELLOW + "Documents are located at" +
    Fore.YELLOW + "http://bitbucket.org/t2y/littlehttpserver")
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
    eval(input('Press Enter to get started!'))
    print(("\n" * 10))
    print('STEP ONE: Setting up the default directory')
    print('------------------------------------------')
    print('')
    print('First, you need to set up a default directory (folder) for your')
    print('web page files to be at! Usually the server will expect a file')
    print('named "index.html" as the first web page.')
    print('')
    #Asks for the file directory in which the server folder will be held
    filedir = eval(input('Type the full path name for the default directory: '))
    boole = eval(input('No mistakes? Answer y/n: '))
    #OPTIMIZE: Needs a logic sanity check to ensure no wasted clock time
    if (boole is ('n' or 'N') and not ('Y' or 'y')):
        filedir = (eval(input('Specify the full path for the default folder:'))
    print(("\n" * 10))
    print('STEP TWO: Setting up any other directories')
    print('------------------------------------------')
    print('')
    print('')
    #Simple while structure that adds any input strings to a list
    boole2 = input('Add directories? y/n: ')
    #FIXME: Now causes if loop to pass no matter input
    if (boole2 is ('y' or 'Y') and not ('n' or 'N')):
        keep_running = True
        while (keep_running is True):
            dirlist = []
            item = 0
            adddir = input('Input the other directories (x to quit): ')
            if (addir is not 'x' or 'X'):
                for item in dirlist:
                    addir = dirlist[item]
                    item + 1
            else:
                keep_running = False