import pytest
from pages.amazon_home_page import AmazonHomePage

@pytest.mark.smoke
def test_amazon_search(page):
    home = AmazonHomePage(page)
    home.load()
    title_before = home.get_title()
    print(f"Title before search: {title_before}")
    home.search_for_item("Playwright Book")
    page.wait_for_timeout(3000)
    title_after = home.get_title()
    print(f"Title after search: {title_after}")
    assert "Playwright" in title_after or "book" in title_after.lower(), \
        "Search did not navigate to expected results page"
