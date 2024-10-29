import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

class FloatArrayPublisher(Node):
    def __init__(self):
        super().__init__('float_array_publisher')
        self.publisher_ = self.create_publisher(Float32MultiArray, 'float_array_topic', 10)
        timer_period = 1.0  # 1秒ごとに配列を送信
        self.timer = self.create_timer(timer_period, self.timer_callback)
    
    def timer_callback(self):
        msg = Float32MultiArray()
        # 配列のデータを設定
        msg.data = [1.1, 2.2, 3.3, 4.4]  # 送信したいfloatの配列
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    float_array_publisher = FloatArrayPublisher()
    rclpy.spin(float_array_publisher)
    float_array_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
