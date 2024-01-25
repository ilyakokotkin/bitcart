import asyncio
import binascii
import json
import os
import secrets
import traceback

import httpx
from decimal import Decimal
from genericprocessor import BlockchainFeatures  
import asyncio

class SOLFeatures(BlockchainFeatures):
    def __init__(self, rpc):
        super().__init__(rpc)
        self.rpc_endpoint = rpc  # Assuming rpc is the endpoint URL for Solana's JSON RPC server

    async def http_post_request(self, method, params=[]):
        async with httpx.AsyncClient() as client:
            data = {
                "jsonrpc": "2.0",
                "id": 1,
                "method": method,
                "params": params,
            }
            response = await client.post(self.rpc_endpoint, json=data)
            result = response.json()
            if "error" in result:
                raise Exception(result["error"].get("message", "Unknown error"))
            return result.get("result")

    async def get_block_number(self) -> int:
        # Fetches the current slot
        result = await self.http_post_request("getSlot")
        return result

    async def is_connected(self) -> bool:
        # Simple check to see if the endpoint is alive
        try:
            await self.http_post_request("getHealth")
            return True
        except:
            return False

    async def is_syncing(self) -> bool:
        # Check if the node is behind the current slot
        node_version = await self.http_post_request("getVersion")
        # Assumption: Simplified sync status check. Adjust as per actual use case
        return node_version is None

    async def get_transaction(self, tx_signature: str) -> dict:
        """
        Fetches transaction details for a confirmed transaction.

        Parameters:
        tx_signature (str): Transaction signature, as a base-58 encoded string.

        Returns:
        dict: A dictionary containing detailed information about the transaction if found and confirmed.
              Returns None if the transaction is not found or not confirmed.
        """
        params = [
            tx_signature,
            {
                "encoding": "jsonParsed",  # Using jsonParsed for more human-readable and explicit data
                "commitment": "finalized",  # Ensuring we fetch a finalized (confirmed) transaction state
            },
        ]
        result = await self.http_post_request("getTransaction", params)
        
        # Handle the case where the transaction is not found or not confirmed
        if result is None:
            return None
            
        return result

    def get_tx_receipt(self, tx) -> dict:
        # Fetch transaction receipt. For Solana, this is part of the transaction itself.
        raise NotImplementedError

    async def get_confirmations(self, tx_hash) -> int:
        # Solana transactions confirmations calculation.
        raise NotImplementedError

    def get_balance(self, address) -> Decimal:
        # Fetch the balance for a given account address
        raise NotImplementedError

    def get_block(self, block, *args, **kwargs) -> dict:
        # Get block details by slot number
        raise NotImplementedError

    async def get_block_txes(self, block) -> list:
        # Get transactions for a given block (slot)
        raise NotImplementedError

    def is_address(self, address) -> bool:
        # Check if a string is a valid Solana address.
        # Solana addresses are base58 encoded, so you can check using a base58 library
        raise NotImplementedError

    def normalize_address(self, address) -> str:
        # Return the normalized (or the same, if already normalized) address
        raise NotImplementedError

    def get_peer_list(self) -> list:
        # Returns list of peers connected to. This might not be directly available via Solana's JSON RPC.
        raise NotImplementedError

    async def get_payment_uri(self, req, divisibility, contract=None) -> str:
        # Generate a Solana payment URI (if applicable)
        raise NotImplementedError

    async def process_tx_data(self, data) -> "Transaction":
        # Process raw transaction data into a Transaction dataclass
        raise NotImplementedError

    def get_tx_hash(self, tx_data) -> str:
        # Extract and return transaction hash from tx_data
        raise NotImplementedError
        
    def get_gas_price(self) -> int:
        raise NotImplementedError