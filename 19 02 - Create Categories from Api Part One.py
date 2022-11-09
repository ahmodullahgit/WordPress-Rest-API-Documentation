import base64
import requests
api_url = 'https://countrycode.org/api/countryCode/countryMenu'
category_endpoints = 'https://localhost/project/python_project/wp-json/wp/v2/categories'

def wp_category_create(url, data):
    """
    This will create category in wordpress site.
    :param url: it is the url of wordpress rest api endpoints
    :param data: this is the data of categories(name, description, slug)
    :return: it will return category.
    """
    wp_user = 'python_codingo'
    wp_password = 'wU3J lr9j OLHW O7sC G1WK N5AD'
    wp_credential = f'{wp_user}:{wp_password}'
    wp_token = base64.b64encode(wp_credential.encode())
    wp_header = {'Authorization': 'Basic '+wp_token.decode('utf-8')}
    res = requests.post(url, json=data, headers=wp_header, verify=False)
    return res.status_code

response = requests.get(api_url)
if response.status_code == 200:
    countries = response.json()
    for country in countries:
        name = country.get('name')
        def slugify(text):
            """
            This will slugify your text.
            """
            slug = text.strip().lower().replace(' ','-')
            return slug
        slug = slugify(name)
        data = {
            'name': name,
            'slug': slug
        }
        wp_category_create(category_endpoints, data)
        print(name, 'category_printed')

