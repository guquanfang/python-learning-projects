import sys
from github_api import get_user, get_user_repositories

def main():
      if len(sys.argv) < 2:
            print("Usage: python main.py <github_username>")
            sys.exit(1)

username = sys.argv[1]   

data = get_user(username)

if data is None:
        print(f"Github user '{username}' not found.")
        sys.exit(1)

print(f"User: {data['login']}")
print(f"ID: {data['id']}")
print(f"Flowers: {data['followers']}")

repos_data = get_user_repositories(username)

if repos_data is None:
    print(f"Could not retrieve repositories for user '{username}'.")
    sys.exit(1)

print("\n-- Repositories --")

for repo in repos_data[:5]:  # Display only the first 5 repositories
    print(repo["name"])


if __name__ == "__main__":
    main()
