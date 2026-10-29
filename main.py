import requests
import re
from datetime import date

# Simulate fetching trending AI repos from GitHub API (replace with real search later)
API_URL = "https://api.github.com/search/repositories"
QUERY = "topic:ai created:>{}".format(date.today().replace(day=1))
headers = {"Accept": "application/vnd.github+json"}

try:
    resp = requests.get(API_URL, params={"q": QUERY, "sort": "stars", "order": "desc", "per_page": 5}, headers=headers, timeout=10)
    repos = resp.json().get("items", [])
except Exception:
    repos = []

# Fallback sample data if network fails
if not repos:
    repos = [{"full_name": "example/new-model", "description": "A new AI model"}]

# Extract potential new terms: repo names, words in descriptions, tags
terms = set()
for repo in repos:
    name = repo.get("full_name", "").split("/")[-1]
    terms.add(name)
    desc = repo.get("description") or ""
    # Simple keyword extraction: camelCase and hyphenated parts
    words = re.findall(r'[a-z]+(?:-[a-z]+)*', desc.lower())
    terms.update(words[:10])

# Print a daily radar summary
print(f"🚀 AI Trend Radar for {date.today().isoformat()}")
print("New model/product names detected:")
for t in sorted(terms)[:10]:
    print(f"  - {t}")
print("Source: GitHub trending AI repos (sample)")