# x^4 + y^2 + 2xy + 1
import numpy as np
import copy

def grad(u):
	x, y = u
	return np.array([
		4*x**3 + 2*y,
		2*y + 2*x
])

def hessian(u):
    x, y = u
    return np.array([
        [12*x**2, 2],
        [2, 2]
    ])

def newton_optimizer(grad_fn, hessian_fn, u_0, tol=1e-8, max_iter=100):
    history = [u_0]
    u = u_0.copy()
    for _ in range(max_iter):
        grad = grad_fn(u)
        if np.linalg.norm(grad) <= tol:
            break

        hessian = hessian_fn(u)
        #hessian_inv = np.linalg.inv(hessian)
        #u = u - grad @ hessian_inv

        a = np.linalg.solve(hessian, grad)
        u = u - a
        history.append(copy.deepcopy(u))

    return history, u

u_0 = np.array([1.0, 2.0])
history, u = newton_optimizer(grad, hessian, u_0, max_iter=1_000)
print(u)