from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
from time import sleep

class InstaAutoBot:

    links = []

    # Function to perform LogIn to Instagram
    def login(self, username, password):
        self.driver = webdriver.Chrome(executable_path="InstaAutoBot/Webdriver/chromedriver.exe")
        self.driver.get(r"https://www.instagram.com/")
        sleep(1)

        # Enters the Username on Instagram Login Page
        userEntry = self.driver.find_element_by_xpath("//input[@name='username']")
        userEntry.send_keys(username)
        sleep(1)

        # Enters the Password on Instagram Login Page
        passEntry = self.driver.find_element_by_xpath("//input[@name='password']")
        passEntry.send_keys(password)
        sleep(1)

        # It press the Login Button
        login_btn = self.driver.find_element_by_xpath("//button[@type='submit']")
        login_btn.click()
        sleep(5)

        # It press the Not Now Button of Save Login Page
        notnow_btn = self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div/div/div/button")
        notnow_btn.click()
        sleep(8)

        # It press the Not Now Button of Turn on Notifications Pop Up
        notnow_btn1 = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
        notnow_btn1.click()
        sleep(3)

    
    # Function to Like Posts of Particular Hashtag
    # Also provide Number of Posts to be liked
    def like_by_hashtags(self, hashtag, num_likes):

        # It press on the Search Box and Enter the Hashtag
        search_box = self.driver.find_element_by_xpath("//input[@placeholder = 'Search']")
        search_box.send_keys("#"+hashtag)
        sleep(3)

        # It press Enter to Search the Hashtag
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a").send_keys(Keys.ENTER)
        sleep(5)
        
        # Extracts all the <a> tag elements of the Current Page
        links = self.driver.find_elements_by_tag_name('a')

        # Function to filter the Posts Links
        def condition(link):
            return '.com/p/' in link.get_attribute('href')

        # Below list contains all the Post Links
        valid_links = list(filter(condition, links))

        if len(valid_links) < num_likes:
            num_likes = len(valid_links)

        self.links = []

        # Extracts all the URLs from the <a> tags
        for i in range(num_likes):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)

        # Visit all the URLs of the Links list
        for link in self.links:
            self.driver.get(link)
            sleep(2)

            # It press the Like button to like the post
            like_btn = self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button")
            like_btn.click()
            sleep(2)

        self.driver.get(r"https://www.instagram.com/")


    # Function to Like and Comment on Posts of Particular Hashtag
    # Also provide Number of Posts to be liked and commented on it
    def comment_by_hashtags(self, hashtag, num_likes):

        # List of some commom Comments
        comments = ["Insane", "Good Day", "Wow!", "Lots of Love", "Nice photo", "You are awesome" , "Made my day!", "Amazing!", "Beautiful", "Great Photo"]
        
        # It press on the Search Box and Enter the Hashtag
        search_box = self.driver.find_element_by_xpath("//input[@placeholder = 'Search']")
        search_box.send_keys("#"+hashtag)
        sleep(3)

        # It press Enter to Search the Hashtag
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a").send_keys(Keys.ENTER)
        sleep(5)

        # Extracts all the <a> tag elements of the Current Page
        links = self.driver.find_elements_by_tag_name('a')

        # Function to filter the Posts Links
        def condition(link):
            return '.com/p/' in link.get_attribute('href')

        # Below list contains all the Post Links
        valid_links = list(filter(condition, links))

        if len(valid_links) < num_likes:
            num_likes = len(valid_links)
        
        self.links = []

        # Extracts all the URLs from the <a> tags
        for i in range(num_likes):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)

        # Visit all the URLs of the Links list
        for link in self.links:
            self.driver.get(link)
            sleep(3)

            # It press the Like button to like the post
            like_btn = self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button")
            like_btn.click()
            sleep(2)

            # It press on Comment Box and Comment on the post
            self.driver.find_element_by_class_name("RxpZH").click()
            sleep(1)
            comment_box = self.driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']")
            comment_box.send_keys(comments[randint(0, 9)])
            sleep(2)
            self.driver.find_element_by_xpath("//button[@type = 'submit']").click()
            sleep(5)

        self.driver.get(r"https://www.instagram.com/")


    # Function to Like the Posts of Particular Username
    # Also provide Number of Posts to be liked
    def like_by_username(self, u_name, num_likes):

        # It press on the Search Box and Enter the Username
        search_box = self.driver.find_element_by_xpath("//input[@placeholder = 'Search']")
        search_box.send_keys(u_name)
        sleep(2)

        # It press Enter to Search the Username
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a").send_keys(Keys.ENTER)
        sleep(5)

        # Extracts all the <a> tag elements of the Current Page
        links = self.driver.find_elements_by_tag_name('a')

        # Function to filter the Posts Links
        def condition(link):
            return '.com/p/' in link.get_attribute('href')

        # Below list contains all the Post Links
        valid_links = list(filter(condition, links))

        if len(valid_links) < num_likes:
            num_likes = len(valid_links)
    
        self.links = []

        # Extracts all the URLs from the <a> tags
        for i in range(num_likes):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)

        # Visit all the URLs of the Links list
        for link in self.links:
            self.driver.get(link)
            sleep(3)

            # It press the Like button to like the post
            like_btn = self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button")
            like_btn.click()
            sleep(2)

        self.driver.get(r"https://www.instagram.com/")


    # Function to Like and Comment on Posts of Particular Hashtag
    # Also provide Number of Posts to be liked and commented on it
    def comment_by_username(self, u_name, num_likes):
        
        # List of some commom Comments
        comments = ["Insane", "Good Day", "Wow!", "Lots of Love", "Nice photo", "You are awesome" , "Made my day!", "Amazing!", "Beautiful", "Great Photo"]
        
        # It press on the Search Box and Enter the Username
        search_box = self.driver.find_element_by_xpath("//input[@placeholder = 'Search']")
        search_box.send_keys(u_name)
        sleep(2)

        # It press Enter to Search the Username
        self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a").send_keys(Keys.ENTER)
        sleep(5)

        # Extracts all the <a> tag elements of the Current Page
        links = self.driver.find_elements_by_tag_name('a')

        # Function to filter the Posts Links
        def condition(link):
            return '.com/p/' in link.get_attribute('href')

        # Below list contains all the Post Links
        valid_links = list(filter(condition, links))

        if len(valid_links) < num_likes:
            num_likes = len(valid_links)
    
        self.links = []

        # Extracts all the URLs from the <a> tags
        for i in range(num_likes):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)

        # Visit all the URLs of the Links list
        for link in self.links:
            self.driver.get(link)
            sleep(3)

            # It press the Like button to like the post
            like_btn = self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button")
            like_btn.click()
            sleep(2)

            # It press on Comment Box and Comment on the post
            self.driver.find_element_by_class_name("RxpZH").click()
            sleep(1)
            comment_box = self.driver.find_element_by_xpath("//textarea[@placeholder='Add a comment…']")
            comment_box.send_keys(comments[randint(0, 9)])
            sleep(2)
            self.driver.find_element_by_xpath("//button[@type = 'submit']").click()
            sleep(5)

        self.driver.get(r"https://www.instagram.com/")
    

    # Function to follow the Users based on 
    # Given list of Usernames
    def follow_by_usernames(self, usernames):

        # Visits all User Profile Page
        for user in usernames:

            # It press on the Search Box and Enter the Username
            search_box = self.driver.find_element_by_xpath("//input[@placeholder = 'Search']")
            search_box.send_keys(user)
            sleep(1)

            # It press Enter to Search the Username
            self.driver.find_element_by_xpath("//*[@id=\"react-root\"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a").send_keys(Keys.ENTER)
            sleep(3)

            # It press the Follow button to follow the Username
            follow_btn = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button")
            follow_btn.click()
            sleep(5)

        self.driver.get(r"https://www.instagram.com/")

        
    # Function to Share the Post using Post URLs
    # With the provided List of Usernames
    def share_post(self, u_list, post_list):

        # Visits all the Posts
        for link in post_list:
            self.driver.get(link)
            sleep(2)

            # It press the Share button for sharing the post
            share_btn = self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[1]/span[3]/button")
            share_btn.click()
            sleep(3)

            # Searches for All the users of the List
            for user in u_list:

                # It press on the Search Box and Enter the Username
                search_box = self.driver.find_element_by_xpath("//input[@placeholder = 'Search...']")
                search_box.send_keys(user)
                sleep(4)

                # Select the User to which post to be shared
                self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div[2]/div[1]/div/div[3]/button").click()
                sleep(2)

            # It press the Send button to Share the Post
            self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div[2]/div[4]/button").click()
            sleep(5)

        self.driver.get(r"https://www.instagram.com/")


    # Function to perform LogOut from Instagram
    def logout(self):

        # It clicks on the Profile Icon
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span").click()
        sleep(1)

        # It press the LogOut button 
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div").click()
        sleep(5)

        # Closes the Window
        self.driver.quit()
            
