import requests
import base64

def data_collect(type):
    """
    This will create an url according to your input -e.g. (type),('posts'),('categories')
    :param type: type takes an input that define, from where you want to collect data -e.g. -('posts'),('categories')
    :return: it will return an url.
    """
    api_url = f'https://localhost/wordpress/wp-json/wp/v2/{type}/'
    return api_url
request_url = data_collect('categories')
res = requests.get(request_url, verify=False)
if res.status_code == 200:
    data = res.json()
    all_id = []
    for d in data:
        input_id = d.get('id')
        all_id.append(input_id)

def delete_anything_using_id(delete_type, any_id):
    """

    :param delete_type: it will take a type which you want to delete. -e.g. -('posts'),('categories')
    :param any_id: it takes id for deletion.
    :return: it will delete your desirable section.
    """
    end_points = f'https://localhost/wordpress/wp-json/wp/v2/{delete_type}/{any_id}'
    return end_points
for id in all_id:
    data = {'id': id, 'force': True}
    result = delete_anything_using_id('categories', id)
    def wp_posts_delete(url, data):
        """
        This will delete posts from WordPress site named as 'Coders.
        :param url: it is the url of WordPress rest api endpoints
        :param data: this is the data of post id and force argument
        :return: it will remove posts.
        """
        wp_user = 'coders'
        wp_password = 'NXxB 2q1k ykn8 tBkC GUL0 zz0E'
        wp_credential = f'{wp_user}:{wp_password}'
        wp_token = base64.b64encode(wp_credential.encode())
        wp_header = {'Authorization': 'Basic '+wp_token.decode('utf-8')}
        res = requests.delete(url, json=data, headers=wp_header, verify=False)
        return f'{id} has deleted successfully!'

    print(wp_posts_delete(result, data))