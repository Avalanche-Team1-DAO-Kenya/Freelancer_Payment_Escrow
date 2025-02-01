Project Overview

This project is a decentralized escrow and milestone verification system built on the Avalanche blockchain. It ensures secure and transparent collaboration between project owners and developers, using on-chain payments, role-based access control, and automated milestone validation via GitHub test results.

Key Features

✅ Role Management – Controls user and developer registration.
✅ Escrow System – Secure milestone-based fund release.
✅ GitHub Oracle Integration – Automates milestone verification using GitHub API test results.
✅ Wallet Connection – Enables seamless interaction with smart contracts.
✅ Secure & Transparent – Funds are locked in escrow and released only upon milestone approval.

Project Structure

The project consists of three main smart contracts:

1️⃣ RoleManagement.sol (User & Developer Access Control)

Registers users and developers to ensure only authorized participants interact with the platform.

Provides role verification functions for other contracts.

Admin-only access control for managing user roles.


2️⃣ Escrow.sol (Payment & Milestone Escrow)

Handles project creation with locked funds for development milestones.

Integrates GitHub Oracle to verify code quality via test results.

Releases funds only when milestones are marked as complete and approved.


3️⃣ GitHubOracle.sol (Milestone Verification)

Receives test results from GitHub API.

Validates milestones based on GitHub test outputs.

Ensures transparency and accountability in the development process.



---

Deployment Instructions

1. Smart Contract Compilation & Deployment

Use Remix IDE or Hardhat to compile and deploy the smart contracts.

Deploy RoleManagement.sol first, followed by GitHubOracle.sol, and then Escrow.sol (passing the addresses of the previous contracts as constructor parameters).


2. Frontend Integration

Connect wallets using Metamask or AvalancheJS.

Allow users to register as owners or developers using RoleManagement.

Enable project creation and milestone tracking via Escrow.sol.

Fetch GitHub test results using GitHubOracle.sol for milestone validation.



---

How It Works

1️⃣ Project Creation & Fund Locking

1. Owner registers and deposits funds for milestones.


2. Developer is assigned and starts working on the project.



2️⃣ Milestone Verification via GitHub Oracle

1. Developer pushes code to GitHub repository.


2. GitHub API runs tests and sends results to GitHubOracle.sol.


3. If tests pass, the milestone is marked complete.



3️⃣ Fund Release & Completion

1. Owner reviews & approves the completed milestone.


2. Escrow releases the payment to the developer.


3. Process repeats for all milestones until project completion.




---

Contract Addresses (Testnet)

RoleManagement.sol – 0x916e4eD7885379d6a6fA3afbBF88adD80423Ea52

GitHubOracle.sol – 0xa24e61886EA1AF9959B2F7952d52Ea243D1007a1

Escrow.sol – 0x8eE3A46aAd8c8F09d56D8d0D6A2227ee9eF45018



---

Technology Stack

Smart Contracts: Solidity

Blockchain: Avalanche (C-Chain)

Frontend: React.js / Next.js

Backend API: Node.js / Express

Storage: IPFS (for project metadata)



---

Future Improvements

🚀 Multi-chain compatibility (Ethereum, Polygon, Base)
🚀 Automated GitHub integration using Chainlink oracles
🚀 Dispute resolution system via decentralized arbitration


---

Contributors

👤 Gethsun Misesi – Lead Blockchain Developer
👤 Jane (KibokoDAO) – Project Coordinator
👤 Muasya – Backend Integration
👤 Timothy Agevi – QA & Testing

For questions or contributions, feel free to open an issue or submit a PR!


---

License

📜 SPDX-License-Identifier: MIT
