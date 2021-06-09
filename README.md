# File Integrity Monitor

The FIM is a django app developed to keep track of and monitor the state of network-shared files. The underlying concept is that each file has a certain hash value based on its current state at any given time. A change in any of the file's contents or properties (meta-data) will result in a change in the hash value of the file. This tool serves to maintain and monitor the integrity of files by comparing the saved hash values with the current hash values for the given time. If any variations are discovered, it will then send an alert to the Administrator or personnel responsible for monitoring the files.

<br />

> Procedure

- Generate hash values and collect creation, access and modification timestamps
- Save the hashes into a database
- Display the relevant file information on the dashboard
- Verify whether the current hash value is the same as that one stored in the database
- Generate an alert if the values are different

<br />

> Technologies Used

- Django(Python) Framework
- MD5 Hashing Algorithm
- HTML, JavaScript and CSS