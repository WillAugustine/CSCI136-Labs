# 
# Author: Will Augustine
#   Credit: Doug Galarus
# 
# Description: Given an URL, traverse through the HTML of the webpage,
#   and find all links using a regular expression. Then, add all links,
#   up to a certain recursion depth, in the inputted URL to a text file
#

# Imports
import urllib.request # For reading html page from link
import re # For finding all strings matching strings using regular expression
import sys # For reading command line input

#
# Description: Crawls through inputted webpage to inputted depth, pulling
#   all links from HTML using regular expression
# 
# Inputs:
#   int depth: Maximum recursion depth
#   string link
#   dictionary linkDictionary: Dictionary of links that have been visited
# 
# Outputs:
#   None
#
def crawl(depth, link, linkDictionary):
        if link in linkDictionary: # If the link has already been visited
            linkDictionary[link] += 1 # Increment the number of times the link was referenced 
            return # Do not visit an already visited link
        
        linkDictionary[link] = 1 # Set the number of link references to 1

        if depth < 1: # If the maximum depth is exceeded
            return # Stop the recursion
        
        try:
            page = urllib.request.urlopen(link) # Get the page at the link
            html = str(page.read()) # Get the HTML of the link
            linkReferences = re.findall("href=\"[^\"]*\"", html) # Find all links in the HTML
            for hrefLink in linkReferences:
                currLink = hrefLink[6:-1] # Removes 'href=' and quotes around link
                if (currLink[:4] == "http"): # If the current link is a whole path (begins with 'http')
                    crawl(depth-1, currLink, linkDictionary)
        except: # If there is an error reading a webpage
            pass # Move on
 
    


if __name__ == "__main__":
    
    try:
        startingLink = str(sys.argv[1]) # Get starting link from command line argument
        depth = int(sys.argv[2]) # Get max depth from command line argument
    except: # If there is an issue reading the command line arguments
        print("USAGE: python Crawler.py link depth") # Tell the user how to call Crawler.py
        exit() # Do not continue
    
    linkDictionary = {} # Creates global variable for dictionary of links
    
    crawl(depth, startingLink, linkDictionary) # Runs the crawl method
    
    # Opens links.txt with write permissions
    #   If file does not exist, it creates a file named 'links.txt'
    linkFile = open("links.txt", "w")

    # For each link (key) and number of occurances (value) in the dictionary of links
    for link, occurances in linkDictionary.items():
        # Write link and number of occurances to text file
        linkFile.write(str(occurances) + " " + link + "\n")
        
    linkFile.close() # Close the file (saves what you wrote)



