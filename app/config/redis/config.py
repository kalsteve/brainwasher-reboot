import redis, os

def get_redis_client():
    host = os.environ.get('REDIS_HOST')
    port = os.environ.get('REDIS_PORT')
    password = os.environ.get('REDIS_PASSWORD')
    db = os.environ.get('REDIS_DB')  # 기본값을 0으로 설정

    return redis.StrictRedis(
        host=host,
        port=int(port),
        password=password,
        db=int(db)
    )