"""Read a file with a json object

Usage:
    bri_launcher <file_path>

Options:
    <file_path>: Path of file with pending BRI data
"""
import docopt
import json
import pytest


def read_data(data):
    """Receive data as a json object print it

    There should be the following fields inside data:

    { id1  :
         { expiration: <datetime> },
      id2 :
         { expiration: <datetime> }
    }

    """

    if not data:
        return
    for objid, elem in data.items():
        print("id: {}, obj: {}".format(objid, elem))


def main():
    arguments = docopt(__doc__)
    file_path = arguments["<file_path>"]
    with open(file_path) as json_file:
        data = json.load(json_file)
        read_data(data)


if __name__ == "__main__":
    main()



from datetime import datetime, timedelta

TODAY = datetime.now().isoformat()
TODAY_PLUS_1_DAYS = (datetime.now() + timedelta(days=1)).isoformat()
TODAY_LESS_1_DAYS = (datetime.now() + timedelta(days=-1)).isoformat()

FAKE_DATA = {
    1: {"expiration": TODAY},
    2: {"expiration": TODAY_LESS_1_DAYS},
    3: {"expiration": TODAY_PLUS_1_DAYS},
}


##################### TEST
# Execute with -s flag to see prints
# pytest -s read_json_from_file

def test_open(mocker):
    m = mocker.patch('builtins.open', mocker.mock_open(read_data='bibble'))
    h = open("foo")
    result = h.read()
    print("\nAbout to print whats in result\n")
    print(result)
    h.close()

    m.assert_called_once_with('foo')
    assert result == 'bibble'


def test_read_data(mocker):
    m = mocker.patch('builtins.open', mocker.mock_open(read_data=json.dumps(FAKE_DATA)))
    h = open("foo")
    result = h.read() # Fake data should be here
    print("\nAbout to print whats in result, should be whats in FAKE DATA")
    print(result)
    print("execute read data")
    read_data(json.loads(result))
    h.close()
    m = mocker.patch('builtins.open', mocker.mock_open(read_data=""))
    h = open("foo")
    result = h.read() # Fake data should be here
    print("execute read data")
    read_data(result)
    h.close()
