## 二叉树的插入

## 二叉树的删除

## 二叉树的遍历

二叉查找树（BST：Binary Search Tree）是一种特殊的二叉树，它改善了二叉树节点查找的效率。二叉查找树有以下性质：
对于任意一个节点 n，
其左子树（left subtree）下的每个后代节点（descendant node）的值都小于节点 n 的值；
其右子树（right subtree）下的每个后代节点的值都大于节点 n 的值

- 广度优先遍历(Breadth-First Search) BFS
- 深度优先遍历(Depth-First-Search) DFS
  - 前序遍历
  - 中序遍历
  - 后续遍历

## 对比

bfs 遍历节点是先进先出，一般使用队列作为辅助数据结构，dfs遍历节点是先进后出，一般使用栈作为辅助数据结构；

前序遍历：1  2  4  5  7  8  3  6
中序遍历：4  2  7  5  8  1  3  6
后序遍历：4  7  8  5  2  6  3  1
层次遍历：1  2  3  4  5  6  7  8

### BFS 广度优先遍历

BFS搜索方式
步骤 1：从源点出发，访问源点的邻居结点，将邻居节点依次放入队列中，并标记为已访问；
步骤 2：取出队列中的邻居结点，依次访问每个节点未被访问的邻居节点；
步骤 3：将邻居节点依次放入队列中，并标记为已访问；
步骤 4：重复步骤 2~3 直到访问到目标节点或所有节点都标记为已访问。

bfs 适用于求源点与目标节点距离近的情况，例如：求最短路径
![Alt text](/assets/img/algorithms/bfs-binary-tree.png)

```java
public void levelTraverse(TreeNode root) {
		if (root == null) {
			return;
		}
		LinkedList<TreeNode> queue = new LinkedList<>();
		queue.offer(root);
		while (!queue.isEmpty()) {
			TreeNode node = queue.poll();
			System.out.print(node.val+"  ");
			if (node.left != null) {
				queue.offer(node.left);
			}
			if (node.right != null) {
				queue.offer(node.right);
			}
		}
	}

```

### DFS 深度优先遍历

DFS搜索方式

步骤 1：从源点出发，访问源点的某个邻居节点，将其放入栈中，并标记为已访问；
步骤 2：从栈中取出一个节点，访问该节点的未被访问的邻居节点；
步骤 3：将邻居节点放入栈中，并标记为已访问；
步骤 4：重复步骤 2 ~ 3，直到访问到目标节点或所有节点都标记为已访问；

dfs 更适合于求解一个任意符合方案中的一个或者遍历所有情况，例如：全排列、拓扑排序、求到达某一点的任意一条路径。


![tree](/assets/img/algorithms/binary-tree.jpg)
#### 1、前序遍历

根据上文提到的遍历思路：根结点 ---> 左子树 ---> 右子树，很容易写出递归版本：

```java
// 递归版本
public void preOrderTraverse1(TreeNode root) {
  if (root != null) {
   System.out.print(root.val + "  ");
   preOrderTraverse1(root.left);
   preOrderTraverse1(root.right);
  }
 }

// 非递归版本
public void preOrderTraverse2(TreeNode root) {
  LinkedList<TreeNode> stack = new LinkedList<>();
  TreeNode pNode = root;
  while (pNode != null || !stack.isEmpty()) {
   if (pNode != null) {
    System.out.print(pNode.val+"  ");
    stack.push(pNode);
    pNode = pNode.left;
   } else { //pNode == null && !stack.isEmpty()
    TreeNode node = stack.pop();
    pNode = node.right;
   }
  }
 }
```

#### 2、中序遍历
根据上文提到的遍历思路：左子树 ---> 根结点 ---> 右子树，很容易写出递归版本：

```java
public void inOrderTraverse1(TreeNode root) {
		if (root != null) {
			inOrderTraverse1(root.left);
			System.out.print(root.val+"  ");
			inOrderTraverse1(root.right);
		}
	}
// 非递归版本
public void inOrderTraverse2(TreeNode root) {
		LinkedList<TreeNode> stack = new LinkedList<>();
		TreeNode pNode = root;
		while (pNode != null || !stack.isEmpty()) {
			if (pNode != null) {
				stack.push(pNode);
				pNode = pNode.left;
			} else { //pNode == null && !stack.isEmpty()
				TreeNode node = stack.pop();
				System.out.print(node.val+"  ");
				pNode = node.right;
			}
		}
	}
```

#### 4、后序遍历
根据上文提到的遍历思路：左子树 ---> 右子树 ---> 根结点，很容易写出递归版本：

```java
public void postOrderTraverse1(TreeNode root) {
		if (root != null) {
			postOrderTraverse1(root.left);
			postOrderTraverse1(root.right);
			System.out.print(root.val+"  ");
		}
	}

```

### 题目

#### 1、查询二叉树的最大深度

```json
const tree = {
    value: 3,
    left: {
        value: 9
    },
    right: {
        value: 20,
        left: { value: 15 },
        right: { value: 9 }
    }
}
```

```js
var maxDepth = function(root) {
  if (!root) {
    return 0;
  }
  const leftDeep = maxDepth(root.left) + 1;
  const rightDeep = maxDepth(root.right) + 1;
  return Math.max(leftDeep, rightDeep);
};
```

#### 2、查询二叉树的所有路径

```js
var binaryTreePaths = function(root) {
  if (!root) return [];
  const res = [];
  function dfs(curNode, curPath) {
    if(!curNode.left && !curNode.right) {
      res.push(curPath);
    }
    if(curNode.left) {
      dfs(curNode.left, `${curPath}->${curNode.left.value}`)
    }
    if(curNode.right) {
      dfs(curNode.right, `${curPath}->${curNode.right.value}`)
    }
  }
  dfs(root, `${root.value}`);
  return res;
};
```
