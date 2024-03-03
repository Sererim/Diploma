import requests as req
import argparse


def upload_image(image_path):
    url: str = "http://localhost:5000/image"
    files = {'image': open(image_path, 'rb')}
    response = req.post(url, files=files)
    print(response.text)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog="Simple CLI interface for work with food recognition server.",
        description="Program gets a path to an image and server url,  \
        sends image there and gets a response, food class"
    )
    parser.add_argument("image_path", nargs="?", default="C:\\Users\\Admin\\Downloads\\Rice.jpg")
    args = parser.parse_args()
    upload_image(args.image_path)
    