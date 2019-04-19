import json

import redis


redis_db = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)

def insert_update(username, percentage, charging, updated_at):
    update_data = json.dumps({
        'username': username,
        'percentage': percentage,
        'charging': charging,
        'updated_at': updated_at.isoformat()
        }); 

    redis_db.rpush('write_queue', update_data)
    redis_db.set('user_%s' % username, update_data)

def read_from_queue(max_count=1000):
    batch = []
    for count in range(max_count):
        update = redis_db.lpop('write_queue')
        if update is not None:
            batch.append(json.loads(update))
    return batch

def get_user_data(username):
    user_data = redis_db.get(username)
    if user_data is None:
        user_data = '{}'
    return json.loads(user_data);

def get_all_users():
    return redis_db.keys('user_*')
