# # coding=utf-8
# import mysql.connector
# import re
# import requests
# import json
# from timeit import default_timer as timer
# from time import sleep

<<<<<<< HEAD
=======
# url = "http://roomer-api-qa-2.herokuapp.com/api/reservations_by_hotels/690/2016-06-18/2016-06-28"

# header = {
#     "Authorization": "Token token=cd7de248487ac667fe3a6f60235ed1d0",
#     "Partner": "eric@kayak.com",
#     "API-Version": "1"
# }

# start = timer()


# def x():
#     r = requests.get(url, None, headers=header)
#     content = r.content
#     x = json.loads(content)
#     print type(x[0].get("reservation"))
#     print x[0].get("reservation").get("private")
#     sleep(1)


# x()

# end = timer()
# print end - start
















>>>>>>> origin/master

# url = "http://roomer-api-qa-2.herokuapp.com/api/reservations_by_hotels/690/2016-06-18/2016-06-28"
#
# header = {
#     "Authorization": "Token token=b673ed8608a1e684d0b957e326f3dffc",
#     "Partner": "eric@kayak.com",
#     "API-Version": "1"
# }
#
# start = timer()
#
#
#
# r = requests.get(url, None, headers=header)
# content = r.content
# x = json.loads(content)
# print type(x[0]["reservation"])
# print x[0]["reservation"]
# sleep(1)
#
#
#
# end = timer()
# print end - start
#
# a = []

# conn = mysql.connector.connect(user='admin', password='Roomerhasit1',
#                                port='14642',
#                                host='qa-db.chwkxuugo66h.us-east-1.rds.amazonaws.com',
#                                database='roomer')

# my_cursor = conn.cursor()
# my_cursor.execute('''
# select email, api_token, rate_plan_id
# from roomer.partners
# where email like '%trivago%'
# or email like '%kayak%'
# or email like '%skyscanner%'
# ''')
# f = my_cursor.fetchall()
# print f[0][0]
# conn.close()

# reservation_extraction_regex = r"(/)(\d+)"
# entry_url = "http://roomer-qa-2.herokuapp.com/hotels/las-vegas-hotels/the-venetian-resort-hotel-casino.h1100/44532119/book?rate_plan_id=1&rate_plan_token=2db3d78575fe81a0f7ad4c7c3104fcd7&"
#
# x = re.search(reservation_extraction_regex, entry_url).group(2)
# y = int(x)
# print y
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
sleep(5)
driver.get('http://roomer-qa-2.herokuapp.com/hotels/cannes-hotels/intercontinental-carlton-cannes.h2339/44560981?rate_plan_id=2&rate_plan_token=2bb5e9a092c79f3cffa0171cc53dbd6a')

'''
Click on life-happens in review
'''
book_first_room_on_list = driver.find_element_by_xpath(u'//.book-btn[contains(text(), "Book")]').click()

<<<<<<< HEAD
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from time import sleep
driver = webdriver.Firefox()
driver.implicitly_wait(5)

driver.get('http://roomer-qa-2.herokuapp.com/hotels/bali-hotels/hanging-gardens-of-bali.h476098/44381586?rate_plan_id=2&rate_plan_token=157c6f410cd7712827ed39b8af69068c&')

'''
Click on life-happens in review
'''

'''
Tries to choose life happens on review if it cant
Moves to filling the rest of the fields
'''
x = driver.find_elements_by_css_selector(".entry-white-box.entry-book-option.entry-white-box-life-happens.clearfix")[0]
x.find_elements_by_css_selector(".entry_box_title.entry_box_col.entry_box_col2")[0].click()
x.find_elements_by_css_selector(".book-wrapper.book-btn.book_now_btn.book_now_btn_redirect")[0].click()
sleep(5)
driver.save_screenshot('screenie.png')

=======
# '''
# Tries to choose life happens on review if it cant
# Moves to filling the rest of the fields
# '''
>>>>>>> origin/master
# try:
#     driver.find_elements_by_css_selector(".lh-row.push-bottom ")[1].click()
#     driver.find_element_by_link_text("Continue").click()
# except IndexError:
#     pass
# driver.find_element_by_id("review-full-name").send_keys("omri golan")
# driver.find_element_by_id("mobile-number").send_keys("7547541452")
# driver.find_element_by_id("review-email").send_keys("bob.g@goroomer.com")
# driver.find_element_by_link_text("Continue").click()
# insert_credit_number_review = driver.find_element_by_id('review-credit-card-number').send_keys('4242424242424242')
# insert_credit_expire_date_review = driver.find_element_by_id('review-cc-exp-month').send_keys(Keys.PAGE_DOWN)
# insert_credit_expire_year_review = driver.find_element_by_id('review-cc-exp-year').send_keys(Keys.PAGE_DOWN)
# insert_credit_4last_num_review = driver.find_element_by_id('review-cc-security-code').send_keys('8789')
# insert_billing_address_text = driver.find_element_by_id('billing-address-input').send_keys('Isrotel Tower, Ha-Yarkon Street, Tel Aviv-Yafo, Israel')
# insert_billing_address_click_box = driver.find_element_by_id('billing-address-input').click()
# insert_billing_address_arrow_down = driver.find_element_by_id('billing-address-input').send_keys(Keys.ARROW_DOWN)
# insert_street_address_click_enter = driver.find_element_by_id('billing-address-input').send_keys(Keys.ENTER)

# driver.find_element_by_id('checkout-button').click()