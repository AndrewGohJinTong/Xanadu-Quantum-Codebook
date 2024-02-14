"""The code template to supply to the front end. This is what the user will
    be asked to complete and submit for grading.

    Do not include any imports.

    This is not a REPL environment so include explicit 'print' statements
    for any outputs you want to be displayed back to the user.

    Use triple single quotes to enclose the formatted code block.
"""

#challenge_code = '''

import pennylane as qml
import numpy as np

dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def apply_u_as_rot(phi, theta, omega):

    ##################
    # YOUR CODE HERE #
    ##################
    
    # APPLY A ROT GATE USING THE PROVIDED INPUT PARAMETERS
    
    # RETURN THE QUANTUM STATE VECTOR
    qml.rot(phi, theta, omega, wire = 0)

    return qml.state()
