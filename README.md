![alt text](<logo.webp>)
# GitHub Shortname Wordlist Generator

This script automates the process of fetching potential file and directory names based on partial names output by a shortscanning tool for Microsoft IIS Tilde vulnerability. It uses a Selenium-driven Chrome browser to perform searches on GitHub.

## Features

- Automates Chrome driver installation.
- Uses a logged-in Chrome profile for authenticated GitHub searches.
- Semi-automated fetching of potential file and directory names from GitHub.
- Supports silent mode to suppress banner output.

## Requirements

- [Python 3.x](https://www.python.org/downloads/)
- [Google Chrome](https://www.google.com/chrome/)
- [chromedriver-autoinstaller](https://pypi.org/project/chromedriver-autoinstaller/)
- [selenium](https://pypi.org/project/selenium/)
- [selenium-wire](https://pypi.org/project/selenium-wire/)

## Installation 🏢

1. Clone the repository or download the script.
2. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```
    or

    ```sh
    pip install chromedriver-autoinstaller selenium selenium-wire
    ```

## Usage 🛠️

```sh
python gsnw.py <search_query> [output_file] [-silent]

<search_query>: The search query to use for GitHub code search.

[output_file]: (Optional) The output file to save the results.

-silent: (Optional) Suppress the banner.
```

# Example ⚡

```sh
python script.py sapmai output.txt -silent
```

This will search for "admin" in GitHub code and save the results to output.txt without displaying the banner.


## Important Notes 🪄

Ensure you are logged in to GitHub on the specified Chrome profile for authenticated searches.

The script currently runs in headless mode by default. If you need to see the browser actions, you can comment out the --headless argument in the chrome_options setup.

## Disclaimer ⚠️

This script is provided "as is" without any warranties. Use it at your own risk.
Author

## Socials
Find me on X (Twitter) [@retkoussa](https://x.com/retkoussa)
