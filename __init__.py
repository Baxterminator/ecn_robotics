import sympy as sy
import numpy as np
from scipy import signal
from progress.bar import IncrementalBar


###########################################################
#                           DATA
#                        PROCESSING
###########################################################
class Data:
    def __init__(self):
        self.t = []
        self.q1 = []
        self.dq1 = []
        self.ddq1 = []
        self.q2 = []
        self.dq2 = []
        self.ddq2 = []
        self.T1 = []
        self.T2 = []

    def differentiate(self):
        self.dq1 = Data.derivatives(self.t, self.q1)
        self.ddq1 = Data.derivatives(self.t, self.dq1)
        self.dq2 = Data.derivatives(self.t, self.q2)
        self.ddq2 = Data.derivatives(self.t, self.dq2)

    def compute_torque(self, w_matrix: sy.Matrix, p_matrix: sy.Matrix, params: np.ndarray):
        self.T1 = []; self.T2 = []
        bar = IncrementalBar("Computing torque", max=len(self.ddq1))
        for i in range(len(self.ddq1)):
            wp = make_wp(w_matrix, p_matrix, [
                self.q1[i],
                self.dq1[i],
                self.ddq1[i],
                self.q2[i],
                self.dq2[i],
                self.ddq2[i]
            ])
            t = np.dot(wp, params)
            self.T1.append(t[0])
            self.T2.append(t[1])
            bar.next()
        bar.finish()

    @staticmethod
    def derivatives(time: list, table: list):
        dtable = [0]
        for i in range(1, len(table)-1):
            dtable.append(
                (table[i+1]-table[i-1])/(time[i+1]-time[i-1])
            )
        dtable.append(0)
        return dtable


def make_wp(w_matrix: sy.Matrix, p_matrix: sy.Matrix, data: list):
    return np.array(w_matrix.subs([
            (p_matrix[0], float(data[0])),
            (p_matrix[1], float(data[1])),
            (p_matrix[2], float(data[2])),
            (p_matrix[3], float(data[3])),
            (p_matrix[4], float(data[4])),
            (p_matrix[5], float(data[5])),
        ]), dtype=float)


def make_wtot(w_matrix: sy.Matrix, p_matrix: sy.Matrix or list, data: Data) -> np.ndarray:
    wtot = None
    bar = IncrementalBar("Making W", max=len(data.q1))
    for i in range(3, len(data.q1)-3):
        wp = make_wp(w_matrix, p_matrix, [
            data.q1[i],
            data.dq1[i],
            data.ddq1[i],
            data.q2[i],
            data.dq2[i],
            data.ddq2[i]
        ])
        if wtot is None:
            wtot = wp
        else:
            wtot = np.vstack([wtot, wp])
            bar.next()
    bar.finish()
    return wtot


def random_generator(n_samples: int) -> Data:
    data = Data()
    for i in range(n_samples):
        # Random vector
        q = 20 * (np.random.random([6, 1]) - 1 / 2)
        data.t = list(np.ones(n_samples))
        data.q1.append(q[0])
        data.q2.append(q[1])
        data.dq1.append(q[2])
        data.dq2.append(q[3])
        data.ddq1.append(q[4])
        data.ddq2.append(q[5])
    return data


def sinus_generator(w1: float, w2: float, dt=10, sub=500) -> Data:
    t = np.linspace(0, dt, sub)
    data = Data()
    data.t = list(t)
    for tk in t:
        data.q1.append(np.sin(w1 * tk))
        data.q2.append(np.sin(w2 * tk))
        data.differentiate()
    fe = float(sub)/float(dt)
    return [data, fe]


def from_file(file_number: int) -> Data:
    data = Data()
    file_name = f"data/randomDriving{file_number}.csv"
    with open(file_name, "r") as f:
        f.readline()
        line = f.readline()
        while line != "":
            l_data = line.split(",")
            data.t.append(float(l_data[0]))
            data.q1.append(float(l_data[1]))
            data.T1.append(float(l_data[2]))
            data.q2.append(float(l_data[3]))
            data.T2.append(float(l_data[4]))
            line = f.readline()
    data.differentiate()
    return data
