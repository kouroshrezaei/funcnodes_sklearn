import unittest
import funcnodes as fn
import numpy as np
from funcnodes_sklearn.metrics import (
    _confusion_matrix,
    
    
)

class TestMetrics(unittest.IsolatedAsyncioTestCase):
    async def test_confusion_matrix(self):
        y_true = [2, 0, 2, 2, 0, 1]
        y_pred = [0, 0, 2, 2, 0, 2]
        metric: fn.Node = _confusion_matrix()
        metric.inputs["y_true"].value = y_true
        metric.inputs["y_pred"].value = y_pred
        self.assertIsInstance(metric, fn.Node)
        await metric
        out = metric.outputs["out"]
        self.assertEqual(out.value.tolist(), [[2, 0, 0], [0, 0, 1], [1, 0, 2]])

# from sklearn.metrics import confusion_matrix
# y_true = [2, 0, 2, 2, 0, 1]
# y_pred = [0, 0, 2, 2, 0, 2]
# confusion_matrix(y_true, y_pred)