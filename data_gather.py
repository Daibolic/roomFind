"""This modules gathers relevant data from webpages"""

from lxml import html
import requests


BASEURL = "https://classes.cornell.edu/browse/roster/SP17"
CODEURL = "https://registrar.cornell.edu/spaces/building-codes"

def find_subpages(url):
    """ returns a list of subpages to visit from url """
    print("Gathering subpages from: "+url)
    page = requests.get(url)
    tree = html.fromstring(page.content)
    subpages = tree.xpath('//li[@class="browse-subjectcode"]/a/text()')
    result = []
    for subpage in subpages:
        result = result+["/subject/" + subpage]
    return result

def find_room_time(url):
    """ returns list of (room_name, days, time_occupied) tuples from url"""
    print("Gathering room and timings from: "+url)
    page = requests.get(url)
    tree = html.fromstring(page.content)
    meet_patterns = tree.xpath('//li[@class="dates"]')
    result = []
    for pattern in meet_patterns:
        room = pattern.xpath('.//a/text()')
        days = pattern.xpath('.//span[@class="tooltip-iws"]/text()')
        time = pattern.xpath('.//time//text()')
        if (len(room) > 0) and (len(time) > 0 and len(days) > 0):
            result.append((room[0], days[0], time[0]))
    return result

def get_building_codes(url):
    """ return list of (building name, building code) tuples from url"""
    page = requests.get(url)
    tree = html.fromstring(page.content)
    rows = tree.xpath('//tbody/tr')
    result = []
    for row in rows:
        code = row.xpath('.//td[@headers="view-field-building-code-table-column"]/text()')
        codestripped = code[0].strip('\n').strip()
        print(codestripped)
        if (codestripped == ""):
            continue
        fullname = row.xpath('.//td[@headers="view-name-table-column"]/a/text()')[0]
        result.append((codestripped, fullname))
    return result

def get_all_room_time():
    """
    Writes the full list of (room, time) tuples from all subpages to file room_info.
    Overwrites the original file.
    """
    subpages = find_subpages(BASEURL)
    all_rm_tm = []
    for suburl in subpages:
        fullurl = BASEURL+suburl
        rm_tm = find_room_time(fullurl)
        all_rm_tm = all_rm_tm + rm_tm
    fileobject = open("room_info", "w")
    for entry in all_rm_tm:
        fileobject.write(entry[0]+","+entry[1]+","+entry[2]+"\n")
    fileobject.close()

def generate_building_codes():
    """
    Writes the full list of buildings and their corresponding codes to file bld_code.
    Overwrites the original file.
    """
    codes = get_building_codes(CODEURL)
    fileObject = open("bld_code", "w")
    for entry in codes:
        fileObject.write(entry[0]+","+entry[1]+"\n")
    fileObject.close()