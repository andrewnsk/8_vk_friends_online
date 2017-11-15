# Watcher of Friends Online

A program that displays a list of users (friends) in the console,
being online in the social network Vkontakte (vk.com)


# How to Install

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```

Get an application ID from vk.com [dev](https://www.google.com "Developers page ")

### Set environment variable on Linux
```bash
$ export VFO_APP_ID=<vk.com application ID>
```


# Run on Linux
```bash
$ python vk_friends_online.py
```

## Example output
```bash
enter user login / e-mail / phone number > Some_user
Password: (will not be echoed) >
Friends online:
Pavel Durov
Darth Vader
Total friends online: 2
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
