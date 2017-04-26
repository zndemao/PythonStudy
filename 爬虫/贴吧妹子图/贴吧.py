import urllib.request as ur
import re


def open_url(url):
    req = ur.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
    page = ur.urlopen(url)
    html = page.read()
    # print(html)

    return html


def get_img(html):
    html = html.decode('utf-8')
    # < img
    # width = "560"
    # height = "747"
    # class ="BDE_Image" src="https://imgsa.baidu.com/forum/w%3D580/sign=aa042893d558ccbf1bbcb53229d9bcd4/82e96d600c338744f222ae5d550fd9f9d62aa07d.jpg" changedsize="true" pic_ext="jpeg" >
    '''https://imgsa.baidu.com/forum/w%3D580/sign=aa042893d558ccbf1bbcb53229d9bcd4/82e96d600c338744f222ae5d550fd9f9d62aa07d.jpg'''
    # p = r'<img width="560" height="747" class="BDE_Image" src="[^"]+\.jpg'
    # p = r'<img class="BDE_Image" src="[^"]+\.jpg'
    p = r'<img class="BDE_Image" src="([^"]+\.jpg)'
    imglist = re.findall(p, html)

    # for each in imglist:
    #     print(each)

    for each in imglist:
        filename = each.split('/')[-1]
        print(filename)
        ur.urlretrieve(each, filename, None)


if __name__ == '__main__':
    url = 'https://tieba.baidu.com/p/3563409202'
    get_img(open_url(url))
