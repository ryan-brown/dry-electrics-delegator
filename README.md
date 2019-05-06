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

- If you'd like to use DED in conjunction with MTMR, you can use the following config to create a touchbar item that displays the driest user.  Just plug in the location of the ded.scpt file (from this repository):
```
  {
    "type": "appleScriptTitledButton",
    "width": 200,
    "source": {
      "filePath":
        "</Path/to/your/ded.scpt>"
    },
    "refreshInterval": 60,
    "image": {
      "base64":
"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"
    }
  }
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
FLASK_APP=main.py FLASK_SECRET=SECRET FLASK_DEBUG=1 python3 -m flask run --host=0.0.0.0 --port=5002
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
