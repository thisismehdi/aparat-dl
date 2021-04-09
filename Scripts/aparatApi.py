import youtube_dl
import requests
from bs4 import BeautifulSoup as bs
import Scripts.aparatLinksFinder as a


class AparatDlApi():
    '''
     an api for download videos from aparat.com
    Methods
    -------
    singleVideo(link)
                    Download Single video
    playList(link)
                    Download a play-list in order
    wholeChannel(link)
                    Download the whole Channel
    '''

    @staticmethod
    def singleVideo(link, res='720p'):
        '''
        Download Single video
        :param str link
        '''

        src = requests.get(link)
        soup = bs(src.text, "html.parser")
        name = soup.title.string
        name = name.replace("\n", " ")
        thelink = a.dllink_extractor(link, res)
        ydl_opts = {
            'outtmpl': name + ".mp4",
            'retries': 999,
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.extract_info(
                thelink,
                download=True)

    @staticmethod
    def playList(link, res='720p'):
        '''
        Download a play-list in order
        :param str link
        '''
        # grab the palylist name
        src = requests.get(link)
        soup = bs(src.text, "html.parser")
        atag = soup.find_all('span', attrs={'class': 'd-in v-m'})
        atag = list(atag)
        if len(atag) == 0:
            raise Exception("This is not a play list link ")
        for i in atag:
            temp = i
        temp = list(temp)
        pdir = temp[0]
        links = a.vlink_extractor(link)
        l2 = list(links)
        for j in links:
            # grab name of videos
            src = requests.get(j)
            soup = bs(src.text, "html.parser")
            name = soup.title.string
            name = name.replace("\n", " ")
            # grab links of videos
            thelink = a.dllink_extractor(j, res)

            # download videos one by one
            orderoflist = l2.index(j)
            orderoflist += 1
            fname = str(orderoflist) + " -" + name + ".mp4"
            ydl_opts = {
                'outtmpl': pdir + "/" + fname,
                'retries': 999,
            }

            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.extract_info(
                    thelink,
                    download=True)

    @staticmethod
    def selectFromPlayList(link, start=0, end=100, res='720p'):
        '''
        Download videos by selection on a play-list
        :param str link
        :param start int
        "param end int
        '''
        # grab the play-list name
        src = requests.get(link)
        soup = bs(src.text, "html.parser")
        atag = soup.find_all('span', attrs={'class': 'd-in v-m'})
        atag = list(atag)
        if len(atag) == 0:
            raise Exception("This is not a play list link ")
        for i in atag:
            temp = i
        temp = list(temp)
        pdir = temp[0]
        links = list(a.vlink_extractor(link))
        links.insert(0, "test")
        end += 1
        try:
            links2 = links[start:end]
        except Exception as E:
            raise E
        for i in range(start, end):
            src = requests.get(links[i])
            soup = bs(src.text, "html.parser")
            name = soup.title.string
            name = name.replace("\n", " ")
            # grab links of videos
            thelink = a.dllink_extractor(links[i], res)
            # download videos one by one
            fname = str(i) + " -" + name + ".mp4"
            ydl_opts = {
                'outtmpl': pdir + "/" + fname,
                'retries': 999,
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.extract_info(
                    thelink,
                    download=True)

    @staticmethod
    def fromFile(ifile, res='720p'):
        '''
            donwlaod single video from file unlimited!
            
    
        '''

        tlinks = []
        with open(ifile) as f:
            tlinks = [line.rstrip() for line in f]
        j = 1
        for i in tlinks:
            src = requests.get(i)
            soup = bs(src.text, "html.parser")
            name = str(j) + " - " + soup.title.string
            name = name.replace("\n", " ")
            thelink = a.dllink_extractor(i, res)
            ydl_opts = {
                'outtmpl': name + ".mp4",
                'retries': 999,
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.extract_info(
                    thelink,
                    download=True)
            j += 1

    @staticmethod
    def fromFileForList(ifile, res="720p"):
        '''
            donwlaod single video from file unlimited!
            

        '''
        tlinks = []
        with open(ifile) as f:
            tlinks = [line.rstrip() for line in f]
        for i in tlinks:
            AparatDlApi.playList(i, res)
