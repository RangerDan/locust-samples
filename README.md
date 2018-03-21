# RangerDan's locust-samples - Load testing PirateBox with Locust.io

This locust sample project collects demonstrations of locust.io features.  The testing target is PirateBox.cc's sharing platform.  All metrics were obtained from PirateBox running on a Raspberry Pi B

## Prerequisites

Locust.io requires Python (v3 supported)

Your PirateBox will require a Raspberry Pi or similar platform.  However, Android (rooted) and laptop setups are also available.

Distributed tests may require more hosts, containers, VMs, etc.

## Installing Locust.io

Locust.io is available in pip

    $ pip install locustio
    $ locust --help

## Obtaining a PirateBox

I set up my PirateBox in under an hour by following these excellent instructions: https://piratebox.cc/raspberry_pi:diy

## Testing Locally

For tests that are run from your host, you will need to connect to the PirateBox network in order to access those services.  You should be able to use the PirateBox itself as a development host if you do not have a separate computer.

For tests running from multiple hosts (demonstrating master/slave functionality), you will need multiple hosts, containers, etc.
