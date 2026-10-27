import requests
from bs4 import BeautifulSoup


def decode_secret_message(url):
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    points = []

    for row in soup.find_all("tr"):
        cells = row.find_all(["td", "th"])

        if len(cells) < 3:
            continue

        try:
            x = int(cells[0].get_text(strip=True))
            char = cells[1].get_text(strip=True)
            y = int(cells[2].get_text(strip=True))

            if char:
                points.append((x, y, char))

        except ValueError:
            continue

    if not points:
        print("No coordinates found.")
        return

    max_x = max(x for x, y, char in points)
    max_y = max(y for x, y, char in points)
    min_x = min(x for x, y, char in points)
    min_y = min(y for x, y, char in points)

    width = max_x - min_x + 1
    height = max_y - min_y + 1

    grid = [[" "] * width for _ in range(height)]

    for x, y, char in points:
        grid[y - min_y][x - min_x] = char

    for row in reversed(grid):
        print("".join(row).rstrip())


if __name__ == "__main__":
    url = (
        "https://docs.google.com/document/d/e/"
        "2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
    )

    decode_secret_message(url)