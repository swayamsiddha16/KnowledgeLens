""""paho.mqtt used to create mqtt client"""
import paho.mqtt.client as mqtt

def on_message(message):
    print("Received message:", message.payload.decode("utf-8"))


client = mqtt.Client()
"""create an instance  of the MQTT client bt calling mqtt.Client()"""

client.on_message = on_message

client.connect("localhost", 1883)

client.subscribe("IOT")

client.loop_forever()