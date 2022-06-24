# Roberta-sts Docker Service

## deploy

for testing

```bash
docker run -it --rm --name roberta-sts -p 8000:8000 qhduan/roberta-sts
```

for service

```bash
docker run -d --restart=always --name roberta-sts -p 8000:8000 qhduan/roberta-sts
```

## test

```bash
curl -XPOST http://localhost:8000/api/sim \
        -H 'Content-Type: applicaton/json' \
        -d '{"a": "你好啊", "b": "你好"}'

# {"ok":true,"logits":[-2.5476226806640625,2.755629539489746],"softmax":[0.004950755275785923,0.9950491189956665],"prob":0.9950491189956665,"label":"相似"}

curl -XPOST http://localhost:8000/api/sim \
        -H 'Content-Type: applicaton/json' \
        -d '{"a": "我要去吃饭", "b": "我不去吃饭"}'

# {"ok":true,"logits":[3.879629135131836,-3.7278754711151123],"softmax":[0.9995034337043762,0.0004964632098563015],"prob":0.0004964632098563015,"label":"不同"}
```