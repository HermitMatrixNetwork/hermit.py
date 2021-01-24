import abc
import base64
from bech32 import bech32_encode, bech32_decode, convertbits
import hashlib
from typing import Optional

from terra_sdk.core.auth import StdSignature, StdSignMsg, StdTx, PublicKey

BECH32_PUBKEY_DATA_PREFIX = "eb5ae98721"

__all__ = ["Key"]

sha = hashlib.sha256()
rip = hashlib.new("ripemd160")


def get_bech(prefix: str, payload: str) -> str:
    return bech32_encode(
        prefix, convertbits(bytes.fromhex(payload), 8, 5)
    )  # base64 -> base32


def address_from_public_key(public_key: bytes) -> bytes:
    sha.update(public_key)
    rip.update(sha.digest())
    return rip.digest()


def pubkey_from_public_key(public_key: bytes) -> bytes:
    arr = bytearray.fromhex(BECH32_PUBKEY_DATA_PREFIX)
    arr += bytearray(public_key)
    return bytes(arr)


class Key:

    public_key: bytes
    raw_address: bytes
    raw_pubkey: bytes

    def __init__(self, public_key: Optional[bytes] = None):
        self.public_key = public_key
        if public_key:
            self.raw_address = address_from_public_key(public_key)
            self.raw_pubkey = pubkey_from_public_key(public_key)

    @abc.abstractmethod
    async def sign(self, payload: bytes) -> bytes:
        raise NotImplementedError("an instance of Key must implement Key.sign")

    @property
    def acc_address(self) -> str:
        if not self.raw_address:
            raise ValueError("could not compute acc_address: missing raw_address")
        return get_bech("terra", self.raw_address.hex())

    @property
    def val_address(self) -> str:
        if not self.raw_address:
            raise ValueError("could not compute val_address: missing raw_address")
        return get_bech("terravaloper", self.raw_address.hex())

    @property
    def acc_pubkey(self) -> str:
        if not self.raw_pubkey:
            raise ValueError("could not compute acc_pubkey: missing raw_pubkey")
        return get_bech("terrapub", self.raw_pubkey.hex())

    @property
    def val_pubkey(self) -> str:
        if not self.raw_pubkey:
            raise ValueError("could not compute val_pubkey: missing raw_pubkey")
        return get_bech("terravaloperpub", self.raw_pubkey.hex())

    async def create_signature(self, tx: StdSignMsg) -> StdSignature:
        if self.publicKey is None:
            raise ValueError(
                "signature could not be created: Key instance missing public_key"
            )

        sig_buffer = await self.sign(tx.to_json(sort=True).strip().encode())
        pub_key = PublicKey(value=base64.b64encode(self.public_key).decode())

        return StdSignature.from_data(
            {
                "signature": base64.b64encode(sig_data).decode(),
                "pub_key": {
                    "type": "tendermint/PubKeySecp256k1",
                    "value": base64.b64encode(self.public_key).deocde(),
                },
            }
        )

    async def sign_tx(self, tx: StdSignMsg) -> StdTx:
        sig = await self.create_signature(tx)
        return StdTx(tx.msgs, tx.fee, [sig], tx.memo)