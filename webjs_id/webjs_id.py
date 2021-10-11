import argparse
import json      
import os
import requests


PUBWWW_API_URL = "https://publicwww.com/js/"
OUTPUT_TYPE = "/?export=csvu"
PUBWWW_API_KEY = os.environ.get("PUB_WWW_API_KEY")


def request_pubwww_api(url:str , query: str) -> requests.Response:
    """Make request to PublicWWW API

    Args:
        url ([str]): PublicWWW API URL
        query ([str]): Search query taken from JSON file

    Returns:
        requests.Response: Content of request to API
    """  
    try:
        api_request = requests.get(
            url 
            + query
            + "+filetype:js" 
            + OUTPUT_TYPE  
            + PUBWWW_API_KEY,
            timeout=300,
        )

        return api_request.content.decode("utf-8")

    except requests.RequestException as err:

        print(f"Problem with PublicWWW request: {err}")


def fetch_api_data(config_file) -> None:
    """Get API data

    Args:
        config_file ([file]): JSON config file in folder

    Returns:
        None
    """
    with open(config_file, "r+") as f:
        queries = json.load(f)

    global response

    for _, v in queries.items():
        for data in v:
            desc = data['description']
            query = data['query']
            print(f'Trying query for: {desc}...\n')

            response = request_pubwww_api(PUBWWW_API_URL, query=query)

            

def format_api_data() -> str:
    """Take results of request to API, and return data in JSON format

    Returns:
        str: JSON output of results from search queries
    """     
    temp_url = []

    for lines in response.splitlines():
        text_data = lines.split(';')

        temp_url.append({
            'domain': text_data[0],
            'rank': text_data[1],
            'snippet': text_data[2] if len(text_data) >= 3 else ''
        })
        json_data = json.dumps(temp_url, indent=4)
    
    return json_data


def main():

    menu = r"""
 _    _      _       ___ _____ ___________ 
| |  | |    | |     |_  /  ___|_   _|  _  \
| |  | | ___| |__     | \ `--.  | | | | | |
| |/\| |/ _ \ '_ \    | |`--. \ | | | | | |
\  /\  /  __/ |_) /\__/ /\__/ /_| |_| |/ / 
 \/  \/ \___|_.__/\____/\____/ \___/|___/  
                           ______          
                          |______|         
------------------------------------------------------------------------------------
Based on a set of search queries, this tool will connect to the PublicWWW API and return 
a list of websites possibly running malicious JavaScript code.

"""

    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter, description=menu
    )
    parser.add_argument("-q", "--query_file", help="JSON file", required=True)
    parser.add_argument("-o", "--output_type", help="Output file to write")
    parser.add_argument("-c", "--csv", help="Output to csv")

    args = parser.parse_args()

    if args.query_file:
        print(menu)
        fetch_api_data(args.query_file)
        print(format_api_data())


if __name__ == "__main__":
    main()
