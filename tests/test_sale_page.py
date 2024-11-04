def test_sale_links(sale_page):
    sale_page.open_page()
    sale_page.open_all_sale_offers()


def test_check_label(sale_page):
    sale_page.open_page()
    sale_page.find_label()


def test_check_title(sale_page):
    sale_page.open_page()
    sale_page.check_title()
