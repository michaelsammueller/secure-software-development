## Secure Coding Principles
Some notes to help with planning / write-up tasks

## Pillai, A.B. (2017) Software Architecture with Python. Birmingham, UK. Packt Publishing Ltd. Chapter 2:

Steps to Secure Coding:
1.	Define areas of interest of the application which are critical and need to be secured
2.	Analyse the software architecture for obvious security flaws 
    - secure interaction between components to ensure data confidentiality and integrity 
    - ensure data is properly protected via authentication and authorization techniques 
    - ensure availability is built into the architecture from the ground up
4.	Review the code using secure coding techniques. Ensure peer review is done with a view to finding security holes.
5.	Review code logic and syntax to ensure there are no obvious loopholes in the implementation. Make sure programming is done keeping within commonly available secure coding guidelines of the programming language/platform.
6.	White box/ unit testing – test code with security tests apart from tests ensuring functionality (use mock data or APIs to virtualise 3rd party data)
7.	Blackbox testing – experience QA engineer tests application and looks for security loopholes (unauthorised access to data, pathways exposing code or data, weak passwords or hashes)

Common security vulnerabilities:
- Overflow errors (buffer and arithmetic or integer overflows)
- Unvalidated / improperly validated input E.g. SQL injections, Server-Side Template Injections, Cross-Site-Scripting (XSS), and Shell Execution Exploits
- Improper access control
- Cryptography issues - e.g. HTTP instead of HTTPS: When implementing RESTFul web services, make sure you favor HTTPS (SSL/TLS) over HTTP. In HTTP, all communication is in plain text between the client and server, and can be easily captured by passive network sniffers or carefully crafted packet capture software or devices installed in routers.
- Insecure authentication
- Use of weak passwords
- Reuse of secure hashes/secret keys
- Weak encryption
- Weak hashing
- Invalid or expired certificates/keys – e.g. SSL certificates
- Password enabled SSH
- Information leak
- Open access to files/folders/databases – access should be role-based
- Race conditions
- System clock drifts – missing local clock time synchronisation on server – can cause error in SSL certificate validation
- Insecure file/folder operations

