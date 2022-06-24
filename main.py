import traceback
from fastapi import Request
from infer import sim
from app import app


@app.post('/api/sim')
async def api_sim(request: Request):
    """
    time curl -XPOST http://localhost:8000/api/sim \
        -H 'Content-Type: applicaton/json' \
        -d '{"a": "你好啊", "b": "你好"}'
    """
    data = await request.json()
    if 'a' not in data or not isinstance(data['a'], str):
        return {
            'ok': False,
            'error': 'Invalid a in post data',
        }
    if 'b' not in data or not isinstance(data['b'], str):
        return {
            'ok': False,
            'error': 'Invalid b in post data',
        }
    try:
        ret = sim(data['a'], data['b'])
        return {
            'ok': True,
            **ret
        }
    except Exception:
        return {
            'ok': False,
            'error': traceback.format_exc(),
        }


@app.get('/')
async def hello():
    return {
        'hello': 'world',
    }
