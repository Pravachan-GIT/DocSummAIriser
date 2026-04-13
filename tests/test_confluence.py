import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from app.services.confluence_connector import get_all_pages
import test_embeddings
from dotenv import load_dotenv

load_dotenv()

pages = get_all_pages(os.getenv("CONFLUENCE_SPACE_KEY"))

print(f"Found {len(pages)} pages")
for page in pages[:10]:  # print first 10
    print(f"- {page['title']} ({len(page['text'])} chars)")