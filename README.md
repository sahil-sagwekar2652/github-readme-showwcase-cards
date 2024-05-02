# Showwcase Readme Cards
[![My Skills](https://skillicons.dev/icons?i=py,flask,vercel,githubactions&theme=light)](https://skillicons.dev)

## How to Use 

1. Add the following code to your README.md file.
```md
<!-- BEGIN SHOWWCASE_PROFILE>
<!-- END SHOWWCASE_PROFILE>
```

2. Get the Showwcase API key from [here](https://showwcase.com/settings/api-keys).

3. Add the API key as a GitHub secret with the name `SHOWWCASE_API_KEY`. You can do this by going to `Settings > Secrets` and clicking on `New repository secret`. Here is a [video tutorial](https://youtu.be/IuT0Ua7V4xA) on how to do this.

4. Add a new workflow in the .github folder. You can do this by going to `.github/workflows` and clicking on `New file` and add the following code to it. Replace your username in the above code and commit the file.
```yml
name: Showwcase Profile Card
on:
  schedule:
    # Runs every day at 12:00
    - cron: "0 12 * * *"
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: sahil-sagwekar2652/github-readme-showwcase-cards@main
        id: showwcase-cards
        with: 
          api_key: ${{ secrets.SHOWWCASE_API_KEY }}
          theme: "dark"
          username: <your showwcase username>
```

## Example 

<!-- BEGIN SHOWWCASE_PROFILE -->
![sahil-sagwekar2652](https://github-readme-showwcase-cards.vercel.app/?name=Sahil+Sagwekar&username=sahil-sagwekar2652&headline=Student+%7C+Developer+%7C+Open+Source+Enthusiast+and+Technical+Writer.&avatar=https%3A%2F%2Fprofile-assets.showwcase.com%2F1680201821508.jpg&profile_url=sahil-sagwekar2652.showwcase.com&resume=https%3A%2F%2Fresume.showwcase.com%2Fsahil-sagwekar2652.pdf&theme=dark)
<!-- END SHOWWCASE_PROFILE -->

##### Inspired by - https://github.com/DenverCoder1/github-readme-youtube-cards
