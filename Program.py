import sys
import time
import random

#These are the empty lists
key= [];
converted= [];
samplefile= [];
decryptoffset= [];
decryptlist= [];
decryptedfile= [];

#These are the procedures of the program
#The encrypt procedure will alow the user to encrypt a message
def encrypt():
    #This allows the user to enter the name of the file and the message will be read and displayed to the user. If an error occurs, it will display that it was unable to open it.
    print ("Enter the name of the file:")
    print ("(It should end in '.txt')")
    file= input()
    try:
        createfile= open (file, "r")
        text= createfile.readline()
        print("")
        print ("The file's message:",text)
        createfile.close()
    except IOError:
        print ("Unable to open file")
    time.sleep (5)

    #This will count the length of characters in the file.
    samplefile= text
    length= len(samplefile)
    
    #This will display 8 randomly generated numbers
    print ("\n")
    print ("Here are your 8 randomly generated numbers:")
    time.sleep(1)

    for number in range(8):
        randomnumber=random.randint(33,126)
        time.sleep(1)
        print (randomnumber)
        asciicharacter= chr(randomnumber)
        key.append(asciicharacter)

    #This displays the key
    print("")
    print ("Your 8 character key is:")
    time.sleep(1)
    print("(Make sure you take a note of this!)")
    time.sleep(1)
    print (key)

    #This calculates the offset factor
    total=0
    for asciicharacter in key:
        asciinumber= ord(asciicharacter)
        number= int(asciinumber)
        total= total+number
        
    average= total/8
    average= int(average)
    result= average-32
    time.sleep(2)
    print("")
    print ("The offset factor is:")
    time.sleep(1)
    print(result)
    time.sleep(1)

    #This encrypts the text file
    for n in range (0,length):
        filecharacter= ord(samplefile[n])
        final= filecharacter+result
        if final > 126:
            subtract= final-94
            subtract= chr(subtract)
            converted.append(subtract)
        else:
            final= chr(final)
            converted.append(final)
    
    #This displays the encrypted message onto the screen
    print("")
    print ("Encrypted message:")
    print (converted)

    #This joins the characters into a string
    string= ''.join(converted)
    print(converted)
    
    #This saves it into a new text file
    while True:
        try:
            print("")
            print("Please enter a name to save the new file:")
            print("(It must end in .txt )")
            filename= input()
            savedfile= open(filename,"w")
            savedfile.write(string)
            savedfile.close()
            print("The file has been saved")
            break
        except:
            print("Unable to save the file. Please try again")
    
#The decrypt procedure will allow the user to decrypt a text file.
def decrypt():
    #This opens the file with the encrypted message.
    print ("Enter the name of the file you want to be decrypted:")
    print("(It must end in .txt )")
    filename=input()
    while True:
        try:
            createfile= open (filename, "r")
            filename= createfile.readline()
            print("")
            print ("The file's message:",filename)
            createfile.close()
            break
        except IOError:
            print ("Unable to open file")

    #This asks the user to enter the characters of the eight character key.
    #This will allow us to work out the offset factor.
    offset= 0
    for n in range (8):
        print("")
        print("Please enter the",n+1,"character of the key:")
        decryptkey= input()
        converted= ord(decryptkey)
        converted= int(converted)
        decryptoffset.append(decryptkey)
        offset= offset + converted

    #This calculates the offset factor.
    offsetfactor= offset/8
    offsetfactor= int(offsetfactor)
    result= offsetfactor-32

    #This displays the key and the offset factor.
    print("")
    print("This was your eight character key:")
    print (decryptoffset)
    print("")
    print("This was your offset factor:")
    print (result)

    length= len(filename)

    #This decrypts the file's characters.
    for n in range (0,length):
        filecharacter= ord(filename[n])
        filecharacter= filecharacter-result
        if filecharacter < 33:
            filecharacter= filecharacter+94
            filecharacter= chr(filecharacter)
            decryptlist.append(filecharacter)
        else:
            filecharacter= chr(filecharacter)
            decryptlist.append(filecharacter)

    #This joins the list and displasy the file's decrypted message
    decryptedfile= ''.join(decryptlist)
    print("")
    print("This is the decrypted message:")
    print(decryptedfile)

    
#The end procedure will display an error message and then exit the program.
def end():
    print ("We have encountered an error")
    print ("Now exiting the program...")
    sys.exit ()

#This is the welcome message for the user
def welcome():
    print ("Welcome to TC's EnDecrypt program")
    time.sleep (2)
    print ("This program will allow you to either Encrypt or Decrypt a message.")
    time.sleep (3)
    print ("It can be used for any types of messages which are in English.")
    time.sleep (3)
    print ("Psst.. Perfect for when you're feeling sneaky!")
    time.sleep (3)

#This is the procedure for the main menu.
def menu():
    print ("\n")
    #This will display a header which will make the menu look asthetically pleasing.   
    print ("*.*.*.*.*.*.*.*.*.*.*.*")
    #Outputs 'Main menu' on the screen so the user knows the choices
    print ("Main menu:")
    print ("")
    print ("1= Encrypt message")
    print ("")
    print ("2= Decrypt message")
    print ("")
    print ("3= Exit the program") 
    print ("*.*.*.*.*.*.*.*.*.*.*.*")
    print ("\n")
    print ("Please enter your choice:")
    #This will allow the user to input their choice as an integer
    choice= input ()
    choice= int(choice)

    #This returns the choice of choosing something else from the menu to the user
    return choice

welcome ()
choice= menu ()

while choice <4:
    #If the user chose 'Encrypt message', then it will follow the procedures of encrypt () which have been described at the top.
    if choice==1:
       encrypt ()
       choice= menu()
    #If the user chose 'Decrypt message', then it will follow the procedures of decrypt () which have been described at the top.
    elif choice==2:
        decrypt ()
        choice= menu()
    #If the user chose 'Exit program', then it will follow the procedures of end () by outputting
    elif choice==3:
        end()
    
    #If something doesn't go to plan or if the user inputted incorrect information, then it will output an error message and exit the program.
    else:
        end()
