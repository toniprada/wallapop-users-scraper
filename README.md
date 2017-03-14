# wallapop-users-scraper

Extract users data from Wallapop at scale.

The motivation for this project was to enable research about reputation in the Sharing Economy. In case you just need a simple client check [wallapopy](https://github.com/toniprada/wallapopy).

## Installing

```
$ pip install -r requirements.txt
```

## Configuring

Customize the Spider method ```user_ids_to_download``` to generate a set of Wallapop user ids to be downloaded (from example from a CSV file). Then just execute ```scrapy crawl wallapop``` and wait for all the users to be downloaded as _JSON_ files.
