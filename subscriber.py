import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

class FloatArraySubscriber(Node):
    def __init__(self):
        super().__init__('float_array_subscriber')
        # Publisherで指定したトピック名に合わせる
        self.subscription = self.create_subscription(
            Float32MultiArray,
            'float_array_topic',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        # 受け取った配列データを表示
        self.get_logger().info(f'Received: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    float_array_subscriber = FloatArraySubscriber()
    rclpy.spin(float_array_subscriber)
    float_array_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
