import os
from atlassian import Confluence
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

def get_confluence_client():
    return Confluence(
        url=os.getenv("CONFLUENCE_URL"),
        username=os.getenv("CONFLUENCE_EMAIL"),
        password=os.getenv("CONFLUENCE_API_TOKEN"),
        cloud=True
    )

def get_all_pages(space_key: str) -> list[dict]:
    confluence = get_confluence_client()

    # Fetch all pages from the space
    pages = confluence.get_all_pages_from_space(
        space=space_key,
        start=0,
        limit=100,
        expand="body.storage"
    )

    results = []

    for page in pages:
        # Extract raw HTML content
        html_content = page["body"]["storage"]["value"]

        # Strip HTML tags to get plain text
        soup = BeautifulSoup(html_content, "html.parser")
        plain_text = soup.get_text(separator=" ", strip=True)

        # Skip empty pages
        if not plain_text.strip():
            continue

        results.append({
            "page_id":    page["id"],
            "title":      page["title"],
            "space_key":  space_key,
            "text":       plain_text,
            "url": os.getenv("CONFLUENCE_URL") + "/wiki/spaces/" + space_key + "/pages/" + page["id"]
        })

    return results