import os, sys, tty, time, termios, subprocess

def showSlide(number):
    os.system("clear")
    count = 0
    print("[" + str(number+1) + "/" + str(len(slides)) + "]"),
    for line in slides[number]:
        if((len(line)>0) and (line[0] == '&')): print("\033[32m" + line[1:] + "\033[0m")
        elif((len(line)>0) and (line[0] == '%')): print("\033[94m" + line[1:] + "\033[0m")
        elif((len(line)>0) and (line[0] == '>')):
            if(count<revealsRevealed):
                print(line[1:])
                count+=1
            else: print(">")
        else: print(line)

def runSampleCode(number):
    global slides
    os.system("clear")
    allCode = ""
    for line in slides[number]:
        if((len(line)>0) and (line[0] == '&')): allCode = allCode + "\n" + line[1:]
    if(len(allCode) > 0):
        print("\033[32m" + allCode + "\033[0m")
        print("\033[33m")
        # Need the "if True" bit in case the sample code is indented !
        exec "if True:\n" + allCode
        print("\033[0m")
        print("Press any key to return to slides"),
        tty.setraw(sys.stdin.fileno())
        sys.stdin.read(1)
        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old_settings)
    else:
        showSlide(number)
        print("No code samples to run !")
        time.sleep(1.5)

def openAllURLs(number):
    global slides
    for line in slides[number]:
        if((len(line)>0) and (line[0] == '%')): subprocess.Popen(["open", line[1:].strip()])

def revealOrNextSlide():
    global revealsRevealed
    global slidePointer
    totalReveals = 0
    for line in slides[slidePointer]:
        if((len(line)>0) and (line[0] == '>')): totalReveals+=1
    if(revealsRevealed < totalReveals): revealsRevealed+=1
    else:
        slidePointer+=1
        revealsRevealed = 0
        if(slidePointer>=len(slides)): slidePointer = len(slides)-1
    showSlide(slidePointer)

def loadSlides():
    global slides
    pointer = 0
    file = open(sys.argv[1],'r')
    slides = [[]]
    for line in file:
        if(line[0] == "~"): 
            pointer+=1
            slides.append([])
        else: 
            text = line[:-1]
            text = text.replace("<R>","\033[91m")
            text = text.replace("<B>","\033[1m")
            text = text.replace("<U>","\033[4m")
            text = text.replace("<?>","")
            text = text.replace("</R>","\033[0m")
            text = text.replace("</B>","\033[0m")
            text = text.replace("</U>","\033[0m")
            text = text.replace("</?>","")
            slides[pointer].append(text)
    file.close()

def close():
    os.system("clear")
    sys.exit()

old_settings = termios.tcgetattr(sys.stdin.fileno())
print("\033[0m")
loadSlides()
slidePointer = 0
revealsRevealed = 0

while True:
    showSlide(slidePointer)
    tty.setraw(sys.stdin.fileno())
    command = sys.stdin.read(1)
    termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, old_settings)
    os.system("clear")
    if(command == 'q'): close()
    elif(command == 'r'): runSampleCode(slidePointer)
    elif(command == 'o'): openAllURLs(slidePointer)
    elif(command == 'l'): loadSlides()
    elif(command == ' '): revealOrNextSlide()
    elif(ord(command) == 65): slidePointer = 0
    elif(ord(command) == 66): slidePointer = len(slides)-1
    elif(ord(command) == 67): revealOrNextSlide()
    elif(ord(command) == 68): slidePointer-=1
    if(slidePointer<0): slidePointer = 0;


