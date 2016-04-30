import splinter
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()

enter_home_page = driver.get('http://roomer-qa-1.herokuapp.com')
click_Find_Rooms = driver.find_element_by_css_selector('div.find_rooms.blue-btn').click()
time.sleep(8)
insert_email_for_secret_deals = driver.find_element_by_name('user[email]').send_keys('afd@afd.com')
click_unlock_secret_deals = driver.find_element_by_name('button').click()
time.sleep(10)
book_first_room_on_list = driver.find_element_by_css_selector('.book-button-row.blue-btn.book-button-row-link').click()
move_to_review_page = driver.switch_to.window(driver.window_handles[-1])
driver.get(driver.current_url)
select_non_life_happens_entry = driver.find_element_by_css_selector(
    '.entry_box_icon.entry_box_radio.entry_box_col.entry_box_col1').click()
time.sleep(5)
click_book_entry = driver.find_element_by_css_selector('.book_now_btn_redirect').click()
driver.get(driver.current_url)
insert_first_name_review = driver.find_element_by_id('review-first-name').send_keys('om')
insert_last_name_review = driver.find_element_by_id('review-last-name').send_keys('ri')
insert_email_review = driver.find_element_by_id('review-email').send_keys('omri@golan.com')
insert_phone_number_review = driver.find_element_by_id('mobile-number').send_keys('7027031452')
insert_credit_number_review = driver.find_element_by_id('review-credit-card-number').send_keys('4242424242424242')
insert_credit_expire_date_review = driver.find_element_by_id('review-cc-exp-month').send_keys(Keys.PAGE_DOWN)
insert_credit_expire_year_review = driver.find_element_by_id('review-cc-exp-year').send_keys(Keys.PAGE_DOWN)
insert_credit_4last_num_review = driver.find_element_by_id('review-cc-security-code').send_keys('8789')
driver.find_element_by_id('review-state').send_keys('adf')
driver.find_element_by_id('review-city').send_keys('daf')
driver.find_element_by_id('review-street').send_keys('dfefq')
driver.find_element_by_id('review-zip').send_keys('101')
time.sleep(5)
driver.find_element_by_id('checkout-button').click()
