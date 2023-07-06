## 二分查找

### 1、二分查找
特点是：有序数组的/队列的查找。
[力扣：704. 二分查找](https://leetcode.cn/problems/binary-search/)

**题目**：给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。

```
示例 1:
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4 ,如果为匹配到返回 -1
```


```js
var search = function(nums, target) {
    let min = 0; 
    let max = nums.length - 1;
    while (min <= max) {
        let middle = Math.floor((min + max) / 2);
        if (nums[middle] === target)
            return middle;
        else if (nums[middle] < target) {
            min = middle + 1;
        } else {
            max = middle - 1;
        }
    }
    return -1;
};
```
n/2，n/4，n/8.... n/2^k => 2^k = n  => k = logN 
`时间复杂的：k= logN， 空间复杂度：`

解析：
1、从数组中间元素开始查找，如果 middle的🈯️ 等于 target直接返回，
2、否则分为两个数组，如果 x 小于 target 则，查找前数组，否则查找后数组。
重复 1-2 步骤，查到则返回，否则返回 - 1