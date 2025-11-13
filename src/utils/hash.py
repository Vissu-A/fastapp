# import hashlib
from passlib.context import CryptContext

pcd_ctx = CryptContext(schemes="argon2", deprecated="auto")

class PasscodeHash():
    def encrypt_passcode(self, passcode: str):
        # # Convert long secret to a fixed 32-byte digest
        # secret_digest = hashlib.sha256(passcode.encode()).digest()
        return pcd_ctx.hash(passcode)
