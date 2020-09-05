from selenium import webdriver

def main():
    chrome_browser = webdriver.Chrome('./automation/chromedriver')
    chrome_browser.maximize_window()
    chrome_browser.get('http://www.seleniumeasy.com/test/basic-first-form-demo.html')

    assert 'Selenium Easy Demo' in chrome_browser.title
    message_button = chrome_browser.find_element_by_class_name('btn-default')
    print(message_button.get_attribute('innerHTML'))

    assert 'Show Message' in chrome_browser.page_source
    text_box = chrome_browser.find_element_by_id('user-message')
    text_box.clear()
    text_box.send_keys('This us my new input')
    message_button.click()

    output_message = chrome_browser.find_element_by_id('display')
    print(output_message.text)

    input('Ready to close window?\n')
    return 0

if __name__ == "__main__":
    main()
