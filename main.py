import pika 
from no_ioloop_asynchronous_publisher_example  import ExamplePublisher
import threading
import time
example = ExamplePublisher(
		'amqp://guest:guest@localhost:5672/%2F?connection_attempts=3&heartbeat=3600'
	)

example.run()
example.publish_message("msg")

