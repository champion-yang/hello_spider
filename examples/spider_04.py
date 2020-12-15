import requests
from lxml import etree
import os

def request_demo(url):
    response = requests.get(url)
    ret = response.text

    return ret

def parse(text):
    html = etree.HTML(text)
    a_lst = html.xpath('//li/a')
    all_data = [(i.find('img'), i.xpath('span/span/text()')) for i in a_lst]
    # 对空值做处理
    res = []
    for i in all_data:
        if i[0] is not None and i[1]:
            res.append((i[0].get('src'), i[1][0]))

    return res

def save_img(img_url, name):
    assert isinstance(img_url, str), '图片路径必须是字符串'
    if not os.path.exists('./static'):  # 判断根目录是否存在
        os.mkdir(root)
    path = './static/' + name + ".jpg"  # 保存的地址
    try:
        r = requests.get(img_url)
        with open(path, 'wb') as f:  # 'wb'以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
            f.write(r.content)  # content返回二进制数据，所以使用'wb'
            f.close()
            print("文件保存成功")
    except:
        print("爬取失败")

def main():
    url = 'https://image.so.com/'
    text = request_demo(url)
    res_list = parse(text)
    for i in res_list:
        save_img(i[0], i[1])

    return None

if __name__ == "__main__":
    main()