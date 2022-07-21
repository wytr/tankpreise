import requests
import json


def get_html_contents(url):
    # get url contents and cast as str
    res = requests.get(url)
    return str(res.content)


def get_start(start, contents):
    # finds start point by iterating over html contents
    i = 0 
    while i < len(contents):
        i+=1
        if contents[i:i+len(start)] == start:
            break
    return i+len(start)

def get_end(end, contents):
    # finds endpoint after start point
    i = 0
    while i < len(contents):
        i += 1
        if contents[i:i+len(end)] == end:
            break
    return i

def grab_data(start, end, contents):
    # uses start and end point of div container to find value
    s = get_start(start, contents)
    e = get_end(end, contents[s:])
    price = float(contents[s:s+e])
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
