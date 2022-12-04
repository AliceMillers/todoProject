from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from datetime import datetime
import random
import time

class TestCompletenessExistingTodo():

    def test_completenessExistingTodo(self):
        driver = webdriver.Chrome()
        #driver=webdriver.firefox()
        #driver=webdriver.ie()
        #maximize the window size
        driver.maximize_window()
        #navigate to the url
        driver.get("https://todo.scriveqa.com/")
        time.sleep(3)
        # check Todos title
        title = "Todo App"
        assert title == driver.title
        #identify the Add to-do field and add the first item
        now = datetime.now()
        date = now.strftime("%m/%d/%Y")
        add_todo_field = driver.find_element(By.CLASS_NAME, "add-todo")
        add_todo_field.send_keys(str(date) + " test " + str(random.randint(1, 1999)))
        time.sleep(3)
        #click on the Enter button
        add_todo_field.send_keys(Keys.ENTER)
        time.sleep(3)
        #add second item
        add_todo_field.send_keys(str(date) + " test " + str(random.randint(1, 1999)))
        time.sleep(3)
        #click on the Enter button
        add_todo_field.send_keys(Keys.ENTER)
        time.sleep(3)
        #Verify completeness to do item
        driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "completed")
        #Verify Completed filter
        completedFilter = "Completed"
        assert completedFilter == driver.find_element(By.LINK_TEXT, 'Completed').text
        driver.find_element(By.LINK_TEXT, 'Completed').click()
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "selected")
        #close the browser
        driver.close()
