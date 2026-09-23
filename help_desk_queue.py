from node import Node


# Queue class used for the help desk line
class Queue:
    def __init__(self):
        # Front is the next customer to be helped
        # Rear is the last customer in line
        self.front = None
        self.rear = None

    def enqueue(self, value):
        # Create a new node for the customer
        new_node = Node(value)

        # If the queue is empty, front and rear are the same node
        if self.rear is None:
            self.front = new_node
            self.rear = new_node
            return

        # Add the new node to the end of the queue
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        # Nothing to remove if the queue is empty
        if self.front is None:
            return None

        # Save the first customer's value
        value = self.front.value

        # Move the front pointer to the next customer
        self.front = self.front.next

        # If the queue becomes empty, reset rear too
        if self.front is None:
            self.rear = None

        return value

    def peek(self):
        # Look at the next customer without removing them
        if self.front is None:
            return None

        return self.front.value

    def print_queue(self):
        # Start at the front and print each customer
        current = self.front

        if current is None:
            print("Queue is empty")
            return

        while current is not None:
            print(f"- {current.value}")
            current = current.next


def run_help_desk():
    # Create the help desk queue
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            queue.enqueue(name)
            print(f"{name} added to the queue.")

        elif choice == "2":
            customer = queue.dequeue()

            if customer is None:
                print("No customers waiting")
            else:
                print(f"Helped: {customer}")

        elif choice == "3":
            customer = queue.peek()

            if customer is None:
                print("No customers waiting")
            else:
                print(f"Next customer: {customer}")

        elif choice == "4":
            print("\nWaiting customers:")
            queue.print_queue()

        elif choice == "5":
            print("Exiting Help Desk Ticketing System.")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    run_help_desk()
