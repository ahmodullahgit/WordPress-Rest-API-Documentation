import requests
import base64

api_url = 'https://localhost/wordpress/wp-json/wp/v2/posts'

response = requests.get(api_url, verify=False)
if response.status_code == 200:
    post_data = response.json()
    all_id = []
    for data_ in post_data:
        all_id.append(data_.get('id'))

for post_id in all_id:
    post_end_points = f'https://localhost/wordpress/wp-json/wp/v2/posts/{post_id}'
    print(post_end_points)
    data = {
        'id': post_id,
        'force': True
    }
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
        return f'{post_id} has deleted successfully!'

    print(wp_posts_delete(post_end_points, data))