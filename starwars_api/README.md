# Star Wars API

This script fetches and prints all characters of a Star Wars movie using data from the Star Wars API.

## Requirements

- Node.js (version 10.14.x)
- npm (Node Package Manager)
- Ubuntu 14.04 LTS

## Installation

1. Install Node.js and npm:

```bash
curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
sudo apt-get install -y nodejs
```

2. Install semistandard and request modules:

```bash
sudo npm install semistandard --global
sudo npm install request --global
```

3. Clone the repository:

```bash
git clone https://github.com/your-username/holbertonschool-interview.git
```

4. Navigate to the project directory:

```bash
cd holbertonschool-interview/starwars_api
```

## Usage

Run the script with the movie ID as an argument:

```bash
./0-starwars_characters.js 3
```

Replace `3` with the desired movie ID.
