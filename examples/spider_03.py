import os
import requests

def save_img(img_url, name):
    path = ''
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

if __name__ == '__main__':
    save_img('https://p.ssl.qhimg.com/dmfd/400_300_/t01c0f0829b497a02da.png', '女孩')