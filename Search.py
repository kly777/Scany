from DrissionPage import Chromium

browser = Chromium()
def get_g_url(q):
    try:
        page = browser.new_tab(None)
        print("G START")
        page.get('https://www.google.com')
        page('#APjFqb').input(q)
        page.actions.key_down('enter')
        page.wait.load_start()
        result_container = page.eles("@class=dURPMd")
        results = result_container[0].children("tag=div")

        result = []
        for i in range(len(results)):
            p = results[i].ele("tag=a")
            if p:
                result.append(p.attr("href"))
        print("G END")
        page.close()
        return result
    except:
        print("G ERROR")
        return []



def get_b_url(q):
    try:
        page=browser.new_tab(None)
        print("B START")
        page.get('https://www.bing.com')
        page('@id=sb_form_q').input(q)
        page.actions.click(on_ele=page('@id=sb_form_q'))
        page.actions.key_down('enter')

        page.wait.load_start()
        result_container = page.eles("@id=b_results")
        results = result_container[0].children("tag=li")

        result = []
        for i in range(len(results)):
            p = results[i].ele("tag=a")
            if p:
                result.append(p.attr("href"))
        print("B END")
        page.close()
        return result
    except:
        print("B ERROR")
        return []

def get_d_url(q):
    page = browser.new_tab(None)
    print("D START")
    page.get('https://www.duckduckgo.com')
    page('@id=searchbox_input').input(q)
    page.actions.click(on_ele=page('@id=searchbox_input'))
    page.actions.key_down('enter')

    page.wait.load_start()
    result_container = page.eles("@class=react-results--main")
    results = result_container[0].children("tag=li")

    result = []
    for i in range(len(results)):
        p = results[i].eles("tag=a")[1]
        if p:
            result.append(p.attr("href"))
    print("D END")
    page.close()
    return result


def get_ba_url(q):
    page = browser.new_tab(None)
    print("BA START")
    page.get('https://www.baidu.com')
    page('@id=kw').input(q)
    page.actions.click(on_ele=page('@id=kw'))
    page.actions.key_down('enter')

    page.wait.load_start()
    result_container = page.eles("@id=content_left")
    results = result_container[0].children("tag=div")

    result = []
    for i in range(len(results)):
        p = results[i].eles("tag=a")[1]
        if p:
            result.append(p.attr("href"))
    print("BA END")
    page.close()
    return result


def get_y_url(q):
    page = browser.new_tab(None)
    print("Y START")
    page.get('https://search.yahoo.com')
    page('@id=yschsp').input(q)
    page.actions.click(on_ele=page('@id=yschsp'))
    page.actions.key_down('enter')

    page.wait.load_start()
    result_container = page.eles("@class=reg  searchCenterMiddle")
    results = result_container[0].children("tag=li")

    result = []
    for i in range(len(results)):
        p = results[i].ele("tag=a")
        if p:
            result.append(p.attr("href"))
    print("Y END")
    page.close()
    return result


def get_s_url(q):
    try:
        page = browser.new_tab(None)
        print("S START")
        page.get('https://startpage.com')
        page('@id=q').input(q)
        page.actions.click(on_ele=page('@id=q'))
        page.actions.key_down('enter')

        page.wait.load_start()
        result_container = page.eles("@class=w-gl")
        results = result_container[0].children("tag=div")

        result = []
        for i in range(len(results)):
            p = results[i].ele("tag=a")
            if p:
                result.append(p.attr("href"))
        print("S END")
        page.close()
        return result
    except:

        print("S ERROR")
        return []