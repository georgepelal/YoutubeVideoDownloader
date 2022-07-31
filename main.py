#pip install pytube
from pytube import YouTube

print("Welcome to YoutubeVideoDownloader")

def downloader():
    link=input("Enter video's link:")
    #print video details
    video=YouTube(link)
    print("name:",video.title)
    print("by:",video.author)
    print("views",video.views)
    print("length:",video.length,"secs(",video.length/60,"mins)")
    #select download options(high or low resolution)
    res=input("If you want the video to download on low resolution type L else leave blank:").capitalize()
    if res=="L":
        video.streams.get_lowest_resolution().download()
    else:
        video.streams.get_highest_resolution().download()

    print("Your video was downloaded!")

    repeat=input("type E if you want to exit or leave blank to download another video:").capitalize()
    if repeat=="E":
        pass
    else:
        downloader()

downloader()
