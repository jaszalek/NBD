import riak
import sys

def store(myClient, bucketName, key, data):
  try:
    bucket = myClient.bucket(bucketName)
    record = bucket.new(key,data)
    record.store()
    print("Zapisano")
  except:
    print(sys.exc_info()[0])

def read(myClient, bucketName, key):
  try:
    bucket = myClient.bucket(bucketName)
    record = bucket.get(key)
    if(record.encoded_data==None):
      print("Brak")
    else:
      print(record.encoded_data.decode("utf-8"))
  except:
    print(sys.exc_info()[0])
        
def update(myClient, bucketName, key, value_up, value):
  try:
    bucket = myClient.bucket(bucketName)
    record = bucket.get(key)
    record.data[value_up] = value
    record.store()
    print("Updated")
  except:
    print(sys.exc_info()[0])

def delete(myClient, bucketName, key):
  try:
    bucket = myClient.bucket(bucketName)
    record = bucket.get(key)
    record.delete()
    print("Deleted")
  except:
    print(sys.exc_info()[0])

def main():
    doc = {
        'type':'crane',
        'name':'rtk',
        'weight' : '200',
        'id'  : '12345'
    }
    myClient = riak.RiakClient(pb_port=8087)
    bucketName = 's16422'
    store(myClient, bucketName, doc['id'], doc)
    read(myClient, bucketName, doc['id'])
    update(myClient, bucketName, doc['id'], 'weight', '1200')
    read(myClient, bucketName, doc['id'])
    delete(myClient, bucketName, doc['id'])
    read(myClient, bucketName, doc['id'])

if __name__=="__main__":
  main()