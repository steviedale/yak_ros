import os
import launch
import launch_ros.actions
from launch_ros.substitutions.find_package import get_package_share_directory

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            node_name='tsdf_node',
            package='yak_ros',
            node_executable='yak_ros_node',
            output='screen',
            remappings=[('input_depth_image', '/camera/aligned_depth_to_color/image_raw')],
            parameters=[{'tsdf_frame': 'tsdf_origin',
            'cx': 316.08880615234375,
            'cy': 241.31689453125,
            'fx': 380.40179443359375,
            'fy': 380.40179443359375,
            'cols': 640,
            'rows': 480,
            'volume_resolution': 0.001,
            'volume_x': 640,
            'volume_y': 640,
            'volume_z': 640}]),
])
