

# pip install urlextract

from urlextract import URLExtract 

x = '''My favorite website is technicallyripped.com.
I also like www.google.com because I can google 
anything! My favorite subreddit is 
https://www.reddit.com/r/python . 
Visit info.gov for more info!'''

ext = URLExtract()

websites = ext.find_urls(x)
print(websites)















