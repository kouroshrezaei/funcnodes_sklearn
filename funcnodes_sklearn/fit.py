from funcnodes import Shelf, NodeDecorator
from typing import Optional, Callable, Union
import numpy as np
from sklearn.base import BaseEstimator
import inspect

@NodeDecorator(
    node_id="sklearn.fit",
    name="fit",
)
def _fit(
    model: Union[BaseEstimator, Callable[[], BaseEstimator]],
    X: np.ndarray,
    y: Optional[np.ndarray] = None,
) -> BaseEstimator:
    if not isinstance(model, BaseEstimator):
        model = model()

    # Get the signature of the fit method
    fit_signature = inspect.signature(model.fit)
    parameter_names = list(fit_signature.parameters.keys())
    
    if len(parameter_names) == 1:
        return model.fit(X)
    else:
        return model.fit(X, y)    
    # # Determine if 'y' is in the parameters of the fit method
    # if 'y' in fit_signature.parameters:
    #     # Check if 'y' is optional
    #     if fit_signature.parameters['y'].default == inspect.Parameter.empty:
    #         # 'y' is a required parameter, ensure 'y' is provided
    #         if y is None:
    #             raise ValueError("The 'y' parameter is required for this model's fit method.")
    #         return model.fit(X, y)
    #     else:
    #         # 'y' is an optional parameter, include it if provided
    #         return model.fit(X, y) if y is not None else model.fit(X)
    # else:
    #     # 'y' is not a parameter in the fit method
    #     return model.fit(X)



@NodeDecorator(
    node_id="sklearn.fit_transform",
    name="fit_transform",
)
def _fit_transform(
    model: Union[BaseEstimator, Callable[[], BaseEstimator]],
    X: np.ndarray,
    y: Optional[np.ndarray] = None,
) -> np.ndarray:

    def apply_fit_transform():
        if not isinstance(model.fit_transform(X, y), np.ndarray):
            return model.fit_transform(X, y).toarray()
        else:
            return model.fit_transform(X, y)

    return apply_fit_transform


@NodeDecorator(
    node_id="sklearn.inverse_transform",
    name="inverse_transform",
)
def _inverse_transform(
    model: Union[BaseEstimator, Callable[[], BaseEstimator]],
    X: np.ndarray,
) -> np.ndarray:

    def apply_inverse_transform():
        if not isinstance(model.inverse_transform(X), np.ndarray):
            return model.inverse_transform(X).toarray()
        else:
            return model.inverse_transform(X)

    return apply_inverse_transform


@NodeDecorator(
    node_id="sklearn.transform",
    name="transform",
)
def _transform(
    model: Union[BaseEstimator, Callable[[], BaseEstimator]],
    X: np.ndarray,
) -> np.ndarray:

    def apply_transform():
        if not isinstance(model.transform(X), np.ndarray):
            return model.transform(X).toarray()
        else:
            return model.transform(X)

    return apply_transform


FIT_NODE_SHELFE = Shelf(
    nodes=[_fit, _fit_transform, _inverse_transform, _transform],
    subshelves=[],
    name="Fit",
    description="Methods for fitting, transforming, and more.",
)
