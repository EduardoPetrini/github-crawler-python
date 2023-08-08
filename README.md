# GitHub Crawler
This repository contains a Python script that uses the GitHub API to search for JavaScript repositories with "vscode-extension" in the name, description, or readme. The script then sorts the results by stars (ranking) and downloads the top 100 repositories to a local folder.

To use the script, you will need to create a GitHub personal access token and set the environment variable `GITHUB_TOKEN` to the value of your token. You can create a personal access token at https://github.com/settings/tokens.

Once you have set the `GITHUB_TOKEN` environment variable, you can run the script by executing the following command:

```
python main.py
```

The script will output the following information for each repository:

* Repository name
* Description
* Stars
* URL

The script will also clone the top 100 repositories to the local folder `repos`.

Here is a step-by-step explanation of the code in `main.py`:

1. The first line imports the `requests`, `os`, and `subprocess` modules.
2. The second line defines the environment variable `GITHUB_TOKEN`.
3. The third line defines the folder `REPOS_FOLDER`.
4. The fourth line creates a header object with the authorization token.
5. The fifth line defines the GitHub API endpoint for repository search.
6. The sixth line defines the search query parameters.
7. The seventh line makes a request to the GitHub API endpoint and stores the response in the variable `response`.
8. The eighth line checks if the response status code is 200. If it is, the script proceeds to the next step. If not, the script prints an error message and exits.
9. The ninth line loads the JSON data from the response into the variable `data`.
10. The tenth line loops over the items in the `data` array. For each item, the script prints the following information:
    * Repository name
    * Description
    * Stars
    * URL
    * The script then clones the repository to the local folder `repos`.
11. The eleventh line prints a divider.
12. The twelfth line ends the script.
