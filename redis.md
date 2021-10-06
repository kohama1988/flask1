### Redis特性
- Redis支持数据的持久化，可以将内存中的数据保存在硬盘中，重启的时候可以再次加载进行使用
- Redis不仅仅支持简单的key-value类型的数据，同时还提供list，set，zset，hash等数据结构的存储
- Redis支持数据的备份，即master-slave模式的数据备份

### Redis优势
- 性能极高，Redis读的速度是110000次/s，写的速度是81000次/s
- 丰富的数据类型，Redis支持二进制案例的Strings，Lists，Hashes，Sets及Ordered Sets数据类型操作
- 原子，Redis的所有操作都是原子性的，同时Redis还支持对几个操作全并后的原子性执行
- 丰富的特性，Redis还支持publis/subscribe，通知，key过期等等特性

### Redis应用场景
- 用来做缓存(memcached等)，Redis的所有数据都是放在内存中
- 可以在某些特定应用场景下替代传统出具库，比如社交类的应用
- 在一些大型系统中，巧妙的实现一些特定的功能，session共享，购物车

### 核心配置选项
- 绑定IP：127.0.0.1
- 端口： 6379
- 是否以守护进程运行:yes(不会在命令行阻塞，类似于服务) or no(当前终端被阻塞) daemonize yes
- 数据文件：dbfilename dump.rdb
- 数据文件存储路径：/var/lib/redis #linux中
- 数据库：默认16个 database 16

### 终端启动Redis
- redis-server