import requests

url = 'http://172.17.0.1:8000/index.php'

files = {
	'file': ('trash.png', open('trash.png', 'rb'), 'image/png', {'Expires': '0'})
}

response = requests.post(url, files=files)

print(response.text)