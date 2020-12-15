text = """
<!DOCTYPE html>
<html class="w3c">
<head></head>
<body>
    <header></header>
    <div id="body">

        <div class="block">
            <section id="bd_focus">
                <ul>
                    <li class="cur">
                        <a href="/z?ch=beauty&t1=595&src=banner_beauty&gid=" target="_blank">
                            <img src="https://p.ssl.qhimg.com/dmfd/400_300_/t01c0f0829b497a02da.png" alt="" />
                            <span class="content">
                                <span class="title">清新美女</span>
                            </span>
                        </a>
                    </li>
                    <li class="">
                        <a href="/z?ch=design&src=banner_design#/&gid=" target="_blank">
                            <img src="https://p.ssl.qhimg.com/dmfd/400_300_/t0115d9c0bbb606dfb4.jpg" alt="" />
                            <span
                                class="content">
                                <span class="title">设计素材</span>
                            </span>
                        </a>
                    </li>
                </ul>
            </section>
        </div>
    </div>
    <footer></footer>
</body>

</html>
"""
import requests
from lxml import etree

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


if __name__ == "__main__":
    url = 'https://image.so.com/'
    text = request_demo(url)
    res = parse(text)

    print(res)
