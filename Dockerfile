# Container is built around ROS Noetic
FROM ros:noetic

# Updates and installs libraries
RUN apt-get update
# RUN apt-get install python3-dev python3-rpi.gpio
RUN apt-get install python3-dev

#   This line should be used when files are being tested on a windows machine running docker, it will convert dos files(edited on windows) to unix files that can be run in our container
RUN  apt-get install dos2unix 

# Makes catkin workspace
RUN mkdir -p catkin_ws/src

# Setup environment
RUN . /opt/ros/noetic/setup.sh && catkin_init_workspace /catkin_ws/src
RUN . /opt/ros/noetic/setup.sh && cd /catkin_ws && catkin_make
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc

# Add src to workspace and create a scripts package
RUN cd catkin_ws/src && catkin_create_pkg scripts

# Copy all folders from source directory
COPY files catkin_ws/src/scripts

# For running windows created files in linux container
RUN dos2unix catkin_ws/src/scripts/**

# Make all files executable
RUN cd catkin_ws/src/scripts && chmod -R +x *

# Setup environment
RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
RUN echo "source /catkin_ws/devel/setup.bash" >> ~/.bashrc

# Make symlink 
RUN ln -s /usr/bin/python3 /usr/bin/python

# Launch master_launch launch file
CMD ["/bin/bash", "-c", "source /opt/ros/noetic/setup.bash && source /catkin_ws/devel/setup.bash && roslaunch scripts master_launch.launch"]
