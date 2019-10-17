def test_reporter():
    assert True

from reporter.header import create_header

def test_create_header():
    auth_list = [
        {"first": "Jojo",
         "last": "Juju",},
        {"first": "Dodo",
         "last": "Dudu",},
    ]
    
    res = create_header(auth_list)
    if not "Jojo" in res:
        raise ValueError('Firstname not in string')
    
    assert "Jojo" in res

def test_create_header_withloc():
    auth_list = [
        {"first": "Jojo",
         "last": "Juju",},
        {"first": "Dodo",
         "last": "Dudu",},
    ]
    
    res = create_header(auth_list, "NY")
    
    assert "NY" in res

def test_create_header_incomplete():
    auth_list = [
        {"first": "Jojo",},
        {"last": "Dudu",},
    ]
    
    res = create_header(auth_list, "NY")
    
    assert "Dudu" in res
    assert "Jojo" in res