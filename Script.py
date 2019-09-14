import requests
import urllib
from selenium import webdriver

tiktokurllist =[]
likevideolist=[]
tiktokidlist=[]
gecko='chromedriver'

driver = webdriver.Chrome(executable_path=gecko)
print("Reading Url Links......")

with open('links.txt','r') as f:
    links = f.readlines()
    for l in links:
        if "tiktok" in l:
            tiktokurllist.append(l)
        if "like-video" in l or "likee" in l:
            likevideolist.append(l)

with open("tiktokids.txt",'r') as f:
    ids = f.readlines()
    for i in ids:
        tiktokidlist.append(i)


print("done.")
# print(tiktokurllist, likevideolist)
name = 1

def download(link,name):
    urllib.request.urlretrieve(link,name)
    print(f"{name} downloaded Successfully!\n")

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'}
for link in likevideolist:
    try:
        driver.get(link)
        video = driver.find_element_by_tag_name('video')
        videolink = video.get_attribute('src')
        print(f"Downloading video from --> {videolink} \n")
        download(videolink, f"likeevideo{name}.mp4")
        name+=1
    except:
        print("\nLike Video not Found!\n")
driver.quit()

for link in tiktokurllist:
    url = link
    source = requests.get(url, headers = headers)
    # print(source)
    if source.status_code == 200:
        newurl = source.url
        getid = newurl.split('/')[5].split('?')[0]
        videolink = 'https://tiktok.com/node/video/playwm?id='+getid
        video = requests.get(videolink, headers=headers)
        print(f"Downloading video from --> {videolink} \n")
        download(video.url, f"tiktokvideo{name}.mp4")
        name+=1
    else:
        print("\nTikTok Video not Found!\n")

for ids in tiktokidlist:
    videolink = 'https://tiktok.com/node/video/playwm?id='+ids
    try:
        videolink = requests.get(videolink, headers=headers)
        print(f"Downloading video from --> {videolink} \n")
        download(video.url, f"tiktokvideo{name}.mp4")
        name+=1
    except:
        print("Some Problem with TikTok ID\n")




