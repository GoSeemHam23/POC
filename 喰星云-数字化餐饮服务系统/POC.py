#还未修改完成

import requests
import argparse

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    "Accept-Encoding": "gzip, deflate",
    "Accept": "*/*",
    "Connection": "keep-alive"
}

def check_keyword_in_response(url, keyword, output_file):
    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200 and keyword in response.text:
            print(f"Keyword '{keyword}' found in the response from {url}.")
        else:
            print(f"Keyword '{keyword}' not found or received non-200 status code from {url}.")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred with {url}: {e}")


def load_urls_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check if the HTTP response contains a specific keyword.")

    parser.add_argument("-u", "--url", type=str, help="Single URL to check.")
    parser.add_argument("-f", "--file", type=str, help="File containing a list of URLs, one per line.")
    parser.add_argument("-k", "--keyword", type=str, default="pwd", help="Keyword to search for in the response.")
    parser.add_argument("-o", "--output", type=str, help="File to export URLs where keyword is found.")

    args = parser.parse_args()

    # Load URLs either from the command line or from a file
    if args.url:
        urls = [args.url]
    elif args.file:
        urls = load_urls_from_file(args.file)
    else:
        print("You must provide either a single URL with -u or a file containing URLs with -f.")
        sys.exit(1)

    for url in urls:
        check_keyword_in_response(url, args.keyword,args.ouput_file)




