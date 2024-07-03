# 👷 Work Plan

## Introduction

Our work plan lays the foundation for the development and implementation of ICRC-75, a standard designed to help DAOs manage lists of cryptographic identities, accounts, and values critical for effective governance. This initiative focuses on developing role-based access control programmable and on-chain, facilitating streamlined, transparent, and efficient management of DAOs' resources and governance activities.

## Phase 1: Definition and Development of ICRC-75

**Objective:** To define and build the ICRC-75 standard that will enable DAOs to manage cryptographic identities and accounts, orchestrate programmable role-based access control, and optimize resource deployment.

**Actions:**

1. **Research and Define ICRC-75:** 
   - Compile requirements from various DAOs to ensure the standard meets the needs of diverse organizations.
   - Define data structures, protocols, and interfaces required for managing cryptographic identities, accounts, and role-based permissions.

2. **Research and Define Portable Credentials:** 
   - Explore the possibilities of issue Verifiable Credentials, JWTs, and subnet certificates for DAO members to use when interacting with other services, or to prove they are a member of the DAO or a working group.

3. **Development of Roles, Groups, and Permissions Tool:**
   - Design and implement smart contracts that define user roles, group memberships, and associated permissions.
   - Develop functionalities to dynamically add or remove roles and permissions based on predefined rules.

4. **Development of Linked Lists:**
   - Create systems for auto-populating lists based on inputs from other lists to reduce governance overhead.

5. **Secure Multi-Sig Implementations:**
   - Design and implement multi-sig smart contracts enabling actions to be executed only upon consensus from multiple signatories, ensuring security and distributed decision-making.

5. **Working Group Membership Systems:**
   - Automate the introduction and rotation of members within working groups based on eligibility and contribution metrics.

6. **Integration and Testing:**
   - Integrate permissions and roles framework into existing DAO infrastructures.
   - Conduct extensive testing to ensure stability, security, and versatility.

**Deliverables:**
- Documentation of ICRC-75 standard.
- Smart contracts for roles, groups, and permissions.
- Automated list population functionality.
- Multi-sig solutions.
- Automated working group membership management.

**Supported By Patterns:**
- **Transparent Governance**
- **Decentralized Autonomy**
- **Incentive Alignment**
- **Resource Optimization**

## Phase 2: Building Lego Blocks Based on ICRC-75

**Objective:** To develop modular and reusable components ("lego blocks") based on the ICRC-75 standard, facilitating easy assembly and leveraging of foundational capabilities in different DAOs.

**Actions:**

1. **Lego Block Definition:**
   - Define the foundational components required, including but not limited to role rotators, fund distributors, and voting booth contracts.

2. **Implementation of Lego Blocks:**
   - Develop and test implementation of modular components, ensuring they are plug-and-play and adaptable to varied DAO environments.

3. **Documentation and Best Practices:**
   - Create comprehensive documentation on how to use and integrate these lego blocks.
   - Develop best practices for leveraging these components effectively within various DAO frameworks.

**Deliverables:**
- Set of modular, reusable lego blocks.
- Detailed documentation and integration guides.
- Best practices for leveraging lego blocks within DAOs.

**Supported By Patterns:**
- **Predefined Action Protocols**
- **Feedback Integration Teams**
- **Cross-functional Teams**

## Phase 3: On-Chain DAO Governance Strategies

**Objective:** To transition more complex forms of DAO governance on-chain, leveraging our developed ICRC-75 standard and lego blocks to automate and optimize decentralized governance.

**Actions:**

1. **Governance Model Design:**
   - Work with leading DAOs to design advanced governance models that can operate fully on-chain.
   - Incorporate complex voting mechanisms like quadratic voting, conviction voting, and multi-factorial consensus.

2. **Smart Contracts for Advanced Governance:**
   - Develop smart contracts that support advanced governance mechanisms.
   - Ensure these contracts are fully auditable and transparent.

3. **Implementation and Testing:**
   - Implement the advanced governance models in pilot DAOs Canisters that can easily be added to existing SNS and other DAOs.
   - Conduct rigorous testing to ensure seamless operation and mitigate any potential vulnerabilities.

**Deliverables:**
- Various On-chain governance models.
- Smart contracts supporting various approval and voting mechanisms.
- Testing reports and community feedback integration.

**Supported By Patterns:**
- **Iterative Funding**
- **Impact Measurement**
- **Scalable Decision-Making**
- **Transitioning to Utilitarian Design**

## Beyond: Funding and Automation

Continue to explore new ways of funding and allocation strategies for DAOs and exploring tools that can reduce overhead.

