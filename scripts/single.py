def create_specific_node_graph_v3(graph, node_name):
    # Define graph attributes
    subgraph = pgv.AGraph(strict=False, directed=True)
    subgraph.graph_attr.update(rankdir="TB", nodesep="0.6", ranksep="1.2")
    subgraph.node_attr.update(shape="box")
    
    # Add the central node with correct attributes
    if node_name in graph:
        node_attrs = graph.get_node(node_name).attr
        subgraph.add_node(node_name, label=node_attrs['label'])
    
    # Handle predecessors
    predecessors = graph.predecessors(node_name)
    if predecessors:
        # Add predecessors with their labels and edges
        for predecessor in predecessors:
            pred_attrs = graph.get_node(predecessor).attr
            subgraph.add_node(predecessor, label=pred_attrs['label'])
            subgraph.add_edge(predecessor, node_name)
        # Place predecessors in 'max' subgraph
        subgraph.add_subgraph(predecessors, name='cluster_predecessors', rank='max', style='invis')

    # Handle descendants
    descendants = graph.successors(node_name)
    if descendants:
        # Add descendants with their labels and edges
        for descendant in descendants:
            desc_attrs = graph.get_node(descendant).attr
            subgraph.add_node(descendant, label=desc_attrs['label'])
            subgraph.add_edge(node_name, descendant)
        # Place descendants in 'min' subgraph
        subgraph.add_subgraph(descendants, name='cluster_descendants', rank='min', style='invis')

    # Save to DOT file
    subgraph_file_path = f'/mnt/data/{node_name}_specific_graph.dot'
    subgraph.write(subgraph_file_path)
    return subgraph_file_path

# Regenerate the graph for "Immutable Records" with the corrected approach
immutable_records_graph_path_v3 = create_specific_node_graph_v3(graph, "Immutable Records")
immutable_records_graph_path_v3
