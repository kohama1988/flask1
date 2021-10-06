from redis import StrictRedis

# 创建redis对象，关联IP和端口, decode_response取出数据自动解码
redis_store = StrictRedis(host='127.0.0.1', port=6379, decode_responses=True)

# 增加数据，key，value，有效期
redis_store.set('name', 'kohama', 5) # 可以设置有效期5s

# 更改数据
redis_store.set('name','hisae')

# 获取数据
name = redis_store.get('name')
print(name)

# 删除数据
redis_store.delete('name')