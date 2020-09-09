import numpy as np
from scipy.misc import derivative
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
def fn_plot1d(fn, x_min, x_max, filename):
    func=np.vectorize(fn)
    x=np.linspace(x_min, x_max, (x_max-x_min)*100+1)
    plt.figure()
    y=func(x)
    plt.plot(x,y)
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel('fn(X)')
    plt.title('graph of single variable function')
    plt.savefig(filename)

def fn_plot2d(fn, x_min, x_max, y_min, y_max, filename):
    func=np.vectorize(fn)
    x=np.linspace(x_min, x_max, 100)
    y=np.linspace(y_min, y_max, 100)
    X, Y= np.meshgrid(x, y)
    Z=func(X, Y)
    fig=plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_surface(X, Y, Z)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('fn(x, y)')
    plt.title('graph of 2 variable function')
    plt.savefig(filename)

def nth_derivative_plotter(fn, n, xmin, xmax, filename):
    func=np.vectorize(fn)
    x=np.linspace(xmin, xmax, (xmax-xmin)*100+1)
    y=derivative(func, n=n, x0=x, dx=1e-6)
    plt.figure()
    plt.plot(x,y)
    plt.xlabel("X")
    plt.ylabel("f'(x)")
    plt.title('graph of '+ str(n)+'th derivative of function')
    plt.grid(True)
    plt.savefig(filename)

h=lambda x: np.exp(-1/(x**2)) if x>0 else 0
g=lambda x: h(2-x)/(h(2-x)+h(x-1))
b=lambda x: g(abs(x))
fn_plot1d(b, -2, 2, "fn1plot.png")

dist= lambda x, y: np.math.sqrt(x**2+y**2)
sinc=lambda x, y: np.math.sin(dist(x, y))/dist(x, y) if dist(x, y)>0 else 1
pi=np.math.pi
fn_plot2d(sinc, -1.5*pi, 1.5*pi, -1.5*pi, 1.5*pi, "fn2plot.png")

nth_derivative_plotter(b, 1, -2, 2, 'bd_1.png')
nth_derivative_plotter(b, 2, -2, 2, 'bd_2.png')