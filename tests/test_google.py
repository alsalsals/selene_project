from selene import browser, by, be, have


def test_check_name_on_github_page():
    """ Open github and check name on the page """
    browser.open('https://github.com/alsalsals')
    browser.element('[itemprop="name"]').should(have.text('Alsu Fayzullina'))

