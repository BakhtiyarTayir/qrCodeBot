import requests

def creatQrCode(text, width, height):
    url = f"http://api.qrserver.com/v1/create-qr-code/?data={text}!&size={width}x{height}"
    response = requests.get(url)
    with open("qrCode.png", "wb") as f:
        f.write(response.content)


if __name__ == "__main__":
    creatQrCode("Hello World", 200, 200)