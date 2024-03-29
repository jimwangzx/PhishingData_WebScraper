# Grace Ciambrone
# Last updated Feb 21 2022

    # TO DO:
    # Make program more modular by breaking down into smaller functions

import os
import urllib.request     # Module for reading from the web
import re                 # Regular Expressions


# Collect data from Arizona State University
def getASUData():

    # Obtain number of pages to scrape
    asu_url = "https://security.arizona.edu/phishing_alerts"
    request = urllib.request.Request(asu_url)
    source = urllib.request.urlopen(request)
    page = source.read()
    text = page.decode()
    
    corpus = []
    
    total_pages = int(re.findall(r"page=(.*)\">last", text)[0])
    print(f"Total pages to be scraped: {total_pages}\n")
    
    # Request each page and scrape data
    for i in range(1, total_pages+1):
        url = asu_url + "?page=" + str(i)
        r = urllib.request.Request(url)
        s = urllib.request.urlopen(r)
        print(f"\tRetrieved page {i}")
        t = s.read().decode()
        email_subject = re.findall(r"/phishing-alert/.*\".*\d{4}.([^<]*)<", t)
        corpus += email_subject
    
    print(f"\nLength of corpus: {len(corpus)}")
    print(f"\nContents of corpus:\n{corpus}")
    
    # Create a corpus of text files
    home_path = "/home/grace/HLT_LAB"
    dir = "ArizonaStateUniversity"
    dir_path = os.path.join(home_path, dir)
    if not os.path.isdir(dir_path): os.mkdir(dir_path)
    
    i = 0
    for subject in corpus:
        i += 1
        id = "{:05d}".format(i) + ".txt"
        p = os.path.join(dir_path, id)
    
        with open(p, 'w') as f:
            f.write(subject)
    
    # Check contents of directory
    print("\nContents of directory:")
    print(os.listdir(dir_path))

# Collect data from University of North Carolina Chapil Hill
def getUNCData():

    # Obtain number of pages to scrape
    unc_url = "https://its.unc.edu/phish-alerts/?wpv_view_count=119932&wpv_post_search=&wpv_paged"
    request = urllib.request.Request(unc_url)
    source = urllib.request.urlopen(request)
    page = source.read()
    text = page.decode()
    
    corpus = []
    
    total_pages = int(re.findall(r"data-maxpages=\"(\d{3})\"", text)[0])
    print(f"Total pages to be scraped: {total_pages}\n")

    # Request each page and scrape data
    for i in range(1, total_pages+1):
        url = unc_url + "=" + str(i)
        r = urllib.request.Request(url)
        s = urllib.request.urlopen(r)
        print(f"\tRetrieved page {i}")
        t = s.read().decode()
        email_subject = re.findall(r"Subject:.(.*)\n", t)
        corpus += email_subject
    
    print(f"\nLength of corpus: {len(corpus)}")
    print(f"\nContents of corpus:\n{corpus}")
    
    # Create a corpus of text files
    home_path = "/home/grace/HLT_LAB"
    dir = "UniversityOfNorthCarolinaChapilHill"
    dir_path = os.path.join(home_path, dir)
    if not os.path.isdir(dir_path): os.mkdir(dir_path)
    
    i = 0
    for subject in corpus:
        i += 1
        id = "{:05d}".format(i) + ".txt"
        p = os.path.join(dir_path, id)
    
        with open(p, 'w') as f:
            f.write(subject)
    
    # Check contents of directory
    print("\nContents of directory:")
    print(os.listdir(dir_path))

def main():
    getASUData()
    getUNCData()

main()