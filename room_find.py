from lxml import html
import requests

base_url = "https://classes.cornell.edu/browse/roster/SP17"

def find_subpages(url):
    """ returns a list of subpages to visit from url """
    page = requests.get(url)
    tree = html.fromstring(page.content)
    subpages = tree.xpath('//li[@class="browse-subjectcode"]/a/text()')
    result = []
    for subpage in subpages:
        result = result+["/subject/" + subpage]
    return result

def find_room_time(url):
    """ returns list of (room_name, time_occupied) tuples from url"""
    page = requests.get(url)
    tree = html.fromstring(page.content)
    meet_patterns = tree.xpath('//li[@class="dates"]')
    result = []
    for pattern in meet_patterns:
        room = pattern.xpath('.//a/text()')
        time = pattern.xpath('.//time//text()')
        if (len(room) > 0) and (len(time) > 0):
            result.append((room[0], time[0]))
    return result
