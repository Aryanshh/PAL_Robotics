from setuptools import setup

package_name = 'generic_subscriber'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    entry_points={
        'console_scripts': [
            'generic_subscriber = generic_subscriber.generic_subscriber:main',
            'string_publisher = generic_subscriber.string_publisher:main',
            'int_publisher = generic_subscriber.int_publisher:main',
            'twist_publisher = generic_subscriber.twist_publisher:main',
        ],
    },
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='Generic ROS 2 topic subscriber',
    license='MIT',
)
