---

# 🛣 Kubernetes & 分布式学习路线图（初学 → 高级）

## **阶段 1：基础概念入门（1–2 周）**

**目标**：理解 Kubernetes 核心概念，能在浏览器/本地搭集群执行基础操作

| 知识点                         | 内容                                  | 练习                                |
| --------------------------- | ----------------------------------- | --------------------------------- |
| Pod                         | 最小部署单元，生命周期                         | 创建 Pod，查看状态，删除 Pod                |
| Deployment / ReplicaSet     | 管理副本，保证服务高可用                        | 创建 Deployment，设置副本数，尝试滚动更新        |
| Service                     | ClusterIP / NodePort / LoadBalancer | 给 Deployment 暴露端口，测试访问            |
| ConfigMap / Secret          | 配置和密钥管理                             | 使用 ConfigMap 注入环境变量，Secret 加密敏感信息 |
| Volume / PVC / StorageClass | 持久化存储                               | 创建 PVC，绑定本地/MinIO 存储（模拟对象存储）      |

**练习平台**：

* Play-with-K8s ([https://labs.play-with-k8s.com/](https://labs.play-with-k8s.com/))
*
Killercoda ([https://killercoda.com/playgrounds/scenario/kubernetes](https://killercoda.com/playgrounds/scenario/kubernetes))

---

## **阶段 2：健康检查 & 无状态化实践（1 周）**

**目标**：掌握 Pod 健康监控，理解无状态化原则

| 知识点             | 内容          | 练习                               |
|-----------------|-------------|----------------------------------|
| Liveness Probe  | 容器存活检查      | 给 Pod 配置 `/health` 或自定义脚本 probe  |
| Readiness Probe | 服务就绪检查      | 配置 Readiness Probe，测试请求是否路由到 Pod |
| 无状态化            | Pod 不依赖本地文件 | 模拟将静态文件挂载到 MinIO / PV            |
| 初始化 & 分布式锁      | 控制多副本初始化    | 用 Redis 实现简单分布式锁控制初始化任务          |

---

## **阶段 3：流量调度 & 多副本管理（1–2 周）**

**目标**：理解多副本流量分发、扩缩容、负载均衡

| 知识点                             | 内容                     | 练习                    |
|---------------------------------|------------------------|-----------------------|
| Service LoadBalancer / Ingress  | 内部/外部流量调度              | 创建 Ingress 路由流量到不同服务  |
| Horizontal Pod Autoscaler (HPA) | Pod 自动扩缩容              | 根据 CPU / 自定义指标调整副本数   |
| Pod 调度策略                        | 节点亲和性 / Pod 亲和性 / 污点容忍 | 设置调度规则，让 Pod 只在特定节点运行 |
| ReplicaSet / Deployment 滚动更新    | 版本更新不中断服务              | 部署新版本应用，观察滚动更新效果      |

---

## **阶段 4：监控 & 日志 & 告警（1 周）**

**目标**：掌握指标采集、日志聚合、可视化面板与告警

| 知识点             | 内容             | 练习                               |
|-----------------|----------------|----------------------------------|
| Prometheus 指标采集 | 采集 CPU/内存、业务指标 | 使用 Prometheus Python SDK 采集自定义指标 |
| Grafana 面板      | 数据可视化          | 建立面板监控 Pod / Deployment / 自定义指标  |
| Loki / EFK 日志聚合 | 集中日志           | 配置 Loki + Promtail 收集日志并展示       |
| Alertmanager    | 告警             | 配置阈值告警，触发邮件/Slack 通知             |

---

## **阶段 5：容错 & 弹性设计（1–2 周）**

**目标**：理解多副本/多节点下的容错、弹性、分布式消息处理

| 知识点          | 内容                | 练习                            |
|--------------|-------------------|-------------------------------|
| 副本失败 & 自动重启  | K8s 重启策略          | 强制删除 Pod，观察 ReplicaSet 重建     |
| Leader 选举    | 单任务多副本时谁执行        | 用 Redis / Etcd 实现简单 Leader 选举 |
| 熔断 / 限流 / 降级 | 防止级联故障            | 学 Istio 或模拟微服务调用熔断            |
| 消息/任务幂等      | Pulsar / Kafka 消费 | 练习幂等消费设计，消息重试策略               |

---

## **阶段 6：进阶架构 & Service Mesh（可选，2 周）**

**目标**：理解云原生全栈，流量控制、策略管理、观测性增强

| 知识点                           | 内容                           | 练习                        |
|-------------------------------|------------------------------|---------------------------|
| Service Mesh（Istio / Linkerd） | 流量分配、灰度发布                    | 部署简单服务网格，设置流量路由           |
| 分布式事务 & 一致性                   | 事务协调、幂等性                     | 了解 2PC/3PC 原理，模拟事务操作      |
| 弹性架构                          | 容灾演练                         | 模拟节点故障，观察 HPA / Pod 重调度效果 |
| 高级监控                          | 链路追踪（Jaeger / OpenTelemetry） | 在服务间调用链中埋点，追踪请求流          |

---

## 🔹 每日学习/练习建议

| 时间       | 内容                             |
|----------|--------------------------------|
| 0–20min  | 阅读官方文档/概念视频                    |
| 20–40min | 在 Play-with-K8s 或本地集群练习命令 / 部署 |
| 40–60min | 做笔记，总结概念和操作原理                  |
| 加分       | 写一个小 demo，把多个知识点串起来            |

---

## 🔹 学习资源汇总

1. **官方文档**

    * Kubernetes: [https://kubernetes.io/docs/](https://kubernetes.io/docs/)
    * Prometheus: [https://prometheus.io/docs/introduction/overview/](https://prometheus.io/docs/introduction/overview/)
    * Grafana: [https://grafana.com/tutorials](https://grafana.com/tutorials)

2. **在线实践**

    * Play-with-K8s: [https://labs.play-with-k8s.com/](https://labs.play-with-k8s.com/)
    *
    Killercoda: [https://killercoda.com/playgrounds/scenario/kubernetes](https://killercoda.com/playgrounds/scenario/kubernetes)
    * Instruqt: [https://instruqt.com/](https://instruqt.com/)

3. **额外进阶**

    * Service Mesh: Istio [https://istio.io/latest/docs/](https://istio.io/latest/docs/)
    * 分布式事务 / 一致性: Wikipedia CAP / BASE
    * 日志聚合: Grafana Loki / EFK

---
