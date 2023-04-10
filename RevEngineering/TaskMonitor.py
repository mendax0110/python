from ghidra.program.model.symbol import SourceType
from ghidra.util.task import TaskMonitor
import time


def add_function_comment(func, comment):
    """
    Adds a comment to the specified function object.
    """
    # Start a new undoable edit
    current_program.startTransaction("Add Comment")
    try:
        # Add the comment to the function
        func.setComment(comment, SourceType.USER_DEFINED)
    except:
        # Roll back the undoable edit if an error occurs
        current_program.rollbackTransaction()
    finally:
        current_program.endTransaction(True, "Function Analysis successful")


def analyze_function(func, monitor):
    """
    Analyzes the specified function object and adds a comment with the number
    of instructions.
    """
    # Start a new undoable edit
    current_program.startTransaction("Function Analysis")
    try:
        # Do some analysis on the function
        instr_count = 0
        for block in func.getBody().getBlocks():
            for instr in block.getInstructions():
                instr_count += 1
                # Check if the user has cancelled the task
                if monitor.isCancelled():
                    raise Exception("Task cancelled by user.")
                # Sleep for a short amount of time to simulate work
                time.sleep(0.1)
        # Add a comment to the function with the instruction count
        add_function_comment(func, "This function has " + str(instr_count) + " instructions.")
        current_program.endTransaction(True, "Function Analysis successful")
    except:
        # Roll back the undoable edit if an error occurs
        current_program.rollbackTransaction()
        current_program.endTransaction(False, "Function Analysis failed")
    finally:
        current_program.endTransaction(True, "Function Analysis successful")


# Get the current program and function manager
current_program = state.getCurrentProgram()
function_manager = current_program.getFunctionManager()

# Get the function objects from the function manager
functions = function_manager.getFunctions(True)

# Create a TaskMonitor instance
monitor = TaskMonitor.DUMMY

# Analyze each function in the list
for func in functions:
    # Check if the user has cancelled the task
    if monitor.isCancelled():
        print("Task cancelled by user.")
        break
    # Analyze the function and print the name
    analyze_function(func, monitor)
    print("Analyzed function: " + func.getName(True))
