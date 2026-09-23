from node import Node


# Stack class used to store actions
class Stack:
    def __init__(self):
        # Top starts empty
        self.top = None

    def push(self, value):
        # Create a new node and put it on top
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        # Nothing to remove if the stack is empty
        if self.top is None:
            return None

        # Save the value before removing the top node
        value = self.top.value
        self.top = self.top.next
        return value

    def peek(self):
        # Look at the top value without removing it
        if self.top is None:
            return None

        return self.top.value

    def print_stack(self):
        # Start at the top and move through each node
        current = self.top

        if current is None:
            print("Stack is empty")
            return

        while current is not None:
            print(f"- {current.value}")
            current = current.next


def run_undo_redo():
    # One stack keeps actions and the other keeps undone actions
    undo_stack = Stack()
    redo_stack = Stack()

    while True:
        print("\n--- Undo/Redo Manager ---")
        print("1. Perform action")
        print("2. Undo")
        print("3. Redo")
        print("4. View Undo Stack")
        print("5. View Redo Stack")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            action = input("Describe the action (e.g., Insert 'a'): ")

            # New actions go into the undo stack
            undo_stack.push(action)

            # Doing a new action clears anything that could be redone
            redo_stack = Stack()

            print(f"Action performed: {action}")

        elif choice == "2":
            # Remove the most recent action
            action = undo_stack.pop()

            if action is None:
                print("No actions to undo")
            else:
                # Save the removed action in case the user wants to redo it
                redo_stack.push(action)
                print(f"Undid action: {action}")

        elif choice == "3":
            # Take the most recently undone action
            action = redo_stack.pop()

            if action is None:
                print("No actions to redo")
            else:
                # Put it back into the undo stack
                undo_stack.push(action)
                print(f"Redid action: {action}")

        elif choice == "4":
            print("\nUndo Stack:")
            undo_stack.print_stack()

        elif choice == "5":
            print("\nRedo Stack:")
            redo_stack.print_stack()

        elif choice == "6":
            print("Exiting Undo/Redo Manager.")
            break

        else:
            print("Invalid option.")


# Only starts the program when this file is run directly
if __name__ == "__main__":
    run_undo_redo()
