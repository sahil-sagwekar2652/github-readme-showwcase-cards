from argparse import ArgumentParser
import requests
import urllib.parse


class profileParser:
    def __init__(self, api_key: str, username: str, theme: str):
        self.api_key = api_key
        self.username = username
        self.theme = theme  # light or dark
        self.url = "https://cache.showwcase.com/user/" + self.username
        self.base_url = "https://github-readme-showwcase-cards.vercel.app/"

    def get_data(self):
        headers = {'Authorization': 'Bearer ' + self.api_key}
        response = requests.get(self.url, headers=headers)
        return response.json()

    def parse_profile(self):
        data = self.get_data()
        params = {
            "name": data["displayName"],
            "username": self.username,
            "headline": data["headline"],
            "avatar": data["profilePictureKey"],
            "profile_url": data["domain"],
            "resume": data["resume"],
            "theme": self.theme,
        }
        card_content = f"![{params['username']}]({self.base_url}?{urllib.parse.urlencode(params)})"  # noqa: E501
        return card_content


class FileUpdater:
    """Update the readme file"""

    @staticmethod
    def update(readme_path: str, comment_tag: str, replace_content: str):
        """Replace the text between the begin and end tags with the replace content"""  # noqa: E501
        begin_tag = f"<!-- BEGIN {comment_tag} -->"
        end_tag = f"<!-- END {comment_tag} -->"

        with open(readme_path, "r") as readme_file:
            readme = readme_file.read()

        begin_index = readme.find(begin_tag)
        end_index = readme.find(end_tag)

        if begin_index == -1 or end_index == -1:
            raise RuntimeError(f"Could not find tags {begin_tag} and {end_tag} in {readme_path}")  # noqa: E501

        readme = f"{readme[:begin_index + len(begin_tag)]}\n{replace_content}\n{readme[end_index:]}"  # noqa: E501
        with open(readme_path, "w") as readme_file:
            readme_file.write(readme)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '--api_key',
        dest='api_key',
        type=str,
        help='API key for the Showwcase API',
        required=False,
        default="9dd5899c1b71c7aad37c207bc781d86674db487ac4675b034e",
    )
    parser.add_argument(
        '--username',
        dest='username',
        type=str,
        help='Username of the profile to fetch',
        required=True,
        )
    parser.add_argument(
        '--theme',
        type=str,
        choices=['light', 'dark'],
        help='Theme of the profile to fetch',
        default='dark',
        )
    parser.add_argument(
        '--readme_path',
        type=str,
        help='Path to the readme file',
        default='README.md',
        )
    args = parser.parse_args()

    profile = profileParser(args.api_key, args.username, args.theme)
    card_content = profile.parse_profile()

    FileUpdater.update(args.readme_path, "SHOWWCASE_PROFILE", card_content)
