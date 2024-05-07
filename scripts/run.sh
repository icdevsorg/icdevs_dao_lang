#!/bin/bash
# Path to your Python scripts
PYTHON_SCRIPT_PATH="/path/to/your/scripts"

# Generate the resource optimization graph
python3 $PYTHON_SCRIPT_PATH/create_resource_optimization_graph.py "Resource Optimization"

# Generate support graphs for each top-level node
python3 $PYTHON_SCRIPT_PATH/create_support_graph.py "Community Involvement"
python3 $PYTHON_SCRIPT_PATH/create_support_graph.py "Impact Measurement"
python3 $PYTHON_SCRIPT_PATH/create_support_graph.py "Resource Development"
python3 $PYTHON_SCRIPT_PATH/create_support_graph.py "Incentive Alignment"
python3 $PYTHON_SCRIPT_PATH/create_support_graph.py "Risk Management"
python3 $PYTHON_SCRIPT_PATH/create_support_graph.py "Effective Action"
