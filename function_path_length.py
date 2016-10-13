def len_curve(n):
    x = np.linspace(0, 1, n+1)
    dx = np.diff(x)
    dy = np.diff(x**2)
    ds = np.sqrt(dx**2 + dy**2)
    return np.around(np.sum(ds), decimals=9)
