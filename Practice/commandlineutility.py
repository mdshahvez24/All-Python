import argparse
import requests

parse = argparse.ArgumentParser()

parser.add_argument("url", help="File url to download")
parse.add_argument("output",
help="by which name u want to save 2")

args = parser.parse.args()

print(args.url)
print(args.output)
download_file(args.url,args,output)


def download_file(url, local_filename):
    local_filename= url.split('/')[1]

    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):

                f.write(chunk)

    return loacal_filename
