#!/usr/bin/env python
import pika

def process_msg(ch, method, properties, body):
    print 'receive msg: ', body

connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='127.0.0.1', port=5672))
channel = connection.channel()
channel.queue_declare(queue='wgwang.github.com')
print 'receiver: waiting msg...'

channel.basic_consume(process_msg,
        queue='wgwang.github.com',
        no_ack=True)
channel.start_consuming()
