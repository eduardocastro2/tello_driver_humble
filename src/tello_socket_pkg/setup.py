from setuptools import setup

package_name = 'tello_socket_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='eduardocastro2',
    maintainer_email='josee.castro@udem.edu',
    description='Tello driver for ROS2 Humble',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'udp_sender = tello_socket_pkg.tello_sender:main',
            'drone_controller = tello_socket_pkg.drone_controller:main'
        ],
    },
)
