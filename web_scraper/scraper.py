import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Blockchain'


class InvalidUrl(Exception):
  """[Throws on failure of request.get(url) in scraper.py module]

  Args:
      Exception ([CustomException]): [sends url passed and custom message]
  """
  def __init__(self, url_attempted, message):
    self.url_attempted = url_attempted
    self.message  = message
    

def get_citations_needed_count(url):
  """[returns sum of elements that contain 'citation needed' links]

  Args:
      url ([str]): [must be wikipedia.org page]

  Raises:
      InvalidUrl: [throws if requests.get(url) fails]

  Returns:
      [int]: [number of paragraphs that flagged as requiring citation]
  """
  try:
    response = requests.get(url)
  except:
    raise InvalidUrl(f'{url}:', 'is invalid or broken, check your arguments and try again')
  
  else:
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    result_to_filter = soup.findAll('a', title='Wikipedia:Citation needed')
    occurence = [note for note in result_to_filter]
    
    return len(occurence) if len(occurence) else f'footnote references to \'citation needed\' found at {url}'


def get_citations_needed_report(url):
  """[Returns a list of 'citation needed' dictionaries with attr. citation_[n]
  and the text of the surrounding paragraph element]

  Args:
      url ([str]): [must be to wikipedia.org page]

  Raises:
      InvalidUrl: [throws if request.get fails]

  Returns:
      [list(dict[1]...dict[2]...dict[n])]: [list of dictionaries with citation objects]
  """
  try:
    response = requests.get(url)
  except:
    raise InvalidUrl(f'{url}:', 'is invalid or broken, check your arguments and try again')
  else:

    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    anchor_to_filter = soup.findAll('a', title='Wikipedia:Citation needed')
    all_cite_needed = []
    occurence = {}

    for note in anchor_to_filter:
      needed = occurence[f'citation_{str(len(all_cite_needed ) + 1)} '] = str(note.parent.parent.parent.text).strip()
      all_cite_needed.append(needed)
  
    return all_cite_needed if anchor_to_filter else f'footnote references to \'citation needed\' found at {url}'
    
    
      

if __name__ == "__main__":
  pass