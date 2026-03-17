from http.client import responses

import requests

def check_broken_links(links):
    broken_links = []

    for link in links:
        url = link.get_attribute("href")

        if url is None or url.startswith("javascript") or url.startswith("mailto"):
            continue

        try:
            response = requests.head(url, timeout=5)
            if response.status_code >= 400:
                broken_links.append((url, response.status_code))
        except requests.exceptions.RequestException:
            broken_links.append((url, "Request failed"))

    return broken_links
