# SecureSpace: Astronaut Health Monitoring Application

**A group project for the post-graduate Computer Science programs at the University of Essex Online.**

Module: _Secure Software Development_\
Members: _Bradley Graham, Michael Sammueller, Tomas Mestanza & Rachel Doherty_

### Table of Contents

1. [How to run the program](1)
2. [Description](2)
3. [User Briefing](3)
4. [Functional Overview](4)
5. [Application Features & Technologies](5)
6. [External tools & Libraries (testing & debugging)](6)
7. [Database](7)
8. [Security Features Checklist](8)
9. [List of changes - Design Document --> Implementation](9)
10. [Testing Results](10)
11. [GDPR](11)
    - [Data Security Statement](11a)
    - [Data Privacy Policy](11b)
    - [Data Deletion Policy](11c)
12. [References](12)

### <a name="2">How to run the program</a>

In order to install all the dependencies required for this project run the command:

> pip install -r requirements.txt

This will install all of the packages in the requirements.txt file.

... tbc.
### <a name="2">Description</a>

This application is intended for use by astronauts to record health indicators related to their physical fitness and mental health during a space mission. It also models the measurement of ambient temperature and radiation exposure via onboard sensors.

The project domain is the International Space Station (ISS), which is a collaborative international space travel and research program between 15 governments, overseen and facilitated by NASA. The  application is intended to support the health and safety of astronauts aboard the ISS during a mission in order to prevent crew health issues jeopardising the success of a mission.

### <a name="3">User Briefing</a>

### <a name="4">Functional overview</a>

The application is accessed via a Command Line Interface (CLI) and allows the User to perform various CRUD actions, based on predefined role-based permission and access parameters. The project brief is to implement secure software development principles into the application design. The project has been deliberately developed in a modular way using object-oriented coding principles and a microservice architecture, in order to improve modifiability, testability and scalability.

### <a name ="5">Application features & Technologies</a>

- **Languages:** Python / SQL
- **Database:** SQLite3
- **Interface:** Command Line
- **Network requirements**: Access via a local terminal (no web access required)

The program is written in Python3 and uses the following built-in libraries: **re, logging, unittest, getpass, threading, pip, json, datetime, random, sys, uuid, cryptography, unittest, abc, os**

### <a name="6">External tools & libraries (testing and debugging)</a>

- **Pylama**
- **Bandit**
- **Pytest Security**
- **coverage**

### <a name="7">Database</a>

This solution makes use of a relational database to store data relevant to the system.

Normalisation has been applied to the database design. Applying the normalisation theory aims to reduce data redundancy and avoid potential problems when performing operations on the database (Eessaar, 2016).

As a consequence of applying normalisation, consistency is improved, and maintenance is reduced in complexity.

UUIDs are use to avoid reveal actual user IDs. We kept the numeric IDs to be able to sort as UUIDs do not allow sorting.

### <a name="8">Security Features Checklist</a>

This project is based on secure design principles, following key vulnerabilites identified in the "OWASP Top 10 Application Security Risks" (2017). The following checklist outlines the implemented security features:

> #### **OWASP Top 10: Planned vs. Implemented measures**                             
> ##### **A1: 2017 Injection**
> - [x] Sanitize input (filter keywords and special characters) for all roles
>       
> **A2:2017 Broken Authentication**
> - [x] multi-factor authentication (secret phrase)
> - [ ] time-limited set-up passwords
> - [x] password length and complexity requirements (min. 8/ max. 64 characters; allow most characters)
> - [x] limit, log and alert all failed login attempts
>       
> **A3:2017 Sensitive Data Exposure**
> - [ ] encrypt database records
> - [x] store passwords using strong salted hashing functions (bcrypt)
> - [ ] penetration testing (incl. link to evidence when done)
> - [x] delete sensitive info after mission ends - cannot be simulated by system, see data deletion policy (incl. link)
>       
> **A5:2017 Broken Access Control**
> - [x] robust roles
> - [x] no role-inheritance
>       
> **A6:2017 Security Misconfiguration**
> - [x] only implement necessary libraries 
> - [x] only implement OWASP-approved or known libraries
> - [x] ensure correct configuration of all technologies through testing (see testing section)
>
> **A9:2017 Using Components with Known Vulnerabilities**
> - [x] implement a tool that checks for dependencies and security vulnerabilities (bandit) (see test result)
>
> **(A10:2017 Insufficient Logging & Monitoring)**
> - [x] implement an effective monitoring and alert system for auditable actions
> - [ ] store log records in a dedicated database with restrictive commands
> - [x] encrypt logs 

### <a name="9">List of changes - Design Document --> Implementation</a>

> #### 1. Class 'CommonActions'
> _Original System Design:_
> > The ‘CommonActions’ class was originally planned as a class to handle all functions and methods relating to user actions.
>
> _Final Implementation:_
> > The class has been renamed to ‘ActionController’ and will act as an interface between the command line and the system objects. It will therefore always call another object’s version of a method. The Action Controller will also perform authorisation and logging. This way, individual class methods remain encapsulated which is favourable in terms of application scalability and microservice design.
>
> #### 2. File Downloads
> _Original System Design:_
> > Originally, we would allow users to download their health records as data files.
>
> _Final Implementation:_
> >
>
> #### 3. Role / Permissions mapping
> _Original System Design:_
> > 1. Superadmin permissions: create user, assign roles and privileges, execute SQL queries for database management
> > 2. Moderator permissions: approve user, delete user profile and data
> > 3. Astronaut permissions: update and view health records, download data files
>
> _Final Implementation:_
> > The planned roles did not cover system functionality. We also needed to map permissions to user actions / roles explicity in order to ensure that
> > role-based access controls (RBAC) was implemented robustly.
> > The updated role matrix maped to permissions and roles is shown in the table below:
> > | UserAction / Permission Name            | _Superadmin_ | _Moderator_ | _Astronaut_ |
> > | :-------------------------------------- | :----------: | :---------: | :---------: |
> > | Add New User / add-user                 | [x]          | [ ]         | [ ]         |
> > | Delete User / delete-user               | [x]          | [ ]         | [ ]         |
> > | Add Health Record/ add-health-record    | [x]          | [ ]         | [x]         |
> > | View Health Record / view-health-record | [x]          | [x]         | [x]         | 
> > | View Warning Logs/ view-logs            | [x]          | [ ]         | [ ]         |
> > | View Temperature / view-temperature     | [x]          | [x]         | [x]         |
> > | View Radition Level / view-radiation    | [x]          | [x]         | [x]         |
> > | Update Health Record / update-record    | [x]          | [x]         | [x]         |
> > | Delete Health Record / delete-record    | [x]          | [ ]         | [ ]         |



### <a name="10">Testing</a>



### <a name="11">GDPR</a>

The application is developed according to UK GDPR.

The lawful basis for data processing is subject to:

1) the consent of the data subjects;
2) the vital interests of crew health as a key ISS vulnerability (IISTF, 2007);
3) the continuation of ISS operations, as outlined in the legal framework of the ISS (IISTF, 2007)

It is assumed that astronaut consent to data processing is sought before any mission commences by that respective national space travel authority (e.g. the UK Space Agency, the Japan Aerospace Exploration Agency etc.). 

> ### <a name="11a">Data Security Statement</a>

> ### <a name="11b">Data Privacy Policy</a>

> ### <a name="11c">Data Deletion Policy</a>

## <a name="12">References</a>

Eessaar, E. (2016) The Database Normalization Theory and the Theory of Normalized Systems: Finding a Common Ground. Baltic J. Modern Computing 4(1): 5-33. Available from: https://www.researchgate.net/publication/297731569_The_Database_Normalization_Theory_and_the_Theory_of_Normalized_Systems_Finding_a_Common_Ground [Accessed 21 June 2023].
