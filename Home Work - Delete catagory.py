import requests
import base64

api_url = 'https://localhost/project/python_project/wp-json/wp/v2/categories?per_page=100'

response = requests.get(api_url, verify=False)
if response.status_code == 200:
    post_data = response.json()
    all_id = []
    for data_ in post_data:
        all_id.append(data_.get('id'))

for cat_id in all_id:
    cat_end_points = f'https://localhost/project/python_project/wp-json/wp/v2/categories/{cat_id}'
    data = {
        'id': cat_id,
        'force': True
    }
    def wp_category_delete(url, data):
        """
        This will delete category from WordPress site.
        :param url: it is the url of WordPress rest api endpoints
        :param data: this is the data of category id and force argument
        :return: it will remove category.
        """
        wp_user = 'python_codingo'
        wp_password = 'wU3J lr9j OLHW O7sC G1WK N5AD'
        wp_credential = f'{wp_user}:{wp_password}'
        wp_token = base64.b64encode(wp_credential.encode())
        wp_header = {'Authorization': 'Basic '+wp_token.decode('utf-8')}
        res = requests.delete(url, json=data, headers=wp_header, verify=False)
        return f'{cat_id} has deleted successfully!'

    print(wp_category_delete(cat_end_points, data))
