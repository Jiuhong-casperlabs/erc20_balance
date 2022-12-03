import {
  CasperClient,
  Contracts,
  CLPublicKey,
  CLKey,
  CLAccountHash,
  CLValueParsers,
} from "casper-js-sdk";

const main = async () => {
  const client = new CasperClient("http://94.130.10.55:7777/rpc");
  const { Contract } = Contracts;

  const contractClient = new Contract(client);
  // contract hash
  const contract_hash =
    "hash-4120116565bd608fae6a45078055f320a2f429f426c86797b072b4efd15b186a";
  contractClient.setContractHash(contract_hash);

  // public key whose balance to be checked
  const pk1String1 =
    "0125a6336791eba195c472a8b7dbcd256a6ecddf8863e586a3dfefe2581a5d672c";
  const account = CLPublicKey.fromHex(pk1String1);
  const key = new CLKey(new CLAccountHash(account.toAccountHash()));
  console.log("key=>", key);
  const keyBytes = CLValueParsers.toBytes(key).unwrap();
  const itemKey = Buffer.from(keyBytes).toString("base64");

  console.log(itemKey);
  const balance = await contractClient.queryContractDictionary(
    "balances",
    itemKey
  );

  console.log(balance.data.toString());
};

main();
