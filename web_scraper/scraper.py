import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Blockchain'


class InvalidUrl(Exception):
  """For use with request module, covers mis-spellings and broken links
  returns an fstring in the format `url passed:{url_attepted}: {message}`

  Args:
      Exception ([ValueError]): [indicates that the url is invalid or broken]
  """
  def __init__(self, url_attempted, message):
    self.url_attempted = url_attempted
    self.message  = message
    

# https://en.wikipedia.org/wiki/Blockchain
def get_citations_needed_count(url):
  """[Scrapes Wikipediapage for <a> tags with the title='Wikipedia:Citation needed' and appends to a List, returns the len(List). will not work for other sites where citations may be noted inline.]

  Args:
      url ([str]): [url of page to scrape data from]
  """
  try:
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    result_to_filter = soup.findAll('a', title='Wikipedia:Citation needed')
    occurence = []
    for note in result_to_filter:
      occurence.append(note)
    return len(occurence) if len(occurence) else f'footnote references to \'citation needed\' found at {url}'
    
  except:
    raise InvalidUrl(f'{url}:', 'is invalid or broken, check your arguments and try again')
  

def get_citations_needed_report(url):
  """[returns list of citation_needed objects with the attribute: citation_num assigned to the surrounding paragraph of the citation needed link found in Wikipedia pages. 

  Args:
      url ([str]): [url of page to scrape data from]

  """
  try:
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    anchor_to_filter = soup.findAll('a', title='Wikipedia:Citation needed')
    occurence = {}
    needed = occurence[f'citation_{str(len(all_cite_needed ) + 1)}'] = str(note.parent.parent.parent.text).strip()

    all_cite_needed = [all_cite_needed.append(needed) for note in anchor_to_filter]
  
    return all_cite_needed if anchor_to_filter else f'footnote references to \'citation needed\' found at {url}'
    
  except:
    raise InvalidUrl(f'{url}:', 'is invalid or broken, check your arguments and try again')
    
      
      
      
    


if __name__ == "__main__":
  get_citations_needed_report(url)