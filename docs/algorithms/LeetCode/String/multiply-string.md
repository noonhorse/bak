# 43 字符串相乘

[力扣.43](https://leetcode.cn/problems/multiply-strings/)

给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。

```shell
示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"


示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
```

**方法一**

一般计算法，对应数的位数相乘，在将各个数的结果相加

```javascript

const multiply = (first: string, second: string): string => {
  // 0 直接返回
  if (first === "0" || second === "0") return "0";
  let result = "0";
  const m = first.length;
  const n = second.length;
  for (let i = n - 1; i >= 0; i--) {
    //
    const padEnd = "".padEnd(n - 1 - i, "0"); // 如 十位数相乘值要补零
    let currentValue = "" + padEnd;

    let carry = 0; // 内部的进位
    for (let k = m - 1; k >= 0; k--) {
      // 字符串相乘隐式转换类型
      const v = parseInt(first[k], 10) * parseInt(second[i], 10) + carry;
      carry = v > 9 ? Math.floor(v / 10) : 0;
      currentValue = (v % 10) + currentValue;
    }
    if (carry > 0) {
      currentValue = carry + currentValue;
    }

    result = addNumber(result, currentValue);
  }
  return result;
};
/*
 * 大数相加
 */
const addNumber = (first: string, second: string) => {
  //取两个数字的最大长度
  const maxLength = Math.max(first.length, second.length);
  //用0去补齐长度
  const a = first.padStart(maxLength, "0");
  const b = second.padStart(maxLength, "0");
  //定义加法过程中需要用到的变量
  let current = 0;
  let carry = 0; //"进位"
  let sum = "";
  for (let i = maxLength - 1; i >= 0; i--) {
    current = parseInt(a[i]) + parseInt(b[i]) + carry;
    carry = current > 9 ? 1 : 0;
    sum = (current % 10) + sum;
  }
  // 首位进位
  if (carry === 1) {
    sum = "1" + sum;
  }
  return sum;
};
```

**方法二** 

利用数学特性，相乘的两个数不超过个数之和

```javascript
// 数理优化
const multiply2 = (first: string, second: string): string => {
  if (first === "0" || second === "0") return "0";
  const m = first.length;
  const n = second.length;
  // 两数相乘，最大长度不超过两个数个数和。9 * 9 = 81; 9 * 10 = 90 < 100；10 * 10 = 100 < 1000
  let result = new Array(m + n).fill(0); 
  /**
   *  竖项相乘
   */
  for (let i = m - 1; i >= 0; i--) {
    for (let j = n - 1; j >= 0; j--) {
      const carry = first[i] * second[j] + result[i + j + 1];
      result[i + j + 1] = carry % 10; 
      result[i + j] = result[i + j] + Math.floor(carry / 10); // 进位处理
    }
  }
  // 循环删除首位被填充 0 的情况
  while (result[0] === 0) {
    result.shift();
  }
  return result.join("");
};
```


## 计算阶乘

题目：计算100的阶乘，要求是精确值

```javascript
const factorial = (num: number): string => {
  if (num <= 1) return "1";
  return multiply(factorial(num - 1), String(num));
};
```


## 计算阶乘后的零的个数

[力扣-172]https://leetcode.cn/problems/factorial-trailing-zeroes/
给定一个整数 n ，返回 n! 结果中尾随零的数量。

提示 n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1


```shell
示例 1：

输入：n = 3
输出：0
解释：3! = 6 ，不含尾随 0

示例 2：

输入：n = 5
输出：1
解释：5! = 120 ，有一个尾随 0
```