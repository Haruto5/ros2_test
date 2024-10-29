from setuptools import setup
import os
from glob import glob

package_name = 'camera'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        # パッケージに必要なファイルをインストールする
        (os.path.join('share', package_name), ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your_email@example.com',
    description='ROS2 package for publishing and subscribing float arrays',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # 実行ファイルの登録
            'publisher = camera.publisher:main',
            'subscriber = camera.subscriber:main',
        ],
    },
)
