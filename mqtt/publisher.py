import paho.mqtt.client as mqtt

client = mqtt.Client()

client.connect("localhost", 1883)

client.publish("swayam", "Hello Swayam!")

client.disconnect()