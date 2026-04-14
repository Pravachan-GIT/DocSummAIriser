# from bs4 import BeautifulSoup
from llama_index.core.node_parser import SentenceSplitter

# def clean_html(html_content: str) -> str:
#     soup = BeautifulSoup(html_content, "html.parser")
#     return soup.get_text(separator=" ", strip=True)

def chunk_text(text: str, page_id: str, page_title: str, space_key: str) -> list[dict]:
    splitter = SentenceSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)
    
    return [
        {
            "text": chunk,
            "page_id": page_id,
            "page_title": page_title,
            "space_key": space_key,
        }
        for chunk in chunks
    ]