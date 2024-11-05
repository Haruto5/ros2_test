import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
from sensor_msgs.msg import Image  # Add this import
from cv_bridge import CvBridge  # Add this import to convert OpenCV images
from . import get_object_position

class ArrayPublisher(Node):
    def __init__(self):
        super().__init__('array_publisher')
        
        # Publisher for position data
        self.array_publisher = self.create_publisher(Float32MultiArray, 'array_topic', 10)
        
        # Publisher for image data
        self.image_publisher = self.create_publisher(Image, 'image_topic', 10)
        
        self.timer = self.create_timer(1.0, self.publish_data)
        self.bridge = CvBridge()  # Initialize CvBridge
        self.get_logger().info('Array and Image Publisher Node started.')

    def publish_data(self):
        # Get position data and image from get_object_position
        data = get_object_position.get_position()
        position_data = data[0]
        img = data[1]  # This should be an OpenCV image

        # Publish position data as Float32MultiArray
        array_msg = Float32MultiArray()
        array_msg.data = position_data
        self.array_publisher.publish(array_msg)
        self.get_logger().info(f'Publishing array: {array_msg.data}')

        # Convert OpenCV image to ROS Image message and publish
        image_msg = self.bridge.cv2_to_imgmsg(img, encoding='bgr8')
        self.image_publisher.publish(image_msg)
        self.get_logger().info('Publishing image.')

def main(args=None):
    rclpy.init(args=args)
    node = ArrayPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
