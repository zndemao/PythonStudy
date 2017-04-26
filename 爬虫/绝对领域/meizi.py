import urllib.request
import os


def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()

    return html


def get_page(url):
    '''获得页面内的图片地址'''
    html = url_open(url).decode('utf-8')

    a = html.find('current-comment-page') + 23
    b = html.find(']', a)

    print(html[a:b])

    # 元祖
    return html[a:b]


def find_imgs(url):
    '''获取这http://jandan.net/ooxx/page-1293#comments里面的图片'''
    html = url_open(url).decode('utf-8')
    img_addrs = []
    a = html.find('img src=')

    while a != -1:
        b = html.find('.jpg', a, a + 255)
        if b != -1:
            img_addrs.append("http:" + html[a + 9:b + 4])
        else:
            b = a + 9

        a = html.find("img src=", b)

    for each in img_addrs:
        print(each)

    return img_addrs


def save_imgs(folder, img_addrs):
    '''将找到的图片保存起来'''
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)


def download_mm(folder='ooxx', pages=10):
    print(os.getcwd())
    os.mkdir(folder)
    os.chdir(folder)
    print('文件夹创建完成')
    url = 'http://jandan.net/ooxx/'
    page_num = get_page(url)
    page_num = 1293
    for i in range(pages):
        page_num -= 1
        '''http://jandan.net/ooxx/page-1293#comments'''
        page_url = url + 'page-' + str(page_num) + '#comments'
        print(page_url)
        img_addrs = find_imgs(page_url)
        save_imgs(folder, img_addrs)


if __name__ == "__main__":
    download_mm()
