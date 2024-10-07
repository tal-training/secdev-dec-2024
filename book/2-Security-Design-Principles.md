 # Security Design Principles

Security design principles are fundamental guidelines that help create secure systems. In this lesson, we will explore ten essential security design principles, which include Defense-in-Depth, Fail Safe, Least Privilege, Separation of Duties, Economy of Mechanism, Complete Mediation, Open Design, Least Common Mechanism, Psychological acceptability, Weakest Link, Leveraging Existing Components, Input Validation, and Output Sanitization.

## Defense-in-Depth (DiD)

Defense-in-depth is a security strategy that involves using multiple layers of defense to protect against unauthorized access or attacks. Instead of relying on a single method or boundary for protection, DiD employs multiple techniques at various levels in the system architecture. Each layer acts as a barrier against potential threats, making it more challenging for attackers to breach the system's security. For example, DiD may include firewalls, intrusion detection systems, access controls, antivirus software, and user education. By implementing Defense-in-Depth, you can reduce the likelihood of successful attacks and minimize the potential damage if a breach does occur.

## Fail Safe vs. Fail Secure

Fail Safe and Fail Secure are two different security concepts that focus on system behavior during errors or abnormal conditions.

### Fail Safe

A fail-safe design aims to ensure the system reverts to a known safe state whenever it encounters an unexpected event or error, typically prioritizing system safety over confidentiality and availability. A classic example of this principle is a nuclear reactor's emergency core cooling system that initiates when certain temperature thresholds are reached.

### Fail Secure

A fail-secure design focuses on maintaining the security of the data and system integrity during errors or unexpected situations, prioritizing confidentiality and often availability over safety. For example, if a web server is under attack and becomes unresponsive, it may be designed to fail securely by shutting down all user sessions while continuing to serve essential services such as SSL/TLS termination and access control checks.

## Least Privilege (Principle of Least Privilege)

The Principle of Least Privilege (PoLP), also known as the principle of least privilege, is a fundamental security concept that suggests an application, user, or process should only have the necessary access rights to perform its tasks. By reducing privileges to their minimum requirements, you significantly reduce the risk of unauthorized access and minimize the potential impact of a successful attack. For example, an application server running in a production environment should only provide necessary access permissions for reading or writing specific files to relevant processes and applications rather than granting full system access.

## Separation of Duties (SoD)

Separation of duties (SoD) is the security principle that restricts a user, application, or process from performing multiple critical tasks within a single transaction. This design helps mitigate potential risks by requiring multiple approvals, steps, or permissions to perform sensitive operations, thereby minimizing the likelihood of errors and reducing the risk of unauthorized access. For example, in a financial organization, an employee may require approval from both their direct supervisor and their HR department before they can process transactions above a specific threshold amount.

## Economy of Mechanism (Keep it Simple)

The Economy of Mechanism principle suggests that complex systems are inherently more vulnerable to security risks because they offer more opportunities for exploitation than simpler designs. By designing your system with minimal components and ensuring the interactions between these components are well-defined and controlled, you can make it harder for attackers to find vulnerabilities and gain unauthorized access. A classic example of this principle is the implementation of a secure payment gateway: The payment gateway must only perform essential tasks such as encryption, decryption, and data transfer without any additional features that might introduce unnecessary complexity and potential security risks.