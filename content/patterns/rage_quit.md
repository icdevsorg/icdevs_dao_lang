## RQ - Rage Quit

![Rage Quit](./output/illustrations/rage_quit.png)

### Supports:
[Well Being](./well_being.html)

### Context:
In many DAOs, member contributions (financial, intellectual, or labor) are pooled to collectively fund projects or make organizational decisions. As these organizations grow and diverge in interests, the risk of disenchantment with collective decisions increases. Ensuring mechanisms for safe exit is essential for maintaining trust.

### Problem:
Members of a DAO might fundamentally disagree with a decision made by the majority, such as the direction of investments or changes in governance rules. In such cases, without an option to exit, members could feel trapped or unwillingly compelled to comply with decisions contrary to their principles or investment judgment.

### Forces:
1. **Autonomy**: Members desire control over their investments and decisions.
2. **Fairness**: Need to ensure that exit options are fair and do not unduly harm the DAO or its remaining members.
3. **Commitment**: Balancing the flexibility of exit against the need for stable, committed capital.
4. **Security**: Safeguarding the DAO’s assets while allowing individual withdrawals.

### Solution:
Implement the "Rage Quit" feature, allowing members to withdraw their share of the DAO's treasury proportional to their holdings or contribution, if they disagree with specific governance decisions. This feature should be integrated into the DAO's smart contracts to allow members to execute this option autonomously, ensuring a non-subjective process tied directly to recorded stakes.

**Technical Implementation Considerations:**
- **Smart Contract Functions**: Create smart contract functions that calculate a member's share based on their token holdings and enable withdrawal.
- **Timelocks**: Implement timelocks to prevent manipulation of the voting process by timing exits strategically after decisions.
- **Minimum Participation Duration**: Establish rules for a minimum participation duration before enabling the Rage Quit feature to encourage initial commitment.


#### Case Study: MolochDAO

MolochDAO, known for its emphasis on simplicity and effectiveness in handling resources among Ethereum projects, was one of the first to implement a Rage Quit mechanism. This feature provided members a clear exit option if they disagreed with the decisions regarding the use of collective funds, notably influencing the governance structure perception in DAOs. 

Through this mechanism, MolochDAO managed to maintain a high degree of autonomy for its members, thus encouraging broader participation by aligning individual and collective interests. This foundational trust likely contributed to the sustained engagement and funding of public goods within the Ethereum ecosystem, proving that the inclusion of a structured exit strategy can benefit both individual stakeholders and the collective.

### Therefore:
Members should feel assured that they can reclaim their vested assets and exit if crucial decisions go against their core values or investment logic, thus maintaining individual autonomy while supporting collective governance.

### Supported By:
[Inability to Fork External Assets](./inability_to_fork_external_assets.html)  

![Rage Quit](./output/rage_quit_specific_graph.png)