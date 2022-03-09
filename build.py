"""
python port of https://github.com/wooorm/html-tag-names/blob/main/build.js
"""
from bs4 import BeautifulSoup
import requests
import re

from HtmlTagNames import html_tag_names

tags = html_tag_names

# Crawl W3C.
page = requests.get("https://w3c.github.io/elements-of-html/")
soup = BeautifulSoup(page.content, "html.parser")

for row in soup.find_all(attrs={"scope": "row"}):
    tag = row.get_text().strip()

    if not re.search(r"\s", tag) and tag not in tags:
        tags.append(tag)

# Crawl WHATWG.
page = requests.get("https://html.spec.whatwg.org/multipage/indices.html")
soup = BeautifulSoup(page.content, "html.parser")

for row in soup.select("tbody th > code"):
    tag = row.get_text().strip()
    tagid = row.get("id")

    if tagid and tagid.split(":")[0] == "elements-3" and tag not in tags:
        tags.append(tag)

tags.sort()
with open("HtmlTagNames/html_tag_names.py", "w+", encoding="utf8") as built:
    built.write(
        f"""\"\"\"
List of known HTML tag names.
\"\"\"

html_tag_names = {tags}"""
    )
