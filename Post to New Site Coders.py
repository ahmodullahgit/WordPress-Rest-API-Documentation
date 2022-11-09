import requests
import base64

api_url = 'https://localhost/wordpress/wp-json/wp/v2/'

def wp_create(creating_type, data):
    wp_user = 'coders'
    wp_password = 'Z2nJ mJkv zRT6 1GEN Ucff h1Ad'
    wp_credential = f'{wp_user}:{wp_password}'
    wp_token = base64.b64encode(wp_credential.encode())
    wp_header = {'Authorization':'Basic '+wp_token.decode('utf-8')}
    res = requests.post(f'{api_url}{creating_type}', json=data, headers=wp_header, verify=False)
    return res.status_code

post_data = {
    'title': 'How to Concentrate on Salah',
    'description': 'This post will help you to get better Salah.',
    'content': 'Understand it. Do you pray your Salah as if in a trance?Recite a Surah which you haven\'t recited before. When you recite the same Surah over and over again, you tend not to concentrate on it. Offer your Salah as if it\'s your last one. Empty yourself before you pray. Know your enemy.',
    'slug': 'how-to-concentrate-on-salah',
    'status': 'publish'
}
wp_create('posts', post_data)