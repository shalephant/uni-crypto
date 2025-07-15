from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.backends import default_backend

parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())

# Alice and Bob generate keys
alice_private = parameters.generate_private_key()
bob_private = parameters.generate_private_key()

# Exchange public keys
alice_public = alice_private.public_key()
bob_public = bob_private.public_key()

# Shared keys
alice_shared = alice_private.exchange(bob_public)
bob_shared = bob_private.exchange(alice_public)

print(alice_shared == bob_shared)  
