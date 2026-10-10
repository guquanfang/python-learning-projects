import sys
import requests 

def get_user(username):
    url = "https://api.github.com/users/" + username
    response = requests.get(url)
    if response.status_code != 200:
        return None
      
        
    return response.json()

def get_user_repositories(username):
    repos_url = "https://api.github.com/users/" + username + "/repos"
    repos_response = requests.get(repos_url)
    if repos_response.status_code != 200:
        return None
    return repos_response.json()


