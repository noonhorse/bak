# react effect hook Error

1、错误提示

```
react-17.0.2.development.js:3424 Warning: Can't perform a React state update on an unmounted component. This is a no-op, but it indicates a memory leak in your application. To fix, cancel all subscriptions and asynchronous tasks in a useEffect cleanup function.
```

提示内存泄漏，需要在组件内取消订阅。

解决办法，useEffect的第一个参数应该返回一个函数，用来取消事件监听。

## 参考
https://blog.csdn.net/u011607490/article/details/88953692

https://stackoverflow.com/questions/56450975/to-fix-cancel-all-subscriptions-and-asynchronous-tasks-in-a-useeffect-cleanup-f
