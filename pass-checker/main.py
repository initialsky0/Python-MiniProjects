import requests
import hashlib
import sys


def request_api_data(query_chars):
    # Security K anonymity
    url = 'https://api.pwnedpasswords.com/range/' + str(query_chars)
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(
            f'Error fetching: {res.status_code}, check the API and try again')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # check password if it exists in API response
    sha1_hasehd_pass = hashlib.sha1(
        str(password).encode('utf-8')).hexdigest().upper()
    first5_chars, tail = sha1_hasehd_pass[:5], sha1_hasehd_pass[5:]
    response = request_api_data(first5_chars)
    count = get_password_leaks_count(response, tail)
    return count


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(
                f"{'*' * len(password)} was found {count} times... you should change your password")
        else:
            print(f"{'*' * len(password)} was not found, you are safe")
    return 0


if __name__ == "__main__":
    main(sys.argv[1:])
