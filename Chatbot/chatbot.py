# Knights to was "ni" video reference
# https://www.youtube.com/watch?v=zIV4poUZAQo

file = open("stop-words.txt")
stopwords = file.readlines()

def removeStopwords(message):
    for word in stopwords:
        next = word.strip()
        message = message.replace(" " + next + " "," ")
    return message

while True:
    input = raw_input("Alice: Hello there, who are you?: ")
    input = " " + input + " "
    filtered = removeStopwords(input)
    filtered = filtered.replace(" name ", " ")
    filtered = filtered.replace(" called ", " ")
    print("Alice: Hello " + filtered)

    input = raw_input("Alice: Where do you live?: ")
    input = " " + input + " "
    filtered = removeStopwords(input)
    print("Alice: Wow, I heard, " + filtered + "is a very nice country." )

    input =raw_input("How is the weather: ")
    input = " " + input + " "
    filtered = removeStopwords(input)
    filtered = filtered.replace("weather","")
    varWeather = filtered
    if varWeather == 'sunny':
        print ("Very nice " + filtered.strip() +" day")
    elif varWeather == 'cold':
        print ("Very nice " + filtered.strip() +" day")
    elif varWeather == 'winter':
        print ("Very nice " + filtered.strip() +" day")
    elif varWeather == '':
        print ("Very nice " + filtered.strip() +" day")
    else:
        print ("Perfect!")

    

    

    

    
