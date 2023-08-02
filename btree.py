


# 1.Implement Binary tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        self.root = self._insert_recursive(self.root, val)

    def _insert_recursive(self, root, val):
        if root is None:
            return TreeNode(val)
        
        if val < root.val:
            root.left = self._insert_recursive(root.left, val)
        else:
            root.right = self._insert_recursive(root.right, val)
        
        return root
    

# 2.Find height of a given tree
    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, root):
        if root is None:
            return 0
        
        left_height = self._height_recursive(root.left)
        right_height = self._height_recursive(root.right)
        
        return max(left_height, right_height) + 1
    
    
# 3.Perform Pre-order, Post-order, In-order traversal

    def pre_order(self):
        self._pre_order_recursive(self.root)
    
    def _pre_order_recursive(self, root):
        if root is not None:
            print(root.val, end=" ")
            self._pre_order_recursive(root.left)
            self._pre_order_recursive(root.right)

    def post_order(self):
        self._post_order_recursive(self.root)
    
    def _post_order_recursive(self, root):
        if root is not None:
            self._post_order_recursive(root.left)
            self._post_order_recursive(root.right)
            print(root.val, end=" ")

    def in_order(self):
        self._in_order_recursive(self.root)
    
    def _in_order_recursive(self, root):
        if root is not None:
            self._in_order_recursive(root.left)
            print(root.val, end=" ")
            self._in_order_recursive(root.right)




# 4.Function to print all the leaves in a given binary tree

    def print_leaves(self):
        self._print_leaves_recursive(self.root)
    
    def _print_leaves_recursive(self, root):
        if root is not None:
            if root.left is None and root.right is None:
                print(root.val, end=" ")
            else:
                self._print_leaves_recursive(root.left)
                self._print_leaves_recursive(root.right)


# 5.Implement BFS (Breath First Search) and DFS (Depth First Search)

    def bfs(self):
        if self.root is None:
            return
        
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print(node.val, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def dfs(self):
        self._dfs_recursive(self.root)

    def _dfs_recursive(self, root):
        if root is not None:
            print(root.val, end=" ")
            self._dfs_recursive(root.left)
            self._dfs_recursive(root.right)



# 6.Find sum of all left leaves in a given Binary Tree

    def sum_left_leaves(self):
        return self._sum_left_leaves_recursive(self.root, False)

    def _sum_left_leaves_recursive(self, root, is_left):
        if root is None:
            return 0

        if root.left is None and root.right is None and is_left:
            return root.val

        left_sum = self._sum_left_leaves_recursive(root.left, True)
        right_sum = self._sum_left_leaves_recursive(root.right, False)

        return left_sum + right_sum



# 7.Find sum of all nodes of the given perfect binary tree

    def sum_perfect_tree(self):
        height = self.height()
        num_nodes = 2 ** height - 1
        return num_nodes * (num_nodes + 1) // 2




# 8.Count subtress that sum up to a given value x in a binary tree

    def count_subtrees_with_sum(self, x):
        def _count_subtrees_with_sum_recursive(root):
            nonlocal count

            if root is None:
                return 0

            left_sum = _count_subtrees_with_sum_recursive(root.left)
            right_sum = _count_subtrees_with_sum_recursive(root.right)
            total_sum = left_sum + right_sum + root.val

            if total_sum == x:
                count += 1

            return total_sum

        count = 0
        _count_subtrees_with_sum_recursive(self.root)
        return count


# 9.Find maximum level sum in Binary Tree

    def max_level_sum(self):
        if self.root is None:
            return 0

        max_sum = float('-inf')
        level_sum = 0
        queue = [self.root, None]  # Using None as a level separator

        while queue:
            node = queue.pop(0)
            if node is None:
                max_sum = max(max_sum, level_sum)
                level_sum = 0
                if queue:
                    queue.append(None)  # Add level separator
            else:
                level_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return max_sum



# 10.Print the nodes at odd levels of a tree

    def print_odd_level_nodes(self):
        self._print_odd_level_nodes_recursive(self.root, 1)

    def _print_odd_level_nodes_recursive(self, root, level):
        if root is None:
            return

        if level % 2 != 0:
            print(root.val, end=" ")

        self._print_odd_level_nodes_recursive(root.left, level + 1)
        self._print_odd_level_nodes_recursive(root.right, level + 1)


tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(12)
tree.insert(18)

print("Height:", tree.height())

print("Pre-order traversal:")
tree.pre_order()

print("\nPost-order traversal:")
tree.post_order()

print("\nIn-order traversal:")
tree.in_order()

print("\nLeaves:")
tree.print_leaves()

print("\nBFS:")
tree.bfs()

print("\nDFS:")
tree.dfs()

print("\nSum of left leaves:", tree.sum_left_leaves())

print("Sum of nodes in perfect tree:", tree.sum_perfect_tree())

x = 30
print("Subtrees with sum", x, ":", tree.count_subtrees_with_sum(x))

print("Maximum level sum:", tree.max_level_sum())

print("Nodes at odd levels:")
tree.print_odd_level_nodes()
