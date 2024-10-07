 # Cryptography Fundamentals

Cryptography is a crucial aspect of information security, used to protect data confidentiality, integrity, and authenticity. In this lesson, we'll explore the fundamentals of cryptography, covering key concepts, symmetric key cryptography, asymmetric key cryptography, hashing functions, public key infrastructure (PKI), digital signatures, and certificates.

## Cryptography Basic Concepts

Cryptography is the practice of protecting information from adversaries by converting it into an unreadable format. The two main goals are _confidentiality_, which ensures that only authorized parties can access the data, and _integrity_, ensuring that data remains unaltered during transmission or storage.

Let's consider a real-life example of confidentiality: imagine sending sensitive financial information over the internet. To ensure that no one intercepts and reads your data, it needs to be encrypted before being transmitted. Only the intended recipient, with the correct decryption key, can access and read the data.

## Symmetric Key Cryptography

_Symmetric key cryptography_ is a technique where the same secret key is used both for encryption and decryption. This method works well when there are only two parties involved (encryptor and decryptor). It's relatively simple and faster than asymmetric key cryptography but poses challenges when dealing with multiple parties or distributing keys securely.

Symmetric key algorithms like _Advanced Encryption Standard_ (AES) use a secret key to scramble data in such a way that only the decryptor, who has the identical key, can unscramble it. For instance, consider Alice encrypting a message with AES using a secret key "mysecretpassword123". She shares this encrypted message with Bob. Bob, with the exact same secret key ("mysecretpassword123"), can decrypt and read the original message.

However, symmetric key cryptography is vulnerable to Man-in-the-Middle (MITM) attacks: an attacker intercepts the communication between Alice and Bob and gains access to the secret key. This risk increases when using public networks like the internet. To address these concerns, we move on to asymmetric key cryptography.

## Asymmetric Key Cryptography

_Asymmetric key cryptography_, also known as _public-key cryptography_, uses a pair of mathematically related but different keys: _public key_ for encryption and _private key_ for decryption. The security relies on the fact that it's computationally infeasible to derive one key from the other.

In an example using RSA, Alice wants to send a secret message to Bob. She encrypts her message using Bob's public key. Now she attaches the encrypted message to a simple plaintext note "Open this message with your private key" and sends it. Upon receiving this message, Bob uses his private key to decrypt the content of the message, revealing Alice's encrypted secret. He can now use his public key to decrypt the actual secret message from Alice.

Asymmetric key cryptography is more secure against MITM attacks because the attacker needs both Bob's public and private keys to intercept communication. However, it has computational complexity compared to symmetric key algorithms, making it less efficient for bulk data encryption. Thus, we often use symmetric key cryptography for data encryption and asymmetric key cryptography for key exchange (e.g., RSA or Elliptic Curve Diffie-Hellman).

---

To be continued with the next subsections: Hashing Functions, Public Key Infrastructure (PKI), Digital Signatures, and Certificates.