import requests
import datetime


def calculate_date_week_ago():
    return datetime.date.today() - datetime.timedelta(weeks=1)


def get_trending_repositories(top_size):
    date_week_ago = calculate_date_week_ago()
    request_parametres = {'q': 'created:>={date_week_ago}'.format(date_week_ago=date_week_ago),
                          'sorted': 'stars'}
    weekly_repos = requests.get('https://api.github.com/search/repositories', params=request_parametres)
    return weekly_repos.json()['items'][:top_size]


if __name__ == '__main__':
    top_size = 20
    trending_repositories_created_for_a_week = get_trending_repositories(top_size)
    print("Today is: {today_date}".format(today_date=datetime.date.today()))
    print('Top {top_size} repositories created for last week: '.format(top_size=top_size))
    for number, repository in enumerate(trending_repositories_created_for_a_week, 1):
        print(number,
              'Name: {name} | '.format(name=repository['name']),
              'URL: {url} | '.format(url=repository['url']),
              'stars: {stars} | '.format(stars=repository['stargazers_count']),
              'Open issues: {open_issues}'.format(open_issues=repository['open_issues'])
              )
