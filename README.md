# dry-electrics-delegator
Some Dry Electrics Delegation

## Client

- Download the latest [bg.sh](https://raw.githubusercontent.com/ryan-brown/dry-electrics-delegator/master/bg.sh) script to `/some/path/bg.sh`
- Run `crontab -e`
- Enter the following with correct path and name, and save:

```
* * * * * sh /some/path/bg.sh YourName
```

## Server
```
pip3 install -r requirements.txt
FLASK_APP=main.py FLASK_DEBUG=1 flask run --host=0.0.0.0 --port=5002
```

Visit the `/reset` route to reset the server state
