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


def get_reservation_ID(url, regex):
    string_reservation_id = re.search(regex, url).group(2)
    int_reservation_id = int(string_reservation_id)
    return int_reservation_id


def get_transaction_ID(url, regex):
    string_transaction_id = re.search(regex, url).group(2)
    int_transaction_id = int(string_transaction_id)
    return int_transaction_id


driver = webdriver.Firefox()
driver.implicitly_wait(20)

enter_home_page = driver.get('http://roomer-qa-1.herokuapp.com')
click_Find_Rooms = driver.find_element_by_css_selector('div.find_rooms.blue-btn').click()
'''
Solves the problem of the code crashing if the list hes not loaded yet
By waiting for the list to load before it takes any action
'''
while True:
    try:
        insert_email_for_secret_deals = driver.find_element_by_name('user[email]').send_keys('afd@afd.com')
        click_unlock_secret_deals = driver.find_element_by_name('button').click()
        break
    except ElementNotVisibleException:
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
        '.component-post.button').click()
move_to_review_page = driver.switch_to.window(driver.window_handles[-1])
driver.get(driver.current_url)
try:
    entry_with_LH = driver.find_element_by_css_selector(".entry-white-box.entry-book-option.entry-white-box-life-happens.clearfix")
    select_non_LH = entry_with_LH.find_element_by_css_selector(".entry-white-box.entry_box_no_refund").click()
    entry_with_LH.find_element_by_xpath(u"//div[contains(text(), 'Book Now')]").click()
except NoSuchElementException:    
    entry_without_LH = driver.find_element_by_css_selector(".entry-white-box.entry-book-option.no_refund")
    entry_without_LH.find_element_by_xpath(u"//div[contains(text(), 'Book Now')]").click()
print get_reservation_ID(driver.current_url, regex_reservation_id)

'''
New review

Tries to choose life happens on review if it cant
Moves to filling the rest of the fields
'''
# try:
review_with_LH = driver.find_element_by_css_selector(".lh-select.collapsable.font-regular.bottom-separator")
review_with_LH.find_element_by_xpath(u"//span[contains(text(), '(Recommended)')]").click()
review_with_LH.find_element_by_css_selector('.continue-button.standard-button.smaller.font-regular.weight-medium.push-bottom').click()
# except NoSuchElementException:
  # pass
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
