import requests


def number_of_subscribers(subreddit):
    """Function returns number of subscribers on a subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        if response.status_code == 200:
            results = response.json().get("data", {})
            subscribers = results.get("subscribers", 0)
            return subscribers
        elif response.status_code == 404:
            return 0
        else:
            print("Unexpected response: {}".format(response.status_code))
            return 0
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
        return 0
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
        return 0
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
        return 0
    except requests.exceptions.RequestException as err:
        print("Something went wrong:", err)
        return 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
