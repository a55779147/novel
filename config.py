class DevConfig:
    """DevConfig
    开发环境
    """
    HOST = 'http://127.0.0.1:5000'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:\
            3306/novel?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProConfig:
    """ProConfig
    生产环境
    """
    HOST = 'https://novel.buglan.org'
    SQLALCHEMY_DATABASE_URI = 'pymysql+mysql://root:root@127.0.0.1:\
            3306/novel?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = True


config = {
        'dev': DevConfig,
        'pro': ProConfig
        }
