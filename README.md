# Roberta-sts Docker Service

## deploy

for testing

```bash
$ docker run -it --rm -p 8000:8000 qhduan/roberta-sts
```

for service

```bash
$ docker run -d --restart=always -p 8000:8000 qhduan/roberta-sts
```

## test

```bash
$ time curl -XPOST http://localhost:8000/api/sim \
        -H 'Content-Type: applicaton/json' \
        -d '{"a": "你好啊", "b": "你好"}'
```