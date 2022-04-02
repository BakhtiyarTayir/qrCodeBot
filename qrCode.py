import requests

def create_qr_code(text, width, height):
    url = f"http://api.qrserver.com/v1/create-qr-code/?data={text}!&size={width}x{height}"
    response = requests.get(url)
    return response.content


if __name__ == "__main__":
    create_qr_code("Hello World", 200, 200)