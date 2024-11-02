
import pika

def send_message(queue, message):
  connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
  channel = connection.channel()
  channel.queue_declare(queue=queue)
  channel.basic_publish(exchange='', routing_key=queue, body=message)
  connection.close()

def receive_message(queue, callback):
  connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
  channel = connection.channel()
  channel.queue_declare(queue=queue)
  channel.basic_consume(queue=queue, on_message_callback=callback, auto_ack=True)
  channel.start_consuming()

