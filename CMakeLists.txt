cmake_minimum_required(VERSION 3.5)
project(hello_world)

# 依存パッケージの設定
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)  # カスタムメッセージ用

# メッセージの生成 (もし msg/TwoDArray.msg が存在する場合)
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/TwoDArray.msg"
)

# Pythonノードのインストール設定
install(
  DIRECTORY hello_world
  DESTINATION lib/${PROJECT_NAME}
)

# パッケージのビルド依存関係を宣言
ament_package()
