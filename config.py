#! /usr/bin/env python
# -*- coding: utf-8 -*-


class CommonConfig(object):
    # 中间件配置
    # 默认使用的缓存后端
    CACHE_BACKEND = 'app.middlewares.CacheMiddleware'
    MIDDLEWARES = {
        # 缓存中间件
        CACHE_BACKEND: {
            "cache": "app.cache.RedisCache",        # 缓存后端类
            "expire": 60 * 30,                      # 缓存过期时间
            "password": ""         # 缓存后端的密码
        },

    }
    # web应用配置
    APP_SETTINGS = {}


class DevelopmentConfig(CommonConfig):
    APP_SETTINGS = {
        'debug': True
    }


class TestingConfig(CommonConfig):
    pass


class ProductionConfig(CommonConfig):
    pass


config_dict = {
    'dev': DevelopmentConfig,
    'test': TestingConfig,
    'prod': ProductionConfig
}