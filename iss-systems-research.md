# ISS Systems Research

### Brainstorming:
* The ISS has limited physical resources due to space constraints, limiting computing power, storage, and network bandwidth.
* Depending on its location, the ISS experiences communications delay. Data must be transmitted through multiple satellite relays.
* The ISS transmits and receives sensitive information, meaning data must be encrypted before transmission.
* Computer systems on the ISS are critical; any software deployed must be reliable and quickly recoverable in cases of emergency.

### This means:
* The application must be efficient and use as little resource as possible to run (i.e. limit the strain on CPU, RAM and network). This also relates to code efficiency.
* The application must be able to handle communication delay/delay in receiving data. Ensure that any parts of the application don’t experience issues related to time out.
* Ensure that the application encrypts the data it sends and is able to decrypt the data it receives.
* Ensure that the application is able to handle errors and exceptions, to avoid crashes.
* The application must be compatible with Linux-based machines, as ISS computers run Linux (Debian). It appears that administrative PCs might still be running Windows 7 or Windows 10. 
  (Potentially check for cross-compatibility, or at least add it as a consideration)
  
### Ideas for a CRUD Application
* Health monitoring of astronauts (Radiation levels, blood sugar, weight, muscle mass, body fat, etc.)
* Task Management System
* Inventory Management System

### System Requirements & Assumptions
**Access:** The system will be used locally by astronauts, and remotely by NASA mission control.
**Storage Required:** The system will be relatively small and lightweight.
**User Roles:**
**Concurrent Data Streams:** Logging?
**Design Decisions:**
        **Algorithms:**
        **Data Storage:**
        **Database:**
        **Design Patterns:**
        **Security Features:**
                  * User authentication
                  * Password encryption
                  * Input validation
                  * Database encryption
                  * Session handling - Assign a session ID (Web App)
                  * Keep a log file which stores user activity
                   * Ensure that the session is destroyed once the user logs out

### Useful Python Libraries
* **Bandit:** Checks code for common security flaws such as SQL injection, cross-site scripting, and buffer overflows.
* **Pytest Security:** Checks for common issues such as input validation, authentication, and access control.
* **Safety:** Command-line tool that checks code dependencies for known security vulnerabilities. Also checks if dependencies are up-to-date.
* **PyT:** Provides tools to test the security of web applications. Tests for common vulnerabilities such as SQL injection, cross-site scripting, and CSRF (Cross-Site Request Forgery). 
           CSRF is an attack where the attacker tricks a victim into performing a malicious action they did not intend to do. For example, the attacker sends a link to the victim, which, 
           when clicked, changes the user’s password.

### Notes:
"*To protect against system failures, the EMU has redundancy in the critical cooling, O2, pressure, and communication systems*" (Page 33)

"*Compromise of an information technology system is a threat to any computing network, and a deliberate attack using the ground command system to issue commands to the ISS systems could have catastrophic results. 
[...] Command security is audited by the NSA on a periodic basis. The IPs have similar IT security measures in place.*" (Page 34)

"*An inadvertent critical command or commands sent from a ground controller could lead to catastrophic results. For this reason, there are multiple checks and balances associated with critical ISS commands.*

*Criticality 1 hazardous commands (those that could cause loss of crew) are required to be “two-stage”, meaning that they require separate “arm” and “fire” commands to be implemented. [...]*

*For criticality 2 hazardous commands (those that could lead to loss of mission), the crew or controllers receive an additional “Are You Sure?” pop-up-message that is to be acknowledged prior to execution of the command*" (Page 34)

"*The software and workstations that perform communications and commanding functions also have several security measures. Security for the MCC workstations is governed by and consistent with the 
National Information Assurance Policy for U.S. Space Systems. All workstations for command and telemetry are continuously monitored by standard anti-virus and spyware protection software and are scanned quarterly for vulnerabilities 
using the latest industry-standard security software. Password protection is in place on all workstations, and only certain users/accounts can access ISS commanding servers, which require an additional password. Access to ISS commanding 
is further limited by partitioning available commands by user groups, and users only have access to the commands necessary to perform that discipline’s function. To provide a quality check of commands, two people are required to perform a command. 
Finally, all commands to the vehicle are encrypted and must pass through a series of validity and authentication checks.*" (Page 44)

# References
* In 2019, NASA doubled the data transmission speed between the ISS and Earth to 600 megabit-per-second (https://www.nasa.gov/feature/goddard/2019/data-rate-increase-on-the-international-space-station-supports-future-exploration)
* According to NASA, the transmission delay between the ISS and Earth is less than a second (https://www.nasa.gov/feature/goddard/2019/data-rate-increase-on-the-international-space-station-supports-future-exploration)
* According to NASA, data is only encrypted when sent to the ISS. Data sent from the ISS, or data sent between Mission Control Centers in Houston and Moscow are not encrypted. (https://llis.nasa.gov/lesson/1148)
