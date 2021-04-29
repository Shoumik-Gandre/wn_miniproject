import paho.mqtt.client as mqtt
import beepy


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("WN/play_music")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    if msg.payload.decode() == "Y":
        beepy.beep(sound=6)


def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("test.mosquitto.org", 1883, 60)

    # Blocking call that processes network traffic, dispatches callbacks and
    # handles reconnecting.
    # Other loop*() functions are available that give a threaded interface and a
    # manual interface.
    client.loop_forever()


if __name__ == "__main__":
    main()
