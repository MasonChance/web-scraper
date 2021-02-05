# Web-scraper 101
Module contains functions for scraping wikipedia pages and finding the number of times the 'citation needed' notation occurs as well as functionality for seeing the text of the paragraph surrounding each instance of the notation. 

## Dependencies libraries, and environments:

[tool.poetry.dependencies]
python = "^3.9"
pytest = "^6.2.2"
beautifulsoup4 = "^4.9.3"
requests = "^2.25.1"

[tool.poetry.dev-dependencies]

black = {version = "^20.8b1", allow-prereleases = true}
pylint = "^2.6.0"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"



## Canvas Assignment version and feature tasks:
[Scraper Assignment task PR]()

1. Scraper should report number of citations needed for the page
  - method w/signature: `get_citation_needed_count(url: str)->int` will only work for [wikipedia](https://en.wikipedia.org/wiki/Main_Page) pages.returns integer. 

2. scraper should identify those cases and include relevant passages:
  - method w/signature: `get_citation_needed_report(url: str)-> list(dict[n])` returns list of dictionary instances. dictionary is in the form `{citation_*number* : content}`
  where *number* is the index position plus 1 reflecting the actual count of citations: contents is the text of the paragraph element surrounding the 'citation needed' notation.

