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
To create the database:
```
sqlite3 database.db < schema.sql
```

Running the server:
```
pip3 install -r requirements.txt
FLASK_APP=main.py FLASK_DEBUG=1 python3 -m flask run --host=0.0.0.0 --port=5002
```

Visit the `/update` route to hot-reload

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
