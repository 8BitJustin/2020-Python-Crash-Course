import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS, \
    NeonStyle as NS

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code: ", r.status_code)
if r.status_code == 200:
    print('Success.')

# Store API response in a variable.
response_dict = r.json()
print(f"Total Python repositories: {response_dict['total_count']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# Create visualization. Commented out to utilize NeonStyle.
# my_style = LS('#228b22', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=NS)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')