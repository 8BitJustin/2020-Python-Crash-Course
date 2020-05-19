import requests
import pygal
from pygal.style import NeonStyle as NS
from operator import itemgetter

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:15]:
    # Make a separate API call for each submission.
    url = (f'https://hacker-news.firebaseio.com/v0/item/'
           f'{str(submission_id)}.json')
    submission_r = requests.get(url)
    print(f"{submission_r.status_code}")
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': f'http://news.ycombinator.com/item?id={str(submission_id)}',
        'comments': response_dict.get('descendants', 0)
        }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['link']}")
    print(f"Comments: {submission_dict['comments']}")

titles, plot_dicts = [], []
for submission_dict in submission_dicts:
    titles.append(submission_dict['title'])
    plot_dict = {
        'value': submission_dict['comments'],
        'label': submission_dict['title'],
        'xlink': submission_dict['link'],
    }
    plot_dicts.append(plot_dict)

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
chart.title = 'Most-Commented on Hacker News'
chart.x_labels = titles

chart.add('', plot_dicts)
chart.render_to_file('hn_most_active.svg')
