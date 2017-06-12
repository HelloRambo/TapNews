from cloudAMQP_client import CloudAMQPClient

CLOUDAMQP_URL = "amqp://nklrrnkw:ZRRNkXKVSmrC-8EKvQU2CxPXkbkDp5Bl@fish.rmq.cloudamqp.com/nklrrnkw"

TEST_QUEUE_NAME = 'test'

def test_basic():
    client = CloudAMQPClient(CLOUDAMQP_URL, TEST_QUEUE_NAME)
    
    sendMsg = {'test': 'demo'}
    client.sendMessage(sendMsg)
    client.sleep(10)
    receivedMsg = client.getMessage()
    assert sendMsg == receivedMsg
    print 'test_basic passed!'


if __name__ == "__main__":
    test_basic()
