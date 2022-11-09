import requests
import base64
api_url = 'https://localhost/project/python_project/wp-json/wp/v2/categories?per_page=100'

res = requests.get(api_url, verify=False)
if res.status_code == 200:
    post_data = res.json()
    categories = {}
    for data in post_data:
        categories[data['name']] = data['id']
all_id = list(categories.values())

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

end_point = 'https://localhost/project/python_project/wp-json/wp/v2/categories/'

for id in all_id:
    cat_end_point = f'{end_point}{id}'
    res = requests.get(cat_end_point, verify=False)
    content = res.json()
    cat_name = content.get('name')+' Places'
    cat_slug = content.get('slug')+'-places'
    cat_data = {'name': cat_name, 'slug': cat_slug}
    wp_category_create(cat_end_point, cat_data)

# country_name = post_data.get('name')
# country_slug = post_data.get('slug')
# name_update = country_name+' Places'
# slug_update = country_slug.strip().lower().replace(' ','-')
# data = {
#     'name': name_update,
#     'slug' : slug_update
# }
#
# end_points = api_url
# wp_user = 'python_codingo'
# wp_password = 'wU3J lr9j OLHW O7sC G1WK N5AD'
# wp_credential = f'{wp_user}:{wp_password}'
# wp_token = base64.b64encode(wp_credential.encode())
# wp_header = {'Authorization': 'Basic '+wp_token.decode('utf-8')}
# res = requests.post(end_points, headers=wp_header, json=data, verify=False)
# print(res.status_code)