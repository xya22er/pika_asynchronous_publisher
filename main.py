import pika 
from asynchronous_publisher_example  import ExamplePublisher
import threading
import time
example = ExamplePublisher(
		'amqp://guest:guest@localhost:5672/%2F?connection_attempts=3&heartbeat=3600'
	)
connection_thread = threading.Thread(target=example.connect_to_server(),args=())
connection_thread.start()


example.message_func("msg1")

example.message_func("msg")

