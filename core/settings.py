# Manage settings by using pydantic.

from typing import Set
from pydantic import (
    BaseModel,
    BaseSettings,
    PyObject,
    RedisDsn,
    PostgresDsn,
    AmqpDsn,
    Field,
)


class SubModel(BaseModel):
    a: str = 'bar'
    b: int = 1


class Settings(BaseSettings):
    auth_key: str = Field(..., envvar='AUTH_KEY')
    api_key: str = Field(..., envvar='API_KEY')

    redis_dsn: RedisDsn = Field(..., envvar='REDIS_DSN')
    postgres_dsn: PostgresDsn = Field(..., envvar='POSTGRES_DSN')
    amqp_dsn: AmqpDsn = Field(..., envvar='AMQP_DSN')

    special_function: PyObject = 'math.cos'

    # to override domains:
    # export my_prefix_domains='["foo.com", "bar.com"]'
    domains: Set[str] = set()

    # to override more_settings:
    # export my_prefix_more_settings='{"a": "x", "b": 1}'
    more_settings: SubModel = SubModel()

    class Config:
        env_prefix = 'my_prefix_'
        env_file = '.env'
        env_file_encoding = 'utf-8'
        case_sensitive = True
        arbitrary_types_allowed = True
        fields = {
            'auth_key': str,
            'api_key': str,
            'redis_dsn': {
                'env': ['service_redis_dsn', 'redis_url']
            },
            # 'postgres_dsn': PostgresDsn,
            'amqp_dsn': {
                'env': ['service_amqp_dsn', 'amqp_url']
            },
        }


print(Settings().dict())
