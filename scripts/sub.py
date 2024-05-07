def create_all_predecessors_graph(graph, node_name):
    # Define graph attributes
    subgraph = pgv.AGraph(strict=False, directed=True)
    subgraph.graph_attr.update(rankdir="TB", nodesep="0.6", ranksep="1.2")
    subgraph.node_attr.update(shape="box")
    
    # Initialize the DFS stack with the initial node
    stack = [node_name]
    visited = set()
    
    # Use DFS to find all predecessors recursively
    while stack:
        current_node = stack.pop()
        if current_node not in visited:
            visited.add(current_node)
            # Get current node attributes and add to subgraph
            if current_node in graph:
                node_attrs = graph.get_node(current_node).attr
                subgraph.add_node(current_node, label=node_attrs['label'])
            
            # Process all predecessors of the current node
            for predecessor in graph.predecessors(current_node):
                if predecessor not in visited:
                    stack.append(predecessor)
                    pred_attrs = graph.get_node(predecessor).attr
                    subgraph.add_node(predecessor, label=pred_attrs['label'])
                    subgraph.add_edge(predecessor, current_node)  # Add edge

    # Save to DOT file
    subgraph_file_path = f'/mnt/data/{node_name}_all_predecessors_graph.dot'
    subgraph.write(subgraph_file_path)
    return subgraph_file_path

# Test this function by generating a graph for a node with known complex predecessors
test_predecessors_graph_path = create_all_predecessors_graph(graph, "Immutable Records")
test_predecessors_graph_path
