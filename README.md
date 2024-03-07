# Omni-directional-mobile-robot

##Description
This project implements a simple robot using Raspberry Pi and ultrasonic sensors for obstacle avoidance. The robot is designed to move forward until it detects an obstacle in its path. Upon obstacle detection, it checks the proximity of obstacles on different sides and adjusts its movement accordingly to avoid collisions. The robot can move forward, backward, turn left, turn right, move left laterally, and move right laterally based on the sensor inputs.

## Features

* Controls the robot's movement (forward, backward, left, right, left/right lateral).
* Detects obstacles using ultrasonic sensors in front, left, right, and lateral directions.
* Avoids obstacles by stopping or changing direction.

  ## Hardware Requirements

* Raspberry Pi
* Motor driver (compatible with your motors)
* Two ultrasonic sensors
* DC motors (with appropriate voltage and current ratings for your motor driver)
* Jumper wires
* Breadboard (optional)

## Software Requirements

* Python 3
* RPi.GPIO library

## Getting Started

1. **Install libraries:**
   ```bash
   pip install RPi.GPIO
   ```

2. Connect the hardware:
Refer to your motor driver and sensor documentation for specific connection instructions.
Ensure the motor driver and motors are compatible based on voltage and current ratings.
3. Run the script:
   ```Bash
    python Omnidirection_mobile_robot.py
   ```

##How it Works
###The script:

- Sets up GPIO pins for motor control and ultrasonic sensors.
- Defines functions for various robot movements (forward, backward, turn, etc.).
- Implements a function to check the distance using ultrasonic sensors.
- Continuously checks the front distance and avoids obstacles based on predefined thresholds.
- Moves forward when no obstacles are detected.


Further Enhancements
- Add functionalities like turning at specific angles, stopping on button press, etc.
- Implement more sophisticated obstacle avoidance algorithms.
- Integrate with a camera for visual obstacle detection.

##License
This project is licensed under the MIT License.
