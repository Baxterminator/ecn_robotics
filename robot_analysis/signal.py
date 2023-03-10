import numpy as np
from scipy import signal
from robot_analysis.robot_analysis.display import print_matrix


def add_quant_noise(table: list, step_quant: float, name="") -> list:
    print_matrix(np.array([len(table), step_quant], dtype=float),
                 name=f"Quant Noise {name}",
                 xaxis=["N elems", "Quant. Step"],
                 yaxis=["Params"],
                 width=18)
    out = []
    for x in table:
        out.append(int(x/step_quant)*step_quant)
    return out


def add_gauss_noise(table: list, sigma: float, mu=0, name="") -> list:
    print_matrix(np.array([len(table), 0, sigma], dtype=float),
                 name=f"Gauss Noise {name}",
                 xaxis=["N elems", "μ", "σ"],
                 yaxis=["Params"],
                 width=18)
    out = []
    for x in table:
        out.append(x+np.random.normal(mu, sigma))
    return out


def butter_data(table: list, f: float, fe: float, order=4, name="") -> np.ndarray:
    wn = f / (2 * fe)
    print_matrix(np.array([len(table), 2*order, fe, f, wn], dtype=float),
                 name=f"LBwF {name}",
                 xaxis=["N elems", "order", "Frequency", "Samp. Freq.", "Pulsation"],
                 yaxis=["Params"],
                 width=18)
    b, a = signal.butter(order, wn, "low")
    out = signal.filtfilt(b, a, table)
    return out
