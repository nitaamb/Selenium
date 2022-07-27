import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistration(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        
    def test_a_success_registration(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/registration") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("punyanitaa") # isi username
        time.sleep(1)
        browser.find_element(By.NAME,"email").send_keys("punyanitaa@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("punyanitaa") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/main/div/div/form/div[5]/button").click() # klik tombol daftar sekarang
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div[1]/main/div/div[2]/p").text

        self.assertEqual('Selamat! Akun anda berhasil dibuat', response_data)

    def test_b_failed_registration_with_registered_email(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/registration") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("nitata") # isi username
        time.sleep(1)
        browser.find_element(By.NAME,"email").send_keys("nitaamb@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("nitata") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/main/div/div/form/div[5]/button").click() # klik tombol daftar sekarang
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div[1]/main/div/div/form/div[1]/div[1]/p").text

        self.assertEqual('Email atau username sudah terdaftar', response_data)

    def test_c_failed_registration_with_empty_username_email_and_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/registration") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"username").send_keys("") # isi username
        time.sleep(1)
        browser.find_element(By.NAME,"email").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/main/div/div/form/div[5]/button").click() # klik tombol daftar sekarang
        time.sleep(3)

        # validasi
        response_username_field = browser.find_element(By.XPATH,"/html/body/div[1]/main/div/div/form/div[2]/div").text
        response_email_field = browser.find_element(By.XPATH,"/html/body/div[1]/main/div/div/form/div[3]/div").text
        response_password_field = browser.find_element(By.XPATH,"/html/body/div[1]/main/div/div/form/div[4]/div").text

        self.assertEqual('diperlukan username', response_username_field)
        self.assertEqual('diperlukan email', response_email_field)
        self.assertEqual('diperlukan kata sandi', response_password_field)

    def tearDown(self): 
        self.browser.close() 

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_d_failed_login_with_invalid_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/login") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"email").send_keys("punyanita@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("punyanita") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/main/div/div/form/div[4]/button").click() # klik tombol masuk
        time.sleep(3)

        # validasi
        response_data = browser.find_element(By.XPATH,"/html/body/div[1]/main/div/div/form/div[2]/p").text

        self.assertEqual('Kata Sandi Salah', response_data)

    def test_e_failed_login_with_empty_email_and_password(self): 
        # steps
        browser = self.browser #buka web browser
        browser.get("https://myappventure.herokuapp.com/login") # buka situs
        time.sleep(3)
        browser.find_element(By.NAME,"email").send_keys("") # isi email
        time.sleep(1)
        browser.find_element(By.NAME,"password").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/main/div/div/form/div[4]/button").click() # klik tombol masuk
        time.sleep(3)

        # validasi
        response_email_field = browser.find_element(By.XPATH,"/html/body/div[1]/main/div/div/form/div[2]/div").text
        response_password_field = browser.find_element(By.XPATH,"/html/body/div[1]/main/div/div/form/div[3]/div").text

        self.assertEqual('diperlukan email', response_email_field)
        self.assertEqual('diperlukan kata sandi', response_password_field)

    def tearDown(self): 
        self.browser.close()

if __name__ == "__main__": 
    unittest.main()