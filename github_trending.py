import requests
import datetime


def calculate_date_week_ago():
    return datetime.date.today() - datetime.timedelta(weeks=1)


def get_trending_repositories(top_size):
    date_week_ago = calculate_date_week_ago()
    request_parametres ={
                            'q': 'created:>='+str(date_week_ago),
                            'sorted': 'stars'
                        }
    weekly_repos=requests.get('https://api.github.com/search/repositories', params=request_parametres)
    return weekly_repos.json()['items'][:top_size]


# С вашего позволения я закомментил данный метод, так как не придумал как же используя 2 метода
# использовать только один запрос к апи гитхаба
# def get_open_issues_amount(repo_owner, repo_name):
#     pass


if __name__ == '__main__':
    top_size = 20
    trending_repositories_created_for_a_week=get_trending_repositories(top_size)
    print("Today is: " + str(datetime.date.today()))
    print('Top ' + str(top_size) +' repositories created for last week: ')
    for number, repository in enumerate(trending_repositories_created_for_a_week, 1):
        print(number,
              'Name: ' + repository['name'] + ' |',
              'URL: ' + repository['url'] + ' |',
              'stars: ' + str(repository['stargazers_count']) + ' |',
              'Open issues: ' + str(repository['open_issues'])
         )
