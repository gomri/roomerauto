import re
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from time import sleep 

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
driver.implicitly_wait(15)


redirect_to_page = driver.get('http://roomer-qa-2.herokuapp.com/rooms/Orlando--FL--USA/dates/2016-06-27,2016-07-02?adults=2&children=0&child_guests_ages=&reservation_id=32477_2016-06-27_2016-07-02_H_APT-U10-B1-SC-U10__2_0_&utm_campaign=Orlando--FL--USA&utm_source=KAYAK&utm_medium=API&rate_plan_id=2&rate_plan_token=8105c3e7462275e0b4f749c4044d8e19&currency=USD&orig_price=155')
sleep(3)
try:
    list_page = driver.find_element_by_css_selector('.list-right')
    high_lighted_room_list = list_page.find_element_by_css_selector(".component-item.component-list-item.highlighted")
    open_first_room_list = high_lighted_room_list.find_element_by_css_selector("button.component-post.button").click()
    move_to_review_page = driver.switch_to.window(driver.window_handles[-1])
    driver.get(driver.current_url)
except NoSuchElementException:
    list_page = driver.find_element_by_css_selector('.list-right')
    first_room = list_page.find_element_by_css_selector('.component-item.component-list-item.secret_deal_unlocked.secret_deal_has.isDatesVisible')
    open_first_room_list = high_lighted_room_list.find_element_by_css_selector("button.component-post.button").click()
    move_to_review_page = driver.switch_to.window(driver.window_handles[-1])
try:
    entry_with_LH = driver.find_element_by_css_selector(".entry-white-box.entry-book-option.entry-white-box-life-happens.clearfix")
    select_non_refund_LH = entry_with_LH.find_element_by_css_selector(".entry-white-box.entry_box_no_refund").click()
    entry_with_LH.find_element_by_xpath(u"//div[contains(text(), 'Book Now')]").click()
except NoSuchElementException:
    try:
        entry_without_LH = driver.find_element_by_css_selector(".entry-white-box.entry-book-option.no_refund")
        entry_without_LH.find_element_by_xpath(u"//div[contains(text(), 'Book Now')]").click()
    except NoSuchElementException:
        entry_free_cancellation = driver.find_element_by_css_selector('.entry-white-box.entry-book-option.free_cancellation')
        pass            
click_book_entry = driver.find_element_by_css_selector('.book_now_btn_redirect').click()
driver.get(driver.current_url)
print get_reservation_ID(driver.current_url, regex_reservation_id)

'''
New review

Tries to choose life happens on review if it cant
Moves to filling the rest of the fields
'''
try:   
    review_with_LH = driver.find_element_by_css_selector(".lh-select.collapsable.font-regular.bottom-separator")
    if review_with_LH:
        life_happen_review = raw_input('Y/N life happens: ')
        if life_happen_review.upper() == 'Y':
            review_with_LH.find_element_by_xpath(u"//span[contains(text(), '(Recommended)')]").click()
            review_with_LH.find_element_by_css_selector('.continue-button.standard-button.smaller.font-regular.weight-medium.push-bottom').click()
        else:
            review_with_LH.find_element_by_css_selector('.continue-button.standard-button.smaller.font-regular.weight-medium.push-bottom').click()
except NoSuchElementException:
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

'''
Check that your on thank you page
'''
try:
    thank_you_page = driver.find_element_by_css_selector('.thank_you_title')
    print get_transaction_ID(driver.current_url, regex_transaction_id)
    print "Successfully Purchased room"
except NoSuchElementException:
    driver.save_screenshot('error_buying_room.png')
    print "Could not Purchase room please look at script diractory for a screenshot of failer"

driver.quit()
