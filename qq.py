import json

import redis


redis_db = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)

def insert_update(username, percentage, charging, updated_at):
    redis_db.rpush('write_queue', json.dumps({
        'username': username,
        'percentage': percentage,
        'charging': charging,
        'updated_at': updated_at.isoformat()
        }));
    update_data = json.dumps({
        'username': username,
        'percentage': percentage,
        'charging': charging,
        'updated_at': updated_at.isoformat()
        }); 
    print("update_data", update_data)

    redis_db.set('user_%s' % username, json.dumps({
        'username': username,
        'percentage': percentage,
        'charging': charging,
        'updated_at': updated_at.isoformat()
        }));

def read_from_queue(max_count=1000):
    batch = []
    for count in range(max_count):
        batch.append(json.loads(redis_db.lpop('write_queue')))
    return batch

def get_user_data(username):
    user_data = redis_db.get(username)
    if user_data is None:
        user_data = '{}'
    return json.loads(user_data);

def get_all_users():
    return redis_db.keys('user_*')
