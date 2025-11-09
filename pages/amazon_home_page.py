class AmazonHomePage:
    def __init__(self, page):
        self.page = page
        self.url = "https://www.amazon.in/"
        self.search_box = "#twotabsearchtextbox"
        self.search_button = "input#nav-search-submit-button"

    def load(self):
        self.page.goto(self.url)

    def search_for_item(self, item):
        self.page.fill(self.search_box, item)
        self.page.click(self.search_button)

    def get_title(self):
        return self.page.title()
