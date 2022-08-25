## is-bot

[![CI](https://github.com/romis2012/is-bot/actions/workflows/ci.yml/badge.svg)](https://github.com/romis2012/is-bot/actions/workflows/ci.yml)
[![Coverage Status](https://codecov.io/gh/romis2012/is-bot/branch/master/graph/badge.svg)](https://codecov.io/gh/romis2012/is-bot)
[![PyPI version](https://badge.fury.io/py/is-bot.svg)](https://pypi.python.org/pypi/is-bot)

Python package to detect bots/crawlers/spiders via user-agent string.
This is a port of the [isbot](https://github.com/omrilotan/isbot) JavaScript module.


## Requirements
- Python >= 3.7
- regex >= 2022.8.17

## Installation
```
pip install is-bot
```

## Usage

### Simple usage

```python
from is_bot import Bots

bots = Bots()

ua = 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/104.0.5112.79 Safari/537.36'
assert bots.is_bot(ua)

ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
assert not bots.is_bot(ua)
```

### Add/remove parsing rules

```python
from is_bot import Bots

bots = Bots()

# Exclude Chrome-Lighthouse from default bot list
ua = 'Mozilla/5.0 (Linux; Android 7.0; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4695.0 Mobile Safari/537.36 Chrome-Lighthouse'
assert bots.is_bot(ua)
bots.exclude(['chrome-lighthouse'])
assert not bots.is_bot(ua)

# Add some browser to default bot list
ua = 'SomeAwesomeBrowser/10.0 (Linux; Android 7.0)'
assert not bots.is_bot(ua)
bots.extend(['SomeAwesomeBrowser'])
assert bots.is_bot(ua)
```

### Get additional parsing information

```python
from is_bot import Bots

bots = Bots()

ua = 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0 SearchRobot/1.0'

# view the respective match for bot user agent rule
print(bots.find(ua))
#> Search

# list all patterns that match the user agent string
print(bots.matches(ua))
#> ['(?<! (ya|yandex))search', '(?<! cu)bot']
```

