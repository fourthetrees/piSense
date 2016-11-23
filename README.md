# piSense
An in-progress collection of scripts for automated sensor-logging and remote upload for raspberry py computers.

# Overview:
The piSense collection is an attempt to create a body of small versatile scripts in the tradition of unix which allow for a wide range of raspberry pi based sensor deployments, as well as well organized local storage, remote upload, and low-maintenance configuration.

Part of the goal of the piSense collection, is to make deploying configurations as easily as possible, and keeping organizational overhead to a minimum.  With this in mind, the piSense body of code should be fully customizeable via a single deployment.json file.  The accompanying flask webserver script should infer all storage needs of a data uplaod from its deployment name and json data labeling.  This should allow for a raspberry pi, and its corresponding server-side resources, to be fully configured via the modification/download of a single file.

# Core Components:
- **Sensor Scripts:** Flexible lightweight scripts for logging from various hardware sensor options.
- **SQLite Scripts:** Script for auto-generation, maintenance, and interface with an on-board SQLite database.
- **HTTP Client:**  Script for handling upload/download of necessary data (sensor data, deployment files, etc...).
- **Master Daemon:**  Orchestrator which parses deployment file & launches workers.
