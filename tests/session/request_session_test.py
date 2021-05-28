from carpathian_beer.session.request_session import RequestSession


def test_session():
    session = RequestSession()
    assert session.get("https://www.google.com/").status_code == 200
    assert session.get("https://api.punkapi.com/v2/beers/a").status_code != 200
