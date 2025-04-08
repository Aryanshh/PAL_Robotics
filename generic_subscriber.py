import rclpy
from rclpy.node import Node
from rosidl_runtime_py.utilities import get_message

class GenericSubscriber(Node):
    def __init__(self, topic_name, msg_type_str):
        super().__init__('generic_subscriber')

        try:
            msg_type = get_message(msg_type_str)
        except Exception as e:
            self.get_logger().error(f"Invalid message type: {msg_type_str}")
            raise e

        self.subscriber = self.create_subscription(
            msg_type,
            topic_name,
            self.callback,
            10
        )
        self.msg_type_str = msg_type_str
        self.get_logger().info(f"Subscribed to '{topic_name}' with type '{msg_type_str}'")

    def callback(self, msg):
        self.get_logger().info(f"[{self.msg_type_str}] Received: {msg}")

def main(args=None):
    rclpy.init(args=args)
    import sys
    if len(sys.argv) < 3:
        print("Usage: ros2 run generic_subscriber generic_subscriber <topic_name> <msg_type>")
        return

    topic = sys.argv[1]
    msg_type = sys.argv[2]

    node = GenericSubscriber(topic, msg_type)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
