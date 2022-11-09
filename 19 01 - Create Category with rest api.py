import requests
import base64

api_url = 'https://localhost/project/python_project/wp-json/wp/v2/'
wp_user = 'python_codingo'
wp_password = 'wU3J lr9j OLHW O7sC G1WK N5AD'
wp_credential = f'{wp_user}:{wp_password}'
wp_token = base64.b64encode(wp_credential.encode())
wp_header = {'Authorization':'Basic '+wp_token.decode('utf-8')}

data = {
    'name' : 'Hajj is Ongoing!',
    'slug' : 'about-hajj-in-mecca',
    'description': 'Only interested people can Go!'
}

res = requests.post(api_url+'categories', json=data, headers=wp_header, verify=False)
if res.status_code == 201:
    print('Categories Created!')
else:
    print('Something Went Wrong!')
