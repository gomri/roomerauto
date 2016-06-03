import time
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

'''
Regex query's to get the reservation ID, transaction ID
'''
regex_reservation_id = re.compile(r'(/)(\d+)')
regex_transaction_id = re.compile(r'(id=)(\d+)')

# show yuval

def get_reservation_ID(url, regex):
    string_reservation_id = re.search(regex, url).group(2)
    int_reservation_id = int(string_reservation_id)
    return int_reservation_id


def get_transaction_ID(url, regex):
    string_transaction_id = re.search(regex, url).group(2)
    int_transaction_id = int(string_transaction_id)
    return int_transaction_id


driver = webdriver.Firefox()

enter_home_page = driver.get('https://www.roomertravel.com')
click_Find_Rooms = driver.find_element_by_css_selector('div.find_rooms.blue-btn').click()
'''
Solves the problem of the code crashing if the list hes not loaded yet
By waiting for the list to load before it takes any action
'''
while True:
    try:
        insert_email_for_secret_deals = driver.find_element_by_name('user[email]').send_keys('afd@afd.com')
        click_unlock_secret_deals = driver.find_element_by_name('button').click()
        time.sleep(5)
        break
    except ElementNotVisibleException:
        time.sleep(10)
        print "Could not find element because page is still loading will try again in 10 seconds"
time.sleep(10)
'''
Deals with the new and the old list
By telling the code that if it gets an exception that there is no such element
Because it's looking for the button of the wrong list it tries the the other lists button
'''
try:
    book_first_room_on_list = driver.find_element_by_css_selector(
        '.book-button-row.blue-btn.book-button-row-link').click()
except NoSuchElementException:
    book_first_room_on_list = driver.find_element_by_css_selector(
        "css=.book-wrapper.book-btn.book_now_btn.book_now_btn_redirect:contains('Book')").click()
move_to_review_page = driver.switch_to.window(driver.window_handles[-1])
driver.get(driver.current_url)
select_non_life_happens_entry = driver.find_element_by_css_selector(
    '.entry_box_icon.entry_box_radio.entry_box_col.entry_box_col1').click()
time.sleep(5)
click_book_entry = driver.find_element_by_css_selector('.book_now_btn_redirect').click()
river.get(driver.current_url)
print get_reservation_ID(driver.current_url, regex_reservation_id)

'''
New review

Tries to choose life happens on review if it cant
Moves to filling the rest of the fields
'''
try:
    click_life_happens_review_step1 = \
        driver.find_elements_by_css_selector('.font-regular.weight-bold.font-highlighted-special')[0].click()
    click_continue_review_step1 = driver.find_element_by_link_text("Continue").click()
except IndexError:
    pass
insert_review_full_name = driver.find_element_by_id("review-full-name").send_keys("omri golan")
insert_review_mobile_number = driver.find_element_by_id("mobile-number").send_keys("7547541452")
insert_review_email = driver.find_element_by_id("review-email").send_keys("bob.g@goroomer.com")
click_continue_review_step2 = driver.find_element_by_link_text("Continue").click()
insert_credit_number_review = driver.find_element_by_id('review-credit-card-number').send_keys('4242424242424242')
insert_credit_expire_date_review = driver.find_element_by_id('review-cc-exp-month').send_keys(Keys.PAGE_DOWN)
insert_credit_expire_year_review = driver.find_element_by_id('review-cc-exp-year').send_keys(Keys.PAGE_DOWN)
insert_credit_4last_num_review = driver.find_element_by_id('review-cc-security-code').send_keys('8789')
insert_billing_address_text = driver.find_element_by_id('billing-address-input').send_keys(
    'Isrotel Tower, Ha-Yarkon Street, Tel Aviv-Yafo, Israel')
insert_billing_address_click_box = driver.find_element_by_id('billing-address-input').click()
insert_billing_address_arrow_down = driver.find_element_by_id('billing-address-input').send_keys(Keys.ARROW_DOWN)
insert_billing_address_click_enter = driver.find_element_by_id('billing-address-input').send_keys(Keys.ENTER)
click_book_button_review = driver.find_element_by_id('checkout-button').click()
time.sleep(10)
print get_transaction_ID(driver.current_url, regex_transaction_id)

'''
Old review
'''
# insert_first_name_review = driver.find_element_by_id('review-first-name').send_keys('om')
# insert_last_name_review = driver.find_element_by_id('review-last-name').send_keys('ri')
# insert_email_review = driver.find_element_by_id('review-email').send_keys('omri@golan.com')
# insert_phone_number_review = driver.find_element_by_id('mobile-number').send_keys('7027031452')
# insert_credit_number_review = driver.find_element_by_id('review-credit-card-number').send_keys('4242424242424242')
# insert_credit_expire_date_review = driver.find_element_by_id('review-cc-exp-month').send_keys(Keys.PAGE_DOWN)
# insert_credit_expire_year_review = driver.find_element_by_id('review-cc-exp-year').send_keys(Keys.PAGE_DOWN)
# insert_credit_4last_num_review = driver.find_element_by_id('review-cc-security-code').send_keys('8789')
# insert_stat_review = driver.find_element_by_id('review-state').send_keys('adf')
# insert_city_review = driver.find_element_by_id('review-city').send_keys('daf')
# insert_street_review = driver.find_element_by_id('review-street').send_keys('dfefq')
# insert_stat_zipcode = driver.find_element_by_id('review-zip').send_keys('101')
# time.sleep(5)

# click_book_button_review = driver.find_element_by_id('checkout-button').click()

# driver.quit()
