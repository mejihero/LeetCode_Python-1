class MyStack {
public:
  /** Initialize your data structure here. */
  MyStack() {}

  /** Push element x onto stack. */
  void push(int x) {
    q_.push(x);
    for (int i = 1; i < q_.size(); ++i) {
      q_.push(q_.front());
      q_.pop();
    }
  }

  /** Removes the element on top of the stack and returns that element. */
  int pop() {
    int top = q_.front();
    q_.pop();
    return top;
  }

  /** Get the top element. */
  int top() {
    return q_.front();
  }

  /** Returns whether the stack is empty. */
  bool empty() {
    return q_.empty();
  }
private:
  queue<int> q_;
};

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * bool param_4 = obj.empty();
 */






     """
             Only this C++ version passed the test. Didn't find any useful Python samples.
     """
