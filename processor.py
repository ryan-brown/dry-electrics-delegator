import database
import qq

def process():
    batch = qq.read_from_queue()
    database.batch_insert_update(batch)
    # print(database.select_everything())

process()
