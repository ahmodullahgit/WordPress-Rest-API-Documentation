import requests
import base64

api_url = 'https://localhost/wordpress/wp-json/wp/v2/'
wp_user = 'coders'
wp_password = 'NXxB 2q1k ykn8 tBkC GUL0 zz0E'
wp_credential = f'{wp_user}:{wp_password}'
wp_token = base64.b64encode(wp_credential.encode())
wp_header = {'Authorization':'Basic '+wp_token.decode('utf-8')}

differentiate = '6'
data = {
    'name' : f'Hajj is Ongoing!{differentiate}',
    'slug' : 'about-hajj-in-mecca',
    'description': f'Only interested people can Go!{differentiate}'
}

res = requests.post(api_url+'categories', json=data, headers=wp_header, verify=False)
if res.status_code == 201:
    print('Categories Created!')
else:
    print('Something Went Wrong!')
