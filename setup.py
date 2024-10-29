from setuptools import setup

package_name = 'hello_world'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple Hello World publisher and subscriber',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'publisher = hello_world.publisher:main',
            'subscriber = hello_world.subscriber:main',
        ],
    },
)
