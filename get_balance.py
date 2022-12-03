from pycspr.types import CL_Key
from pycspr import NodeClient
from pycspr import NodeConnection
from pycspr.types import DictionaryID_ContractNamedKey
import base64

_NODE_ADDRESS = "94.130.10.55"

def main():
    # step1 create dictionary_item_key
    account_key=CL_Key.from_string('account-hash-2293223427d59ebb331ac2221c3fcd1b3656a5cb72be924a6cdc9d52cdb6db0f')
    itemKey  = base64.b64encode(b'\x00' + account_key.identifier)  # b'\x00' for account; b'\x01' for contract package
    print("itemKey",itemKey.decode("utf-8"))

    client = NodeClient(NodeConnection(host=_NODE_ADDRESS,port_rpc=7777))

    # step2 get rpc
    # Set dictionary item identifier.
    dictionary_id = DictionaryID_ContractNamedKey(
        dictionary_name="balances",
        dictionary_item_key=itemKey.decode("utf-8"),
        contract_key="4120116565bd608fae6a45078055f320a2f429f426c86797b072b4efd15b186a"
    )

    # Set node JSON-RPC query response.
    response = client.get_dictionary_item(dictionary_id)
    # get balance
    balance = response["stored_value"]["CLValue"]["parsed"]

    print("balance => ",balance)

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(f"API ERROR @ NODE {_NODE_ADDRESS} :: {err}")