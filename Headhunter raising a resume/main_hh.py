from selenium import webdriver
from selenium.webdriver.common.by import By
from login_with_password import LoginWithPassword
from hh import HH
from datetime import datetime, timedelta
import time


driver = webdriver.Firefox()
log_site = LoginWithPassword()
hh = HH()

def main():
    try:
        driver.maximize_window()
        driver.get(log_site.site)
        hh.send_btn(driver, log_site.entrance)
        hh.send_btn(driver, log_site.with_psswrd)

        hh.fill_field(driver, value=log_site.phone, field=log_site.tel_field) #authorization hh
        hh.fill_field(driver, value=log_site.password, field=log_site.pswrd_field)
        hh.send_btn(driver, log_site.log_btn)

        hh.send_btn(driver, hh.resume) #resume extension

        while True: #check time
            resume_txt = driver.find_element(by=By.XPATH, value=hh.extension_line)
            resume_time = resume_txt.text
            print(resume_time)
            is_there_text = True if 'Поднять в поиске' in driver.find_element(by=By.XPATH, value=hh.btn_name).text else False
            now = datetime.now()
            current_time = timedelta(hours=now.hour, minutes=now.minute)
            h, m = map(int, resume_time.split()[-1].split(':'))
            time_obj = timedelta(hours=h, minutes=m)
            if not is_there_text:
                if current_time < time_obj:
                    total = int(str(((time_obj - current_time) + timedelta(seconds=60)).seconds))
                    print(f'pause {hh.edited_time(total)}')
                    time.sleep(total)
                    driver.refresh()
            else:
                print('the resume has been raised')
                hh.send_btn(driver, hh.prolongation)
                driver.refresh()

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

if __name__ == '__main__':
    main()
