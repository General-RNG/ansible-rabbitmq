#!/usr/bin/env python
import pika

# Connect to RabbitMQ with admin user credentials
credentials = pika.PlainCredentials('admin', 'test123')
parameters = pika.ConnectionParameters('localhost', 5672, '/prod/test', credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Declare a test exchange
exchange_name = 'test_exchange'
channel.exchange_declare(exchange=exchange_name, exchange_type='direct')

# Declare a test queue with TTL (3600 seconds)
queue_name = 'test_queue'
args = {'x-message-ttl': 3600000}  # TTL in milliseconds
channel.queue_declare(queue=queue_name, arguments=args)

# Bind test exchange to test queue
channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key='hello_world')

# Produce sample messages to the test exchange
sample_messages = ['Hello', 'Hi', 'Greetings', 'Bonjour', 'Labas']
for message in sample_messages:
    channel.basic_publish(exchange=exchange_name, routing_key='hello_world', body=message)
    print(f"Sent: '{message}'")

# Close the connection to RabbitMQ server
connection.close()