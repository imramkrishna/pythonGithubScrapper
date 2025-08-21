from config import git
from api import getLanguages
import csv

def getData(username):
    user = git.get_user(username)
    print(user.name)
    print(user.bio)
    repoBuffer = list(user.get_repos())  # Convert to list for indexing
    if repoBuffer:
        print(repoBuffer[0])
    # Define CSV fieldnames
    fieldnames = ['name', 'full_name', 'html_url', 'description', 'created_at', 'stargazers_count', 'language']
    # Open CSV file and write all repo data
    with open('github_repos.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for repo in repoBuffer:
            try:
                print("name : " + repo.name)
                print("description : " + str(repo.description))
                print("language : " + repo.languages_url)
                languages = getLanguages(repo.languages_url)
                print("Languages : ", languages)
                print("stars : " + str(repo.stargazers_count))
                print("forks : " + str(repo.forks_count))
                writer.writerow({
                    'name': repo.name,
                    'full_name': repo.full_name,
                    'html_url': repo.html_url,
                    'description': repo.description,
                    'created_at': str(repo.created_at),
                    'stargazers_count': repo.stargazers_count,
                    'language': languages
                })
                print("\n")
            except Exception as e:
                print("Error processing repo: " + str(e))
    print("All repos processed.")