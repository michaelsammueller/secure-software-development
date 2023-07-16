# Possible architectures for the project

## Repository

* The repository needs to be secure.
* The repository needs to be able to store different kinds of information. Types of information include:
  * Atmospheric conditions (temperature, pressure, composition)
  * ISS diagnostic conditions (temperature, electrical power)
* Interchangeable
* CRUD capabilities
* Suitable databases?
* GDPR compliant

## Network Architecture

* The network should support telephone and email for the astronauts wellbeing
* The network should support communication with mission control.
* async
* Serialisation?
* Encryption?
* Authentication from mission control
* Authorisation of commands (to prevent sabotage)

### Distributive Architecture

* ISS has modular design so may benefit from distribution of data across modules.
* Distributive architecture provides some resilience against damaged communication channels.

## Sense-Plan-Act Architecure

* Sense-plan-act architecture connects sensory componenents and actuating components, with planning components for a level of automation. Examples include:
  * health monitors with life support mechanisms
  * atmospheric monitors with O2 generators, contamination disposal, humidity control, coolers
  * inventory monitors with delivery service
  * proximity monitors with navigational control
* manual overides as resilience
* sense-plan-act architectures integrated with distributed architecture requires components to have network capabilities, like a micro IoT.
* loggers

## Interface

* CLI
* Web browser?
* VUI?