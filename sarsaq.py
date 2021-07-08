import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from IPython.display import HTML

theta_0 = np.array([
    [np.nan,1,1,np.nan],
    [np.nan,1,1,1],
    [np.nan,np.nan,np.nan,1],
    [1,np.nan,1,np.nan],
    [1,1,np.nan,np.nan],
    [np.nan,np.nan,1,1],
    [1,1,np.nan,np.nan],
    [np.nan,np.nan,np.nan,1]])

def get_pi(theta):
    [m,n] = theta.shape
    pi = np.zeros((m,n))
    for i in range(0,m):
        pi[i,:] = theta[i,:] / np.nansum(theta[i,:])
    pi = np.nan_to_num(pi)
    return pi

pi_0 = get_pi(theta_0)

def get_s_next(s,a):
    if a == 0:
        return s -3
    elif a == 1:
        return s + 1
    elif a == 2:
        return s + 3
    elif a == 3:
        return s - 1

[a,b] = theta_0.shape
Q = np.random.rand(a,b) * theta_0

def get_a(s,Q,epsilon,pi_0):
    if np.random.rand() < epsilon:
        return np.random.choice([0,1,2,3],p = pi_0[s])
    else:
        return np.nanargmax(Q[s])

def sarsa(s,a,r,s_next,a_next,Q):
    eta = 0.1
    gamma = 0.9

    if s_next == 8:
        Q[s,a] = Q[s,a] + eta * (r-Q[s,a])
    else:
        Q[s,a] = Q[s,a] + eta * (r + gamma * Q[s_next,a_next] - Q[s,a])
    return Q

def q_learning(s,a,r,s_next,a_next,Q):
    eta = 0.1
    gamma = 0.9

    if s_next == 8:
        Q[s,a] = Q[s,a] + eta * (r-Q[s,a])
    else:
        Q[s,a] = Q[s,a] + eta * (r + gamma * np.nanmax(Q[s_next,:]) - Q[s,a])
    return Q

def play(Q,epsilon,pi):
    s = 0
    a = a_next = get_a(s,Q,epsilon,pi)
    s_a_history = [[0,np.nan]]

    while True:
        a = a_next
        s_next = get_s_next(s,a)

        s_a_history[-1][1] = a
        s_a_history.append([s_next,np.nan])

        if s_next == 8:
            r = 1
            a_next = np.nan
        else:
            r = 0
            a_next = get_a(s_next,Q,epsilon,pi)

        Q = sarsa(s,a,r,s_next,a_next,Q)
        if s_next == 8:
            break
        else:
            s = s_next

    return [s_a_history,Q]

epsilon = 0.5
for episode in range(10):
    epsilon = epsilon / 2
    [s_a_history,Q] = play(Q,epsilon,pi_0)
    print('episode:{},step:{},epsilon:{}'.format(episode,len(s_a_history)-1,epsilon))
    print(Q,'\n')
    print('Hello')
