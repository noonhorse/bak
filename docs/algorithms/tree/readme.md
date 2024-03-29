## 树的性质：

只有一个根节点；
除了根节点，所有节点都有且只有一个父节点；
无环。将任意一个节点作为起始节点，都不存在任何回到该起始节点的路径。（正是前两个性质保证了无环的成立。）

## 树中使用的术语
 - 根（Root）：树中最顶端的节点，根没有父节点。
 - 子节点（Child）：节点所拥有子树的根节点称为该节点的子节点。
 - 父节点（Parent）：如果节点拥有子节点，则该节点为子节点的父节点。
 - 兄弟节点（Sibling）：与节点拥有相同父节点的节点。
 - 子孙节点（Descendant）：节点向下路径上可达的节点。
 - 叶节点（Leaf）：没有子节点的节点。
 - 内节点（Internal Node）：至少有一个子节点的节点。
 - 度（Degree）：节点拥有子树的数量。
 - 边（Edge）：两个节点中间的链接。
 - 路径（Path）：从节点到子孙节点过程中的边和节点所组成的序列。
 - 层级（Level）：根为 Level 0 层，根的子节点为 Level 1 层，以此类推。
 - 高度（Height）/深度（Depth）：树中层的数量。比如只有 Level 0,Level 1,Level 2 则高度为 3。

## 

## 树的应用

 ### 1、红黑树