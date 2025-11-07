import instaloader
import json
import sys

if len(sys.argv) < 2:
    print(json.dumps({"error": "please type username!"}))
    sys.exit(1)

target_username = sys.argv[1]


L = instaloader.Instaloader()

try:
    L.load_session_from_file() 
except:
    try:
        username = input("👤 insta username: ")
        password = input("🔐 password ")
        L.login(username, password)
        L.save_session_to_file()
    except Exception as e:
        print(json.dumps({"error": f"Login failed!{str(e)}"}))
        sys.exit(1)

try:
    profile = instaloader.Profile.from_username(L.context, target_username)
    story_urls = []

    for story in L.get_stories(userids=[profile.userid]):
        for item in story.get_items():
            story_urls.append(item.url)

    print(json.dumps({
        "username": target_username,
        "story_count": len(story_urls),
        "stories": story_urls
    }, indent=2, ensure_ascii=False))

except Exception as e:
    print(json.dumps({"error": f"Can not get story!: {str(e)}"}))
    sys.exit(1)