#!/usr/bin/env python
import pika
import random

def send(msg):
    connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='127.0.0.1', port=5672))
    channel = connection.channel()
    channel.queue_declare(queue='wgwang.github.com')
    channel.basic_publish(exchange='',
            routing_key='wgwang.github.com',
            body=msg)
    print 'send msg: ', msg
    connection.close()

for i in range(10):
    msg = 'hi %d, welcome to WoW!' %(random.randint(1, 100))
    send(msg)
