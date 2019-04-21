# Basic information
## <a name="about">About</a>
This project's goal is to build [Yandex ClickHouse](https://clickhouse.yandex/) database into [Django](https://www.djangoproject.com/) project.  
It is based on [infi.clickhouse-orm](https://github.com/Infinidat/infi.clickhouse_orm) library.  

## <a name="features">Features</a>
* Multiple ClickHouse database configuration in [settings.py](https://docs.djangoproject.com/en/2.1/ref/settings/)
* ORM to create and manage ClickHouse models.
* ClickHouse migration system.
* Scalable serialization of django model instances to ORM model instances.
* Effective periodical synchronization of django models to ClickHouse without loosing data.
* Synchronization process monitoring.

## <a name="requirements">Requirements</a>
* [Python 3](https://www.python.org/downloads/)
* [Django](https://docs.djangoproject.com/) 1.7+
* [Yandex ClickHouse](https://clickhouse.yandex/)
* [infi.clickhouse-orm](https://github.com/Infinidat/infi.clickhouse_orm)
* pytz
* six
* typing
* psycopg2
* celery
* statsd

### Optional libraries
* [redis-py](https://redis-py.readthedocs.io/en/latest/) for [RedisStorage](storages.md#redis_storage)
* [django-pg-returning](https://travis-ci.com/M1hacka/django-pg-returning) 
  for optimizing registering updates in [PostgreSQL](https://www.postgresql.org/)

## <a name="installation">Installation</a>
Install via pip:  
`pip install django-clickhouse` ([not released yet](https://github.com/carrotquest/django-clickhouse/issues/3))    
or via setup.py:  
`python setup.py install`