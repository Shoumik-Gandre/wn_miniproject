import paho.mqtt.publish as publish


def main():

    publish.single(
        topic="WN/test",
        payload="Hello",
        hostname="test.mosquitto.org"
    )
    publish.single(
        topic="WN/topic",
        payload="World",
        hostname="test.mosquitto.org"
    )


if __name__ == '__main__':
    main()
