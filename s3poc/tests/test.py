import requests

def test_object(url):
    h1 = requests.get(url)
    return(h1.status_code)

    # to add try catch raise error go on.