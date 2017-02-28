# lab robot scripts
These python scripts are used to communicate with a home-build lab robotic system that we are using
for single-cell genomics research to interface microfluidics chips to macrofluidics (well plates).
This step often becomes necessary since most genomics protocols require the use of well plates.

We created several helper scripts that identify the different Arduino microcontrollers that are attached to
the computer running the scripts.  One Ardunino is running grbl and is controlling all the stepper motors
that in turn drive the x-y axis of the well plate and a z motor that moves a pipette.

