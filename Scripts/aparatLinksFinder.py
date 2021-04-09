import requests
from bs4 import BeautifulSoup as bs


def reclister(link):
    """
    
        find any QUALITIE

    """
    resolutions = ['1080p', '720p', '480p', '360p', '240p', '144p']

    src = requests.get(link)
    soup = bs(src.text, "html.parser")
    links = []
    for i in soup.find_all("a"):
        k = str(i).split("href")[1].split('"')
        for j in k:
            if j.count("http") and j.count("cdn"):
                links.append(j)
    link_list = {}
    for i in links:
        for j in resolutions:
            if i.count(j):
                link_list[j] = i
    ordered_res = list(link_list.keys())
    ordered_res.sort()
    return ordered_res


def dllink_extractor(link, res='720p'):
    '''
    find the best quality that available and return it
    :param str link
    :reutrn: the best quality
    :rtype: str
    '''

    resolutions = ['1080p', '720p', '480p', '360p', '240p', '144p']

    src = requests.get(link)
    soup = bs(src.text, "html.parser")
    links = []
    for i in soup.find_all("a"):
        k = str(i).split("href")[1].split('"')
        for j in k:
            if j.count("http") and j.count("cdn"):
                links.append(j)
    link_list = {}
    for i in links:
        for j in resolutions:
            if i.count(j):
                link_list[j] = i
    ordered_res = list(link_list.keys())
    ordered_res.sort()

    if res in link_list:
        return link_list.get(res)
    else:
        print(link_list)
        res = list(link_list)[-1]
        return link_list.get(res)


def vlink_extractor(link):
    '''
    grab all links of all videos in play-list
    :param str link
    :return: all links of page in play-list
    :rtype: list
    '''
    src = requests.get(link)
    soup = bs(src.text, "html.parser")
    video_links = []
    for i in str(soup.find_all(attrs={'class': 'playlist-body'})).split('"'):
        if i.count("/v/"):
            video_links.append(i)
    links = []
    for i in range(0, len(video_links), 2):
        links.append(
            "https://aparat.com{}".format(video_links[i].split("/%")[0]))
    # links of all videos in play-list
    links = dict.fromkeys(links).keys()
    return links
