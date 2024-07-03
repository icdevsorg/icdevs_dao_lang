import pygraphviz as pgv
import os

def validate_graph(graph):
    errors = []
    for node in graph.nodes():
        if graph.degree(node) == 0:
            errors.append(f"Node '{node}' has no relationships.")
    return errors




def create_specific_node_graph_v3(graph, node_name, output_dir):
    
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

    filename = f"{node_name.replace(' ', '_').replace('/', '_').replace('-', '_').lower()}_specific_graph.dot"
    
    subgraph.write(os.path.join(output_dir, filename))
    subgraph.layout(prog='dot')
    subgraph.draw(os.path.join(output_dir, filename.replace('.dot', '.png')), format='png')

def create_all_predecessors_graph(graph, node_name, output_dir):
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

    filename = f"{node_name.replace(' ', '_').replace('/', '_').replace('-', '_').lower()}_all_predecessors_graph.dot"

    subgraph.write(os.path.join(output_dir, filename))
    subgraph.layout(prog='dot')
    subgraph.draw(os.path.join(output_dir, filename.replace('.dot', '.png')), format='png')

def main(dot_file_path, output_dir):
    graph = pgv.AGraph(dot_file_path)
    errors = validate_graph(graph)
    if errors:
        print("Validation errors:", errors)
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for node in graph.nodes():
        successors = graph.successors(node)
        predecessors = graph.predecessors(node)

        print(f"Node: {node}, Successors: {len(successors)}, Predecessors: {len(predecessors)}")

        if graph.predecessors(node):
          create_all_predecessors_graph(graph, node, output_dir)
          
        else:
          print(f"Skipping {node}: No predecessors.")
        
        create_specific_node_graph_v3(graph, node, output_dir)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python script.py [DOT file path] [output directory]")
    else:
        main(sys.argv[1], sys.argv[2])
