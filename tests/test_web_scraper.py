import pytest
from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report, InvalidUrl

# reasearch pytest requests_mock for future instances where I need to test how my script interacts with hhtp requests. 

def test_citation_needed_report():
    url = 'https://en.wikipedia.org/wiki/Blockchain'
    cite_1 = {
        "citation_1":'Permissioned blockchains use an access control layer to govern who has access to the network.[41] In contrast to public blockchain networks, validators on private blockchain networks are vetted by the network owner. They do not rely on anonymous nodes to validate transactions nor do they benefit from the network effect.[citation needed] Permissioned blockchains can also go by the name of \'consortium\' blockchains.[citation needed]'
        }

    cite_2 = {
        'citation_2':'Permissioned blockchains use an access control layer to govern who has access to the network.[41] In contrast to public blockchain networks, validators on private blockchain networks are vetted by the network owner. They do not rely on anonymous nodes to validate transactions nor do they benefit from the network effect.[citation needed] Permissioned blockchains can also go by the name of \'consortium\' blockchains.[citation needed]'
    }
    
    assert get_citations_needed_report(url) == [cite_1['citation_1'], cite_2['citation_2']]


def test_get_citation_needed_count():
    url = 'https://en.wikipedia.org/wiki/Blockchain'
    assert get_citations_needed_count(url) == 2


def test_citation_needed_count_invalid_url():
    url = 'https://en.wikipedia.jrg/wiki/Blockchain'

    with pytest.raises(InvalidUrl) as excinfo:
        get_citations_needed_count(url)

    assert 'https://en.wikipedia.jrg/wiki/Blockchain:is invalid or broken, check your arguments and try again' == excinfo.value.url_attempted + excinfo.value.message

def test_citation_needed_report_invalidurl():
    url = 'https://en.wikipedia.jrg/wiki/Blockchain'

    with pytest.raises(InvalidUrl) as excinfo:
        get_citations_needed_count(url)

    assert 'https://en.wikipedia.jrg/wiki/Blockchain:is invalid or broken, check your arguments and try again' == excinfo.value.url_attempted + excinfo.value.message


def test_citation_count_none_found():
    url = 'https://en.wikipedia.org/wiki/Society'
    assert get_citations_needed_count(url) == f'footnote references to \'citation needed\' found at {url}'


def test_citation_report_none_found():
    url = 'https://en.wikipedia.org/wiki/Society'
    assert get_citations_needed_report(url) == f'footnote references to \'citation needed\' found at {url}'





