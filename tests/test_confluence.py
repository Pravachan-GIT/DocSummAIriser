from app.services.confluence_connector import get_all_pages
import os
from dotenv import load_dotenv

load_dotenv()

pages = get_all_pages(os.getenv("CONFLUENCE_SPACE_KEY"))

print(f"Found {len(pages)} pages")
for page in pages[:10]:  # print first 10
    print(f"- {page['title']} ({len(page['text'])} chars)")