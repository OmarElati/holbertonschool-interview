# Count It!

Count It! is a Python script that counts the occurrences of given keywords in the titles of hot articles from a specified subreddit using the Reddit API. It provides a recursive function to achieve this task and a main script for easy usage.

## Usage

### Prerequisites
- Python 3.x
- `requests` library (install via `pip install requests`)

### Running the Script
To run the script, use the following command format:

```shell
python3 0-main.py <subreddit> <list of keywords>
```

For example:

```shell
python3 0-main.py programming 'react python java javascript scala no_results_for_this_one'
```

output:

```shell
java: 27
javascript: 20
python: 17
react: 17
scala: 4
```

### Note
- If no posts match the given subreddit or the subreddit is invalid, the script will print nothing.
- Keywords are case-insensitive.
- Duplicates of keywords are counted separately unless specified.
- Words with special characters like `java.`, `java!`, or `java_` are counted as separate occurrences.

## File Structure
- `0-count.py`: Contains the recursive function to count keywords in subreddit titles.
- `0-main.py`: Main script to run the program and handle user input.

## Contributing
Feel free to contribute to this project by submitting issues or pull requests.
