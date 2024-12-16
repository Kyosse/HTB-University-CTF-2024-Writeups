// Author: 0xSpiizN
//// Challenge: blockchain_cryopod
//// Description: Get all stored pods

const { ethers } = require('ethers');

// Serveur RPC
const provider = new ethers.JsonRpcProvider("http://94.237.50.250:33407/");

// Mes informations
const privateKey = "c887873437dfffaaa54fa76a6c68fd7d12d9dcbf9df07a8e8cb4d2d2dad58e10";
const wallet = new ethers.Wallet(privateKey, provider);

// Adresses des contrats
const cryoPodAddress = "0xE1bFf0FBF55F0bBB07ccc72361A2A20A321F0fb5";
const setupAddress = "0x0a30a39C4B5758856C1Dd9188Ce1151c4904E2b1";

// ABI pour CryoPod
const cryoPodABI = [
  "function storePod(string memory _data) external",
  "event PodStored(address indexed user, string data)"
];

// ABI pour Setup
const setupABI = [
  "function isSolved(string calldata flag) public view returns (bool)"
];

// Contrats
const cryoPodContract = new ethers.Contract(cryoPodAddress, cryoPodABI, wallet);
const setupContract = new ethers.Contract(setupAddress, setupABI, wallet);

// Main
async function main() {
  const filter = cryoPodContract.filters.PodStored();  // No filter, get all events
  const events = await cryoPodContract.queryFilter(filter);

  // Extract and log the stored data
  events.forEach((event) => {
    console.log(`- Address: ${event.args.user}, Data: ${event.args.data}`);
  });
}

main().catch((error) => {
  console.error(error);
});
