from charm.toolbox.pairinggroup import PairingGroup, extract_key
from charm.schemes.ibenc.ibenc_bb04 import IBE_BB04
import hashlib

group = PairingGroup('MNT224')
ibe = IBE_BB04(group)

def generate_ibe_keys(user_email):
    """Génère une clé IBE basée sur l’email du patient"""
    master_secret, public_params = ibe.setup()
    private_key = ibe.extract(master_secret, user_email)
    hashed_key = hashlib.sha256(str(private_key).encode()).hexdigest()
    return hashed_key, public_params
