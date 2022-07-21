import requests
import json


def get_html_contents(url):
    # get url contents and cast as str
    res = requests.get(url)
    return str(res.content)

def grab_data(start, end, contents):
    # find start and end by iter over string and grab value
    i = 0
    while contents[i:i+len(start)] != start:
        i+=1
    s = i

    while contents[i:i+len(end)] != end:
        i += 1
    e = i

    price = float(contents[s+len(start):e])
    return price

def main(city='stadt-bochum'):
    url = 'https://www.clever-tanken.de/tankstellen/' + city
    res = get_html_contents(url)

    start_point = '<div class="strong-title text-color-white-gray">'
    end_point = '<sup>0</sup></div>'

    price = grab_data(start_point, end_point, res)
    print(city, price)
    return price

if __name__ == '__main__':
    main()
