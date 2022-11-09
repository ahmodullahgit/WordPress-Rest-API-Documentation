import base64
import requests

api_url = 'https://localhost/project/python_project/wp-json/wp/v2/'

def wp_create(creating_type, data):
    wp_user = 'python_codingo'
    wp_password = 'wU3J lr9j OLHW O7sC G1WK N5AD'
    wp_credential = f'{wp_user}:{wp_password}'
    wp_token = base64.b64encode(wp_credential.encode())
    wp_header = {'Authorization':'Basic '+wp_token.decode('utf-8')}
    res = requests.post(f'{api_url}{creating_type}', json=data, headers=wp_header, verify=False)
    return res.status_code

data = {
    'title': '10 Best places in Afganistan',
    'content': 'If you are in Afganistan, you must visit these 10 places. These are enlisted below.',
    'categories': '7'
}

wp_create('posts', data)