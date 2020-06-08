# VIDEO DOWNLOADER
from pytube import YouTube

print('WELCOME TO THE VIDEO DOWNLOADER!')
print('-' * 30)


choice = str(input('''Please, choose an option below:
[1] Download a list of videos from a .txt document
[2] Download a video from an URL address

Type down here your option: ''').strip())   # Choosing between download from a .txt file or URL address


choice_dir = str(input('Do you want to save your videos in a specific folder? [y/n] ').strip().upper())
# Choosing the folder to store the downloaded videos

if choice_dir in 'Y':
    directory = str(input('Type down the new directory: '))

else:
    directory = 'C:\\Users\\Patrik\\Desktop\\Trabalho\\Python\\Experimentations\\video_downloader'


if choice in '1':   # Downloading from a .txt file
    counter = 0
    video_list = open('video_download_list.txt', 'r')
    for i in video_list:
        try:
            address = YouTube(i)
            counter += 1
            video = address.streams.first()
            video.download(directory)
            print(f'Download {counter}º video complete!')
        except:
            print('Download failed for ', i)


elif choice in '2':     # Downloading from an URL address
    x = str(input('Type down the URL of the video your want to download: ').strip())
    try:
        address = YouTube(x)
        video = address.streams.first()
        video.download(directory)
        print('Download completed.')
    except:
        print('Download failed.')


else:   # Wrong download option
    print('Invalid option!')
