import base64
import requests

api_url = 'https://localhost/wordpress/wp-json/wp/v2/'

def wp_create(creating_type, data):
    wp_user = 'coders'
    wp_password = 'NXxB 2q1k ykn8 tBkC GUL0 zz0E'
    wp_credential = f'{wp_user}:{wp_password}'
    wp_token = base64.b64encode(wp_credential.encode())
    wp_header = {'Authorization':'Basic '+wp_token.decode('utf-8')}
    res = requests.post(f'{api_url}{creating_type}', json=data, headers=wp_header, verify=False)
    return res.status_code

country = 'UAE'
cat = '13'

data = {
    'title': f'10 Best places in {country}',
    'content': f'If you are in {country}, you must visit these 10 places. These are enlisted below.',
    'categories': f'{cat}',
    'status': 'publish'
}

wp_create('posts', data)