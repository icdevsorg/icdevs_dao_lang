## HON - Honour

![Honour](output/illustrations/honour.png){ width=50% }

#### Supports:
* [Reputation Systems](/patterns/reputation_systems.html)

#### Context:
In DAOs where trust and reputation are central to operations, there is a need for a robust mechanism to evaluate and visualize the trust worthiness and contribution of members, beyond traditional monetary transactions.

#### Problem:
Traditional monetary systems are inherently asset-focused, encouraging accumulation and wealth as metrics of success. This doesn't align well with the collaborative, trust-based, and community-centered ethos of DAOs.

#### Forces:

- **Trust vs. Transparency**: Balancing privacy with the need for transparent transactions in a community.
- **Reciprocity vs. Accumulation**: Encouraging ongoing involvement and mutual support as opposed to mere accumulation of assets.
- **Simplicity vs. Manipulation**: Implementing a system simple enough to use but robust against gaming or exploitation.

#### Solution:
Implement a decentralized social credit such as Honour (HON)(see [link](https://www.kernel.community/en/tokens/token-studies/honour/)), which inverts traditional monetary values: holding HON signifies obligation, not wealth. This transformation is rooted in historical notions of money as a communal ledger of credit and debt within trust networks. The Honour system utilizes an ERC20 token contract modified to prevent transfers, representing obligations (debts) that members owe to the community. A separate contract governs the issuance and forgiveness of these obligations, ensuring that transactions are consensual and reflect actual contributions and needs within the community.

Key elements include:

- **Creation through Consensus**: HON tokens are minted when a member agrees to a proposed obligation or service from another member.
- **Non-transferability**: Tokens cannot be transferred between members, only forgiven, emphasizing the non-commercial, trust-based nature of the interactions.
- **Obligation as Currency**: Holding more tokens indicates a greater owed obligation, inversely related to traditional wealth metrics.

This system encourages members to engage continuously with each other, fulfilling obligations and thereby earning forgiveness of their own tokens. The larger your balance, the more you owe to the community, encouraging a cycle of service and reciprocity.

#### Therefore:
Design DAO operations around community-centered credit systems that encourage ongoing engagement and mutual support, rather than accumulation of wealth. Use technological solutions to implement non-transferable tokens that represent social credits, embedding these values into the very fabric of the community's operations.

#### Supported By:
* [Immutable Records](/patterns/immutable_records.html)

![Honour](output/honour_specific_graph.png)