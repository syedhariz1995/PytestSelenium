# if all classes (e.g. under POM) requires to have a method to get something in common
# e.g. all class is required to get page's title
# then create a utils folder, and add a utils.py file
# this is the parent, to be pass to child class'


class BrowserUtils:
    def __init__(self, driver):
        self.driver = driver
        
    def getTitle(self):
        return self.driver.title