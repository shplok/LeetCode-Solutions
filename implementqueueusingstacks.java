import java.util.Stack;

class MyQueue {

    // Two stacks to simulate the queue
    Stack<Integer> stack1 = new Stack<>();
    Stack<Integer> stack2 = new Stack<>();

    // Variable to store the front element of the queue
    int front;

    public MyQueue() {

    }

    public void push(int x) {
        // If stack1 is empty, set the front element
        if (stack1.isEmpty()) {
            front = x;
        }
        // Push the element onto stack1
        stack1.push(x);
    }

    public int pop() {
        // Check if stack2 is empty, if so, transfer elements from stack1 to stack2
        if (stack2.isEmpty()) {
            while (!stack1.isEmpty()) {
                int x = stack1.pop();
                stack2.push(x);
            }
        }
        // Pop from stack2
        return stack2.pop();
    }

    public int peek() {
        // If stack2 is not empty, peek the top element from it
        if (!stack2.isEmpty()) {
            return stack2.peek();
        }
        // Otherwise, return the front element stored earlier
        return front;
    }

    public boolean empty() {
        // The queue is empty if both stacks are empty
        return (stack1.isEmpty() && stack2.isEmpty());
    }
}
