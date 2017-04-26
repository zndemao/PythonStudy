import urllib.request as ur
import os
import re
import shutil



def url_open(url):
    req = ur.Request(url)
    ''' User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063'''
    # req.add_header('User-Agent',
    #                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36')
    req.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063')
    response = ur.urlopen(url)
    html = response.read()
    return html


def get_img_page(url):
    # print('url', url)
    '''<a class="imageLink image" href="http://www.jdlingyu.moe/28323/" 
    target="_blank"><img width="200" height="299.66" class="lazy" alt="浴衣日常" 
    src="http://www.jdlingyu.moe/wp-content/uploads/thumbnail/2017-04-19_21-18-20_200.jpg" 
    oriheight="299.66666666667"><span class="bg">浴衣日常</span></a>"'''
    html_page = url_open(url)
    html_page = html_page.decode('utf-8')
    # print(html_page)
    # p = r'href="(http://www.jdlingyu.moe/[\d]+/)"'
    p = r'</span></span></a> <a href="(http://www.jdlingyu.moe/[\d]+/)"'
    page_address = re.findall(p, html_page)
    # for each in page_address:
    #     print(each)
    return page_address


def get_img_address(html):
    html = html.decode('utf-8')
    '''class="phzoom" href="http://www.jdlingyu.moe/wp-content/uploads/2016/02/2017-04-18_21-42-40.jpg'''
    p = r'href="([^"]+\.jpg)'
    img_address = re.findall(p, html)
    # for each in img_address:
    #     print(each)
    return img_address


def save_img(folder, address):
    for each in address:
        print('保存图片',each)
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)


def download(url=r'http://www.jdlingyu.moe/', pages=10):
    # 创建文件夹
    address=os.getcwd()
    folder=address+"/小姐姐"
    if os.path.exists(folder):  # 如果文件夹不存在，就创建
        # os.removedirs(folder)
        rmtree = shutil.rmtree(folder)
        # print(rmtree)
    os.mkdir(folder)
    os.chdir(folder)

    print('file end')
    # 访问网站
    # for page in range(1,2):# 默认访问10页
    # url = r'http://www.jdlingyu.moe/page/'+pages+1+'/'

    for i in range(1, pages + 1):
        # print(url+"page/%d/" % i)
        img_page = get_img_page(url+"page/%d/" % i)
        for each_page in img_page:
            print('图片所在页',each_page)
            html = url_open(each_page)
            address = get_img_address(html)
            save_img(folder, address)
            # 获取图片的所在页面for each_url in img_page:
            #     html = url_open(each_url)
            #     # print(html)
            #     # 抓取图片地址
            #     address = get_img_address(html)
            #     save_img(folder, address)
            #


if __name__ == '__main__':
    download(pages=2)
