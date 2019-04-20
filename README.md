# dry-electrics-delegator
Some Dry Electrics Delegation

![wet elecs](https://raw.githubusercontent.com/ryan-brown/dry-electrics-delegator/master/app/static/logo.png)

## Client

- Download the latest [bg.sh](https://raw.githubusercontent.com/ryan-brown/dry-electrics-delegator/master/bg.sh) script to `/some/path/bg.sh`
- Run `crontab -e`
- Enter the following with correct path and name, and save:

```
* * * * * sh /some/path/bg.sh YourName
```

## Server
The server consists of:

- a sqlite file `database.db` where all offline data is stored
- a redis instance where cache/queue data is stored
- flask server `run.py` that collects datapoints and displays them from redis
- `processor.py` which moves data from the queue into the sqlite file

To create the database:
```
sqlite3 database.db < schema.sql
```

Running redis:
```
docker-compose up
```

Running the server:
```
pip3 install -r requirements.txt
FLASK_APP=main.py FLASK_DEBUG=1 python3 -m flask run --host=0.0.0.0 --port=5002
```

Adding processor to a crontab on the server (every 5 minutes):
```
*/5 * * * * user cd /path/to/dry-elecs/ && python3 processor.py
```

## API
```
/api/driest
```
Fetch the user who needs energy the most badly in Google Home Action format.

```
/api/stats
```
Get a summary of all active users in json format

```
/api/database
```
Download the database file from the server

```
/update
```
Force a hot-reload and restart of the flask server
```
