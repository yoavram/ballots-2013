import re

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def get_ballots(f):
    BALLOT_DATA_RE = re.compile(
        r'(\d\d)\n(.*)\n(\d\d\d\d)\n(.*)\n([\d\.]+)\n(.*)\n(.*)')
    m = re.findall(BALLOT_DATA_RE, f)
    for x in m:
        commitee_id, commitee, city_id, city, ballot_id, ballot_address, ballot_location = x
        print commitee_id, commitee, city_id, city, ballot_id, ballot_address, ballot_location

f = read_file('ballots.txt')
data = get_ballots(f)
print data
