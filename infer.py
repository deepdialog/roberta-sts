import os
from functools import lru_cache

import numpy as np
from scipy.special import softmax
from onnxruntime import GraphOptimizationLevel, InferenceSession, SessionOptions, get_all_providers
from transformers import BertTokenizer


def create_model_for_provider(model_path: str, provider: str= 'CPUExecutionProvider') -> InferenceSession:
    assert provider in get_all_providers(), f"provider {provider} not found, {get_all_providers()}"
    # Few properties that might have an impact on performances (provided by MS)
    options = SessionOptions()
    options.intra_op_num_threads = int(os.environ.get('NUM_THREADS', 4))
    options.graph_optimization_level = GraphOptimizationLevel.ORT_ENABLE_ALL
    # Load the model as a graph and prepare the CPU backend
    session = InferenceSession(model_path, options, providers=[provider])
    session.disable_fallback()
    return session


@lru_cache(maxsize=1000)
def sim(texta, textb):
    inputs = np.array([tokenizer.encode(texta, textb)], dtype=np.int64)
    logits = model.run(None, {
        "input": inputs
    })[0]
    probs = softmax(logits)
    label = '相似' if probs.argmax(-1)[0] == 1 else '不同'
    return {
        'logits': logits.astype(float).tolist()[0],
        'softmax': probs.astype(float).tolist()[0],
        'prob': probs.astype(float).tolist()[0][1],
        'label': label
    }


print('model loading')
CURERENT_DIR = os.path.realpath(os.path.dirname(__file__))
tokenizer = BertTokenizer.from_pretrained(os.path.join(CURERENT_DIR, 'roberta_sts_tokenizer'))
model = create_model_for_provider(os.path.join(CURERENT_DIR, 'roberta_sts_300m.quant.onnx'))
print('model green')


if __name__ == '__main__':
    print(sim('你好', 'hello'))
