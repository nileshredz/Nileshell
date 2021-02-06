# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 14:40:04 2020

@author: Nilesh
"""
from datetime import datetime
import webbrowser
import os
from time import sleep
import speech_recognition as sr
from translate import Translator




################################
# Initial Program with functions
################################
def start():
        print("+"+"-"*78,end = "+")
        print("\n|"+" "*29+"Welcome to Nileshell"+" "*29,end = "|")
        print("\n|"+" "*24+"Email: nilesh_ohol@outlook.com"+" "*24,end = "|")
        print("+"+"-"*78,end = "+\n") # 80 Len
        

        print("+"+"-"*78,end = "+")
        print("\n| Commands:"+" "*68+"|\n| 14 Features"+" "*66+"|")
        print("+"+"-"*78,end = "+")
        print("| break - To Quit the window"+" "*(80 - len("| break - To Quit the window")-1)+"|")
        print("| largeodd - To find the large Odd"+" "*(80 - len("| largeodd - To find the large Odd")-1)+"|")
        print("| dtime - To fetch the System time"+" "*(80 - len("| dtime - To fetch the System time")-1)+"|")
        print("| clear - clear Screen"+" "*(80 - len("| clear - clear Screen")-1)+"|")
        print("| pwd - Current Working Directory"+" "*(80 - len("| pwd - Current Working Directory")-1)+"|")
        print("| listdir - List Directory"+" "*(80 - len("| listdir - List Directory")-1)+"|")
        print("| dirch - change the Directory."+" "*(80 - len("| dirch - change the Directory.")-1)+"|")
        print("| eline - Echo."+" "*(80 - len("| eline - Echo.")-1)+"|")
        print("| ctxt - Create .txt file."+" "*(80 - len("| ctxt - Create .txt file.")-1)+"|")
        print("| speech2txt - Convert English Speech to Hindi"+" "*(80 - len("| speech2txt - Convert English Speech to Hindi")-1)+"|")
        print("| linkedin - Look at developers LinkedIn Account"+" "*(80 - len("| linkedin - Look at developers LinkedIn Account")-1)+"|")
        print("| github - Look at developers GitHub Account"+" "*(80 - len("| github - Look at developers GitHub Account")-1)+"|")
        print("| profile - Look at the developer Profile website"+" "*(80 - len("| profile - Look at the developer Profile website")-1)+"|")
        print("| wlink - Open Link"+" "*(80 - len("| wlink - Open Link")-1)+"|")
        print("| help - For more Information"+" "*(80 - len("| help - For more Information")-1)+"|")
        print("+"+"-"*78,end = "+")
    
start()

###############
# Main Program
###############


while True:
    
    command = input(">  ")
    ############################################
    # Defining the Functions below for NIleshell
    ############################################
   

    def largeodd():
        """
        Output: Largest odd number
        """
        num = [int(_) for _ in input("Enter Numbers in one line: ").split()]
        

        num.sort(reverse = True)

        for _ in num:
            if _%2 == 1:
                print(_,"is the largest Odd Number")
                break

    def date_time():
        """
        Output: Current System Date and Time.
        """
        date = str(datetime.now())
        print("Current System Date is:",date[8:10]+"-"+date[5:7]+"-"+date[:4])
        print("Current System Time is:",datetime.now().strftime("%I:%M:%S %p"))


    def linkedIn():
        """
        Output: Opens the LinkedIn Profile of the Developer on your Default browser.
        """
        webbrowser.open('https://www.linkedin.com/in/nilesh-ohol/')
        print("Look at your opened Default Browser")

    def clear():
        """
        Output: Clears the console.
        """
        os.system('clear')
        
    def pwd():
        """
        Output: Current Working Directory
        """
        print(os.getcwd())
    
    def help_():
        """
        Output: For Fun, A wise man once said, God Help those who help themselves' - Benjamin Franklin
        """
        quote = r"'A wise man once said, God Help those who help themselves' - Benjamin Franklin"
        print(quote)
    
    def dirch():
        """
        Input: Directory Location i.e. C:\\folder\\folder1
        Output: Changes the Working Directory.
        """
        try:
            print(f"Current Working Directory is {os.getcwd()}")
            os.chdir(input("Enter Directory Path: "))
            print(f"Directory changed to {os.getcwd()}")
        except:
            formats = r"C:\\Folder1\\Folder1.1\\Folder1.1.1"
            print("Operation Failed.\nDirectory should be in the format",format)
            if input("Would you like to try again? [y/n]") == "y":
                dirch()
    def github():
        """
         Output: Opens the GitHub Profile of the Developer on your Default browser.
        """
        webbrowser.open('https://github.com/nileshredz')
        print("Look at your opened Default Browser")
    
    def profile():
        """
        Output: Opens the Profile of the Developer on your Default browser.
        """
        webbrowser.open('http://nileshohol.me/')
        print("Look at your opened Default Browser")

    def wlink(link):
        """
        Input: Link of where you want to navigate.
        Output: Opens the link on your Default Browser.

        """
        webbrowser.open(link)
        print("Look at your opened Default Browser")
        
    def listdir():
        """
        Output: Shows Files and Folders in the current Directory.
        """
        print(f"Files and Directories in {os.getcwd()} are:\n")
        files = os.listdir()
        for i,_ in enumerate(files):
            print(i+1,_)
        print(f"\n\nTotal {len(files)} Files and Directory.")
    
    def create_txt(tname):
        """
        Input: Enter the text 
        Output: Create a text File in the Current Working Directory.
        """
        filename = open(tname+".txt","w+")
        newline_msg = r"To add space type \n"
        tab_msg =r"to add tab type \t "
        msg = input(newline_msg+"\n"+tab_msg+"\nWrite your text Below: \n")
        
        filename.write(msg)
        filename.close()
    
    def speechtxt():
        """
        Input: Speech from from your microphone in English.
        Output: Translate Speech into Text and transalate the text into Hindi.
        
        """
        r=sr.Recognizer()
    
        with sr. Microphone() as source:
            r.adjust_for_ambient_noise(source)
            translator=Translator(to_lang='hi')
        
            print("Say Something......")
        
            audio= r.listen(source)
            print('Recognizing Now....')
        
            #recognize speech using google:
        
            try:
                speech=r.recognize_google(audio)
                translation=translator.translate(speech)
                print('You have said: \n' +speech )
                print('Translation in Hindi: \n' +translation)
            
            
            except Exception as e:
                print('Error: ' +str(e))



    #######################################################
    # Calling the Function as per the request from the User
    #######################################################
    try:
        if command == "break":
            print("Be Patient. The window will close automatically")
            for _ in range(40):
                sleep(0.1)
            break
        elif command == "largeodd":
            largeodd()
        elif command == "dtime":
            date_time()
        elif command == "linkedin":
            linkedIn()
        elif command == "clear":
            clear()
            start()
        elif command == "pwd":
            pwd()
        elif command == "help":
            help_()
        elif command == "dirch":
            dirch()
        elif command == "github":
            github()
        elif command == "profile":
            profile()
        elif command == "listdir":
            listdir()
        elif command == "ctxt":
            create_txt(input("Create .txt file.\nEnter filename: "))
        elif command.split()[0] == "eline":
            print(*command.split()[1:],sep=" ")
        elif command.split()[0] == "wlink":
            wlink(command.split()[1])
        elif command == "speech2txt":
            speechtxt()
        else:
            print(command, "Command not found")
    except:
        print("Something went wrong.\nPlease try Again.")
        
    