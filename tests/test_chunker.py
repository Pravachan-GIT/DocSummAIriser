import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from app.services.chunker import clean_html, chunk_text

def test_clean_html():
    html = "<h1>Hello</h1><p>This is <b>Confluence</b> content.</p>"
    result = clean_html(html)
    print(f"Cleaned text: '{result}'")
    assert "<" not in result, "HTML tags still present"
    assert "Confluence" in result
    print("clean_html passed")

def test_chunk_text():
    text = "This is a test sentence. " * 50  # simulate a long page
    chunks = chunk_text(
        text=text,
        page_id="PAGE-001",
        page_title="Test Page",
        space_key="TEST"
    )
    print(f"Number of chunks: {len(chunks)}")
    print(f"First chunk preview: '{chunks[0]['text'][:80]}...'")
    print(f"Metadata: page_id={chunks[0]['page_id']}, space={chunks[0]['space_key']}")
    assert len(chunks) >= 1
    assert chunks[0]["page_id"] == "PAGE-001"
    assert "text" in chunks[0]
    print("chunk_text passed")

if __name__ == "__main__":
    test_clean_html()
    print("---")
    test_chunk_text()