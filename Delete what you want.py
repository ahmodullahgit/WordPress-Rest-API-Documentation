import requests
import base64

api_url = 'https://localhost/wordpress/wp-json/wp/v2/'
response = requests.get(api_url, verify=False)
if response.status_code == 200:
    post_data = response.json()
    all_id = []
    for data_ in post_data:
        all_id.append(data_.get('id'))
    print(all_id)
for post_id in all_id:
    data = {
        'id': post_id,
        'force': True
    }

def delete_what_you_want(deletion_type, url, data):
    """
    This will delete category from WordPress site.
    :param url: it is the url of WordPress rest api endpoints
    :param data: this is the data of category id and force argument
    :return: it will remove category.
    """
    wp_user = 'coders'
    wp_password = 'NXxB 2q1k ykn8 tBkC GUL0 zz0E'
    wp_credential = f'{wp_user}:{wp_password}'
    wp_token = base64.b64encode(wp_credential.encode())
    wp_header = {'Authorization': 'Basic ' + wp_token.decode('utf-8')}
    res = requests.delete(api_url+f'{deletion_type}', json=data, headers=wp_header, verify=False)
    # post_end_points = f'https://localhost/wordpress/wp-json/wp/v2/{deletion_type}/{post_id}'
    return res

print(delete_what_you_want('categories', api_url, data))