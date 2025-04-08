import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class StringPublisher(Node):
    def __init__(self):
        super().__init__('string_publisher')
        self.publisher = self.create_publisher(String, 'string_topic', 10)
        self.timer = self.create_timer(1.0, self.publish)

    def publish(self):
        msg = String()
        msg.data = "Hello from StringPublisher"
        self.publisher.publish(msg)
        self.get_logger().info(f"Published: {msg.data}")

def main():
    rclpy.init()
    node = StringPublisher()
    rclpy.spin(node)
    rclpy.shutdown()
