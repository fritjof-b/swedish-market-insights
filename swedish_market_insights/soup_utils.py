from bs4 import BeautifulSoup
import pandas as pd


def get_trade_entries_from_page(page_content: bytes) -> pd.DataFrame:
    soup = BeautifulSoup(page_content, "html.parser")
    table = soup.find("table")
    rows = table.find_all("tr")

    header_row = rows.pop(0)
    columns = [col.get_text(strip=True) for col in header_row.find_all("th")]

    data = []
    for row in rows:
        data.append([col.get_text(strip=True) for col in row.find_all("td")])

    df = pd.DataFrame(data, columns=columns)
    return df


def find_href_for_next_page(page: bytes) -> str:
    soup = BeautifulSoup(page, "html.parser")
    next_button = soup.find("li", class_="next")
    if next_button and next_button.a:
        href = next_button.a.get("href")
    else:
        href = ""
    return href
