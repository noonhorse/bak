## MQTT 
MQTT 模式按照 MQTT 标准，对 CoAP 的 Method 进行转义，只有简单的 Pub/Sub 行为，转义对照表如下：

| Method| Token|	MQTT 类型|
|:----|:----|:----|
|GET | 0 | Subscribe |
|GET | 1 | UnSubscribe |
|GET | _ | 非法操作 |
|PUT | _ | Publish |
|POST | _ | 非法操作 |
|DELETE | _ | 非法操作 |

该模式适用于以下场景:

- 只需要使用 EMQX 进行消息、指令或者其他实时信息传输
- 如果需要长时间使用 Observe 功能， 则需要处于专用网络或者内网中 这点比较重要，因为 UDP 是无连接的，所以在公网上产生的 UDP 链路是无法长时间保持的，这会导致 Observe 可能无法正常接受到数据
- 如果处于公网，则 Observe 只能用来做为 PUT 操作的结果监听机制，例如: 假设一个 CoAP 设备需要通过 EMQX 向另外的其他设备发送指令、数据，并且根据返回的数据进行后续处理，则可以:
  - 使用 PUT 方法向某个 Topic 发送指令
  - 使用 Observe 方式监听这个 Topic
  - 根据 EMQX 返回的数据进行处理 鉴于公网中 UDP 链路的维持时间，Observe 的时间在 30s 以内是安全的，在 15s 内是足够安全的


## 文章参考
[一文解决 CoAP 协议设备与外部网络沟通难题](https://www.emqx.com/zh/blog/connecting-coap-devices-to-emqx)
[CoAp协议说明](./iot-co-ap-protocol.md)