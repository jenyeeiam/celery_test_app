# celery_test_app
brew install rabbitmq
mkvirtualenv celery_test_app

add `export PATH="$PATH:/usr/local/sbin` to .profile (or equivalent)

(if necessary)
brew services stop rabbitmq

sudo rabbitmq-server

pip install celery

celery -A tasks worker --loglevel=INFO

```
import tasks
tasks.add.delay(1,2)
```
