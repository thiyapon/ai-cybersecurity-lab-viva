# AI Cybersecurity Lab Manual and Viva Preparation System — Study Guide

> Draft educational material. Match topics to your actual syllabus and verify answers against course material and current official references before submission.


## Password Hashing

**Aim:** Understand secure password storage using password hashing and salts.

**Theory:** Password hashing derives a verifier from a password. Use a purpose-built password-hashing algorithm with appropriate parameters. Salts are unique random values stored with each hash; they help prevent identical passwords from producing identical stored values and reduce the value of precomputed attacks.

**Procedure checklist:**

- [ ] Review hashing vs encryption.
- [ ] Run a local demonstration with test-only passwords.
- [ ] Compare outputs produced with different salts.
- [ ] Observe password verification.
- [ ] Record findings and security precautions.

### Viva questions and model answers

1. **Q: What is password hashing?**
   **A:** A one-way transformation used to derive a password verifier from a password.
   *Reference to check:* OWASP Password Storage Cheat Sheet

2. **Q: Is hashing the same as encryption?**
   **A:** No. Hashing is designed to be one-way; encryption is reversible with the appropriate key.
   *Reference to check:* NIST cryptography guidance

3. **Q: What is a salt?**
   **A:** A unique random value used with a password before hashing; it is stored alongside the resulting verifier.
   *Reference to check:* OWASP Password Storage Cheat Sheet

4. **Q: Why use a unique salt for each password?**
   **A:** It helps prevent identical passwords from having identical stored hashes and reduces the effectiveness of precomputed attacks.
   *Reference to check:* OWASP Password Storage Cheat Sheet

5. **Q: Name a password-hashing algorithm.**
   **A:** Argon2id is a recommended option; bcrypt and PBKDF2 may also be appropriate when configured correctly.
   *Reference to check:* OWASP Password Storage Cheat Sheet

6. **Q: Why should passwords not be stored in plaintext?**
   **A:** A database exposure would reveal the original passwords directly.
   *Reference to check:* OWASP Password Storage Cheat Sheet

7. **Q: What is a brute-force attack?**
   **A:** An attack that tries many candidate passwords until a match is found.
   *Reference to check:* NIST digital identity guidance

8. **Q: What is a pepper?**
   **A:** An additional secret value kept separately from the password database and salt.
   *Reference to check:* OWASP Password Storage Cheat Sheet

9. **Q: Can a hash alone prove who created a file?**
   **A:** No. A hash can help check integrity, but by itself it does not establish the creator's identity.
   *Reference to check:* NIST cryptography guidance

10. **Q: How should an application verify a password?**
   **A:** Use the stored algorithm parameters and salt with a trusted password-verification function, then compare securely according to that library's guidance.
   *Reference to check:* OWASP Password Storage Cheat Sheet


## Firewall Rules

**Aim:** Understand how firewall rules control network traffic.

**Theory:** A firewall applies rules to network traffic based on properties such as direction, protocol, address and port. A least-privilege policy allows only traffic needed for the service. Rule order and default policy can affect outcomes.

**Procedure checklist:**

- [ ] Review inbound and outbound traffic.
- [ ] Inspect a sample ruleset in a lab or simulator.
- [ ] Identify protocol, port, direction and action.
- [ ] Test only in an authorized lab.
- [ ] Document the expected and observed result.

### Viva questions and model answers

1. **Q: What is a firewall?**
   **A:** A security control that monitors or filters network traffic according to defined rules.
   *Reference to check:* CISA cybersecurity resources

2. **Q: What is inbound traffic?**
   **A:** Traffic entering a host or network from another system.
   *Reference to check:* Course material / firewall documentation

3. **Q: What is outbound traffic?**
   **A:** Traffic leaving a host or network toward another system.
   *Reference to check:* Course material / firewall documentation

4. **Q: What is a firewall rule?**
   **A:** A condition and action that determine whether matching traffic is allowed, blocked or otherwise handled.
   *Reference to check:* Course material / firewall documentation

5. **Q: What does least privilege mean for firewall rules?**
   **A:** Permit only the traffic required for the intended service or task.
   *Reference to check:* CISA cybersecurity resources

6. **Q: What is a port?**
   **A:** A numbered logical endpoint used by transport-layer protocols to identify a service or process.
   *Reference to check:* IANA service-name registry / networking text

7. **Q: What is a default-deny policy?**
   **A:** Traffic is blocked unless a rule explicitly permits it.
   *Reference to check:* CISA cybersecurity resources

8. **Q: Why does rule order matter?**
   **A:** Some firewalls evaluate rules sequentially, so an earlier matching rule may determine the result.
   *Reference to check:* Relevant firewall product documentation

9. **Q: What is the difference between TCP and UDP?**
   **A:** TCP provides a connection-oriented reliable byte stream; UDP sends datagrams without TCP's delivery guarantees.
   *Reference to check:* RFC 9293 / RFC 768

10. **Q: How should firewall rules be tested?**
   **A:** In an authorized, isolated environment using expected test traffic and documented results.
   *Reference to check:* Course material / lab policy


## Secure Configuration

**Aim:** Identify basic system-hardening practices.

**Theory:** Secure configuration reduces attack surface by disabling unnecessary services, applying updates, enforcing least privilege, strengthening authentication and documenting approved settings. Exact settings depend on the operating system, workload and organizational policy.

**Procedure checklist:**

- [ ] Record the lab system and baseline settings.
- [ ] Review updates, accounts, permissions and services.
- [ ] Compare settings with an approved checklist or benchmark.
- [ ] Change only an authorized test system.
- [ ] Record changes and rollback steps.

### Viva questions and model answers

1. **Q: What is system hardening?**
   **A:** Reducing a system's attack surface through secure configuration and removal of unnecessary exposure.
   *Reference to check:* CIS Benchmarks / NIST configuration guidance

2. **Q: What is least privilege?**
   **A:** Giving users and processes only the permissions needed for their tasks.
   *Reference to check:* NIST security guidance

3. **Q: Why install security updates?**
   **A:** Updates can fix known vulnerabilities and other defects.
   *Reference to check:* CISA cybersecurity resources

4. **Q: Why disable unnecessary services?**
   **A:** It reduces exposed functionality and potential attack paths.
   *Reference to check:* CIS Benchmarks

5. **Q: What is an attack surface?**
   **A:** The set of points where an attacker could attempt to enter or affect a system.
   *Reference to check:* NIST glossary

6. **Q: Why use multi-factor authentication?**
   **A:** It requires more than one type of evidence to authenticate, reducing reliance on a single compromised factor.
   *Reference to check:* CISA MFA guidance

7. **Q: What is a baseline configuration?**
   **A:** An approved reference set of configuration settings used for consistency and comparison.
   *Reference to check:* NIST configuration management guidance

8. **Q: Why review user accounts?**
   **A:** To remove or disable unneeded accounts and limit unauthorized access.
   *Reference to check:* CIS Benchmarks

9. **Q: What is a rollback plan?**
   **A:** A documented way to restore the previous state if a change causes problems.
   *Reference to check:* Operational best practice / course material

10. **Q: How do you verify a hardening change?**
   **A:** Compare the resulting setting with the approved requirement and record evidence.
   *Reference to check:* Course material / benchmark


## Security Log Review

**Aim:** Recognize useful security events in sample system logs.

**Theory:** Logs record events with fields such as timestamp, source, account, event type and result. Reviewing repeated failures, unusual times and unexpected changes can help identify activity requiring investigation. A log event alone is not proof of an attack.

**Procedure checklist:**

- [ ] Use synthetic or approved sample logs.
- [ ] Identify fields and timestamps.
- [ ] Filter for failed logins and unusual patterns.
- [ ] Correlate events before drawing conclusions.
- [ ] Record findings and uncertainty.

### Viva questions and model answers

1. **Q: What is a security log?**
   **A:** A record of security-relevant events generated by a system or application.
   *Reference to check:* NIST log-management guidance

2. **Q: Why are timestamps important?**
   **A:** They help establish event order and correlate events across systems.
   *Reference to check:* NIST log-management guidance

3. **Q: What can repeated failed logins indicate?**
   **A:** They may indicate mistyped credentials, misconfiguration or a password-guessing attempt; context is needed.
   *Reference to check:* NIST / course material

4. **Q: What is log correlation?**
   **A:** Connecting related events across records or systems to understand a sequence of activity.
   *Reference to check:* NIST log-management guidance

5. **Q: Why synchronize system clocks?**
   **A:** Consistent time makes event ordering and cross-system correlation more reliable.
   *Reference to check:* NIST log-management guidance

6. **Q: What is a false positive in monitoring?**
   **A:** An alert that flags benign activity as suspicious.
   *Reference to check:* Security monitoring terminology

7. **Q: Does one failed login prove an attack?**
   **A:** No. It needs context and corroborating evidence.
   *Reference to check:* Security analysis best practice

8. **Q: Why protect log integrity?**
   **A:** Tampered logs may mislead investigations and weaken evidence reliability.
   *Reference to check:* NIST log-management guidance

9. **Q: What is log retention?**
   **A:** Keeping logs for a defined period based on policy, legal needs and investigation requirements.
   *Reference to check:* Organizational policy / NIST guidance

10. **Q: What should a log-review report include?**
   **A:** Scope, time range, notable events, evidence, interpretation, limitations and recommended follow-up.
   *Reference to check:* Course material / NIST guidance


## Encryption Basics

**Aim:** Explain core encryption concepts and common use cases.

**Theory:** Encryption transforms plaintext into ciphertext using an algorithm and key to protect confidentiality. Symmetric encryption uses the same secret key for encryption and decryption; public-key cryptography uses a key pair. Hashing and digital signatures serve different purposes from encryption.

**Procedure checklist:**

- [ ] Identify plaintext, ciphertext, algorithm and key.
- [ ] Compare symmetric and public-key approaches.
- [ ] Use a trusted educational tool with sample data.
- [ ] Observe encryption and decryption with authorized keys.
- [ ] Record what encryption does and does not guarantee.

### Viva questions and model answers

1. **Q: What is encryption?**
   **A:** A transformation that protects information confidentiality using an algorithm and key.
   *Reference to check:* NIST cryptography guidance

2. **Q: What is plaintext?**
   **A:** The readable or original data before encryption.
   *Reference to check:* Cryptography terminology

3. **Q: What is ciphertext?**
   **A:** The transformed output produced by encryption.
   *Reference to check:* Cryptography terminology

4. **Q: What is symmetric encryption?**
   **A:** Encryption and decryption use the same secret key.
   *Reference to check:* NIST cryptography guidance

5. **Q: What is public-key cryptography?**
   **A:** A cryptographic approach using related public and private keys for supported operations.
   *Reference to check:* NIST cryptography guidance

6. **Q: What is a key?**
   **A:** A value that controls a cryptographic operation.
   *Reference to check:* NIST cryptography guidance

7. **Q: Does encryption automatically ensure integrity?**
   **A:** Not always. Use an authenticated-encryption scheme or a separate integrity mechanism appropriate to the design.
   *Reference to check:* NIST cryptography guidance

8. **Q: What is decryption?**
   **A:** Recovering plaintext from ciphertext using the required key and algorithm.
   *Reference to check:* Cryptography terminology

9. **Q: How is hashing different from encryption?**
   **A:** Hashing is designed to be one-way; encryption is designed to be reversible with the appropriate key.
   *Reference to check:* NIST cryptography guidance

10. **Q: Why should established cryptographic libraries be used?**
   **A:** They reduce the risk of implementation mistakes compared with designing cryptography from scratch.
   *Reference to check:* NIST cryptography guidance
