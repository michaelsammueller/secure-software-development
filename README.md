# Astronaut Health Monitoring Application

**A group project for the post-graduate Computer Science programs at the University of Essex Online.**

Module: _Secure Software Development_\
Team Name: _SecureSpace_\
Members: _Bradley Graham, Michael Sammueller, Tomas Mestanza & Rachel Doherty_

## Description

This application is intended for use by astronauts to record health indicators related to their physical fitness and mental health during a space mission. It also models the measurement of ambient temperature and radiation exposure via onboard sensors.

The project domain is the International Space Station (ISS), which is a collaborative international space travel and research program between 15 governments, overseen and facilitated by NASA. The  application is intended to support the health and safety of astronauts aboard the ISS during a mission in order to prevent crew health issues jeopardising the success of a mission.

The project brief is to implement secure software development principles into the application design. 

### Application features & Technologies

- **Languages:** Python / SQL
- **Database:** SQLite3
- **Interface:** Command Line
- **Network requirements**: Ethernet - access is via a local terminal (no web access)

### External tools & libraries (security)

- **Python built-in libraries:** re, logging, unittest, getpass, threading, pip
- **Bcrypt**
- **Cryptography**

### External tools & libraries (testing and debugging)

- **Pylama**
- **Bandit**
- **Pytest Security**
- **coverage**

### How to run the project

## GDPR

The application is developed according to UK GDPR.

The lawful basis for data processing is subject to:

1) the consent of the data subjects;
2) the vital interests of crew health as a key ISS vulnerability (IISTF, 2007);
3) the continuation of ISS operations, as outlined in the legal framework of the ISS (IISTF, 2007)

It is assumed that astronaut consent to data processing is sought before any mission commences by that respective national space travel authority (e.g. the UK Space Agency, the Japan Aerospace Exploration Agency etc.). 

### Data Security Statement

### Data Privacy Policy

### Data Deletion Policy

## Database

This solution makes use of a relational database to store data relevant to the system.

Normalisation has been applied to the database design. Applying the normalisation theory aims to reduce data redundancy and avoid potential problems when performing operations on the database (Eessaar, 2016).

As a consequence of applying normalisation, consistency is improved, and maintenance is reduced in complexity.

UUIDs are use to avoid reveal actual user IDs. We kept the numeric IDs to be able to sort as UUIDs do not allow sorting.

## References

Eessaar, E. (2016) The Database Normalization Theory and the Theory of Normalized Systems: Finding a Common Ground. Baltic J. Modern Computing 4(1): 5-33. Available from: https://www.researchgate.net/publication/297731569_The_Database_Normalization_Theory_and_the_Theory_of_Normalized_Systems_Finding_a_Common_Ground [Accessed 21 June 2023].
