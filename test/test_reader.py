import sys
from pathlib import Path

# let the test find project_os.py, which is one folder up
sys.path.insert(0, str(Path(__file__).parent.parent))

from project_os import read_document

HERE = Path(__file__).parent          # the test/ folder


def test_reads_txt_file():
    text = read_document(str(HERE / "README.txt"))
    assert "Cryptography" in text     # a word that is in README.txt


def test_reads_pdf_file():
    text = read_document(str(HERE / "sample.pdf"))
    assert text.strip() != ""         # got some text back


def test_unsupported_type_returns_none():
    assert read_document("notes.html") is None