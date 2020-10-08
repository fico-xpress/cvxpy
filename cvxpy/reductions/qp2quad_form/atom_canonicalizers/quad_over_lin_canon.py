"""
Copyright 2017 Robin Verschueren

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from cvxpy.expressions.variable import Variable
from cvxpy.atoms.quad_form import SymbolicQuadForm
from scipy.sparse import eye


def quad_over_lin_canon(expr, args):
    affine_expr = args[0]
    y = args[1]
    if isinstance(affine_expr, Variable):
        return SymbolicQuadForm(affine_expr, eye(affine_expr.size)/y, expr), []
    else:
        t = Variable(affine_expr.shape)
        return SymbolicQuadForm(t, eye(affine_expr.size)/y, expr), [affine_expr == t]
