// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    // The `new` function is not used in the current code but can be useful for future use
    // #[inline]
    // fn new(val: i32) -> Self {
    //     ListNode {
    //         next: None,
    //         val
    //     }
    // }
}

pub struct Solution;  // Define the Solution struct

impl Solution {
    // Function to calculate GCD using the Euclidean algorithm
    fn gcd(a: i32, b: i32) -> i32 {
        if b == 0 { 
            a 
        } else { 
            Solution::gcd(b, a % b) 
        }
    }

    pub fn insert_greatest_common_divisors(
        mut head: Option<Box<ListNode>>
    ) -> Option<Box<ListNode>> {
        let mut current = &mut head;  // Pointer to traverse the linked list
        
        // Traverse the list until we reach the second last node
        while let Some(ref mut current_node) = current {
            if let Some(ref mut next_node) = current_node.next {
                // Calculate GCD of current node's value and next node's value
                let gcd_val = Solution::gcd(current_node.val, next_node.val);
                
                // Insert a new node with the GCD value between current_node and next_node
                let new_node = Some(Box::new(ListNode {
                    val: gcd_val,
                    next: current_node.next.take(),  // Link the new node to the next node
                }));

                // Link current node to the new node
                current_node.next = new_node;

                // Move current to the new node's next (the original next_node)
                current = &mut current_node.next.as_mut().unwrap().next;
            } else {
                // If there is no next node, we are at the end of the list
                break;
            }
        }
        
        head  // Return the modified list
    }
}

// Helper function to build a linked list from a vector of values
fn build_linked_list(values: Vec<i32>) -> Option<Box<ListNode>> {
    let mut head = None;
    let current = &mut head;
    
    for &value in values.iter().rev() {
        let new_node = Box::new(ListNode { val: value, next: current.take() });
        *current = Some(new_node);
    }
    
    head
}

// Helper function to convert a linked list back into a vector of values for easy testing
fn linked_list_to_vec(mut head: Option<Box<ListNode>>) -> Vec<i32> {
    let mut values = Vec::new();
    while let Some(node) = head {
        values.push(node.val);
        head = node.next;
    }
    values
}

fn main() {
    // Example 1: Input = [18,6,10,3], Expected Output = [18,6,6,2,10,1,3]
    let head = build_linked_list(vec![18, 6, 10, 3]);
    let modified_head = Solution::insert_greatest_common_divisors(head);
    let result = linked_list_to_vec(modified_head);
    println!("{:?}", result);  // Output: [18, 6, 6, 2, 10, 1, 3]

    // Example 2: Input = [7], Expected Output = [7]
    let head = build_linked_list(vec![7]);
    let modified_head = Solution::insert_greatest_common_divisors(head);
    let result = linked_list_to_vec(modified_head);
    println!("{:?}", result);  // Output: [7]
}
