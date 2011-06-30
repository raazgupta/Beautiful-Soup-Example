#For all questions, please refer to - http://www.crummy.com/software/BeautifulSoup/documentation.html

#import the library used to query a website
import urllib2
#import the Beautiful soup functions to parse the data returned from the chosen website
from BeautifulSoup import BeautifulSoup

#This is the url that will be queried. You can change this to something else
#Of course if it is changed so will the structure of the returned html
#Hence the parse logic will beed to be modified
urlStr = "http://news.google.com.sg/nwshp?ie=UTF-8&hl=en&tab=in&ar=1309403034"

print "Querying" + urlStr
print

#Querying the website and returning the html to 'page'
page = urllib2.urlopen(urlStr)

#Parsing the html in 'page', and storing it in Beautiful Soup format
soup = BeautifulSoup(page)

#Now that we have it nicely stored. We can query for this.
#For instance all the Titles of news stories in the html are as follows
#<span class="titletext">blah blah blah</span>
#So if we find all 'span' with class="titletext" and extract it's contents, we have 
#all the news headings in the site. You can check the source html on a website by 
#right clicking in the browser and saying 'View Source'. Then search.
#Anyways back to the python magic

allTitles = soup.findAll('span', attrs = { 'class' : 'titletext' })

#Now we loop through each title and print out the text contents
for title in allTitles:
	print title.contents[0].strip()
	print
	
#That's it! We can keep running this every time the main news site changes. It will
#print out all title, together with the updated ones. Of course you could also store these
#in a file and do other fun stuff with it. All you need is an imagination!

#IMPORANT: Another thing I realized when I looked at the results. These results are 
#obtained when you are logged out of google and query news. It is a different story if 
#you are logged in to the browser, as cookies then need to be factored in. Also there is
#a lot more cleaning up of the query that can be done. Python is good at doing this stuff
#though. Google your heart out and use Regular Expressions

#The End :)

