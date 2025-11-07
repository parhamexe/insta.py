📸 Instagram Story Fetcher
A simple Python script that uses the instaloader library to fetch and display Instagram Stories for a given username.
It outputs story information (URLs, count, etc.) as JSON, making it easy to integrate with other applications or scripts.

🚀 Features


🔍 Fetches Instagram Stories from a target username


💾 Automatically saves and loads session for faster reuse


🔐 Prompts for Instagram login if no session file exists


🧱 Outputs clean, machine-readable JSON


⚙️ Works via command line



🧰 Requirements


Python 3.8 or higher


instaloader


Install dependencies:
pip install instaloader


🧑‍💻 Usage
Run the script from your terminal:
python story_fetcher.py <instagram_username>

Example:
python story_fetcher.py natgeo

If no saved session is found, you’ll be prompted to log in:
👤 insta username: your_username
🔐 password: your_password


🧾 Output Example

{
  "username": "natgeo",
  "story_count": 3,
  "stories": [
    "https://instagram.fxyz1-1.fna.fbcdn.net/v/t51.12442-15/e35/xyz.jpg",
    "https://instagram.fxyz1-1.fna.fbcdn.net/v/t51.12442-15/e35/abc.jpg",
    "https://instagram.fxyz1-1.fna.fbcdn.net/v/t51.12442-15/e35/123.jpg"
  ]
}


If an error occurs (e.g., user not found, private account, or login failure), the script returns a JSON error message:
{"error": "Can not get story!: Login required."}


⚠️ Notes


This script does not bypass Instagram privacy rules.
You can only view stories from public accounts or accounts you follow (if logged in).


Be mindful of Instagram’s Terms of Use.



📄 License
This project is licensed under the MIT License — feel free to use, modify, and distribute it.

💡 Author
Created by [Parham Sarkeshikian]
✨ Feel free to contribute or open issues!
