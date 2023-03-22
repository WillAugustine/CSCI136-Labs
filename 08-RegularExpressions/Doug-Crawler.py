import urllib.request
import re 
import sys

def crawl(depth, link, dctlinks):
        if link in dctlinks:
            dctlinks[link] = dctlinks[link] + 1
            return
        else:
            dctlinks[link] = 1
            #print(link)
            if depth < 1:
                return
            else:
                try:
                    page = urllib.request.urlopen(link)
                    html = str(page.read())
                    matches = re.findall("href=\"[^\"]*\"",html)
                    for m in matches:
                        path = m[6:-1]
                        if (path[:4] == "http"):
                            crawl(depth-1, path, dctlinks)
                except:
                    pass
    
 
def main():
    
    try:
        startlink = str(sys.argv[1])
        depth = int(sys.argv[2])
    except:
        print("USAGE: python Crawler.py link depth")
        return
    
    dctlinks = {}
    #crawl(1, "https://www.mtech.edu/", dctlinks)
    crawl(depth, startlink, dctlinks)
    
    
    f = open("links.txt", "w") #Opens a links.txt file.

    for l in dctlinks:
        #print(dctlinks[l], l)
        f.write(str(dctlinks[l]) + " " + l + "\n")
        
    f.close()


if __name__ == "__main__":
    main()




