import requests
url = 'https://localhost/project/python_project/wp-json/wp/v2/categories?per_page=100'

res = requests.get(url, verify=False)

if res.status_code == 200:
    data = res.json()
    categories = {}
    for d in data:
        categories[d['name']] = d['id']
print(categories)