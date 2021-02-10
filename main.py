from selenium import webdriver
import time


item = input('please enter you search term and hit enter')

url = 'https://www.facebook.com/marketplace/{}/search?sortBy=best_match&query={}&exact=false'

cities = ['orlando', 'atlanta', 'nyc', 'houston', 'albuquerque', 'chicago', 'omaha', 'denver',
          'la', 'boise']



global driver
driver = webdriver.Chrome()


for city in cities:
    driver.get(url.format(city, item))
    time.sleep(2)
    # driver.find_element_by_class_name("j83agx80 taijpn5t cxgpxx05 dflh9lhu sj5x9vvc scb9dxdr").click()
    # driver.find_element_by_class_name('dwo3fsh8 g5ia77u1 ow4ym5g4 auili1gw nhd2j8a9 oygrvhab cxmmr5t8 hcukyx3x kvgmc6g5 l9j0dhe7 i1ao9s8h du4w35lb rq0escxv oo9gr5id j83agx80 jagab5yi knj5qynh fo6rh5oj lzcic4wl osnr6wyh hv4rvrfc dati1w0a p0x8y401 k4urcfbm').click()
    # driver.find_element_by_class_name('bp9cbjyn j83agx80 btwxx1t3 buofh1pr i1fnvgqd hpfvmrgz').click()
    input('PRESS ENTER TO GO TO NEXT CITY')

SCROLL_PAUSE_TIME = 0.5





# scroll_height = 360
#
# for x in range(8):
#     driver.execute_script("window.scrollTo(0, {})".format(scroll_height))
#     scroll_height += 360
# Get scroll height
# last_height = driver.execute_script("return document.body.scrollHeight")
#
# while True:
#     # Scroll down to bottom
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#     # Wait to load page
#     time.sleep(SCROLL_PAUSE_TIME)
#
#     # Calculate new scroll height and compare with last scroll height
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == last_height:
#         break
#     last_height = new_height

