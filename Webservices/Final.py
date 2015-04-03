import twitter, datetime, urllib2

#Amy Permata Twitter
user = 463503640
file = open("secret.txt")
cred = file.readline().strip().split(',')
api = twitter.Api(consumer_key=cred[0],consumer_secret=cred[1],
                  access_token_key=cred[2],access_token_secret=cred[3])
statuses = api.GetUserTimeline(user)

#Read Current Session
file = open("C:\Users\user\AppData\Local\Google\Chrome\User Data\Profile 1\Current Session",'r')
data = file.read()

#Find URL
startUrl = data.rfind("http")
endUrl = data.find(chr(0), startUrl)
url = data[startUrl:endUrl]
print(url)

#Find Page Title
readhtml = urllib2.urlopen(url)
thePage = readhtml.read()
theTitle = thePage[thePage.index('<title'):thePage.index('</title>')]
theTitle = theTitle.replace('<title>','')
print("The page title is : " + theTitle.strip()) 
print("\nHey! Let's take a look " + theTitle.strip() + " on " + url)


#Post to Twitter
timestamp = datetime.datetime.utcnow()
response = api.PostUpdate("Hey! Let's take a look " + theTitle.strip() + " on " + url)
print("New Tweet Updated!")


