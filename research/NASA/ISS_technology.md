# Technology on Board the ISS

## Computers

* Hewlett Packard Enterprise (HPE) sent Spaceborne Computer-1 (SBC-1) to the 
ISS, which remained there for 657 days. This was sponsered by the ISS U.S. National Laboratory. It was a commerical off-the-shelf (COTF) machine that was unmodified. It demonstrated supercomputing capabilities from a COTS on the space station, that had not been 'hardened' to withstand spaceflight. 'Smart software' was used to protect the systems hardware. SBC-1 achieved 1 teraflop of operation per second. The smart software monitored hardware status and altered it's performance to accomodate those conditions. Common issues in space include network signal loss with Earth and power interruptions. SSD's were the most vulnerable component, with 9/20 failing. [ISS National Laboratory, 2021](https://www.issnationallab.org/hpe-supercomputing-return-space/)
* SBC-2 experiments will return in Autumn 2022, and features embedded processors used in mobile phones such as the Snapdragon 855, and Intel Movidius Myriad X Vision Processing Unit. [NASA Artificial Intelligence Group](https://ai.jpl.nasa.gov/public/projects/iss/)
* IBM ThinkPad Computer - an COTF laptop [NLSP](https://nlsp.nasa.gov/view/lsdapub/lsda_hardware/IDP-LSDA_HARDWARE-0000000000000009#:~:text=The%20IBM%20Thinkpad%20Computer%20is,and%20retrieve%20instructions%20and%20data.)

### Edge Computing

* IBM Cloud was scheduled to provide a place where researchers develop, test and make code ready to be pushed to the ISS. The plan consisted of VPN connections to connect users who submit jobs with the HPE ground systems that communicate securely with the SBC-2 system on the ISS. IBM installed Red Hat CodeReady Containers on SBC-2, capable of executing code to analyse data produced on the ISS, saving the need of transferring that data to Earth. Results will be available on the ISS, and relayed via a messaging queue to the ground. Job executions will be on demand. [IBM, 2021](https://www.ibm.com/cloud/blog/ibm-develops-a-unique-custom-edge-computing-solution-in-space)

## Space Station Assembly

![exploded view](./images/exploded%20view.jpg)

[Space Station Assembly History](https://www.nasa.gov/mission_pages/station/structure/elements/space-station-assembly)