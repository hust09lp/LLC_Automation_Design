# define the LLC converter class
class LLC:
    # 我的想法时最好直接传递一个输入参数字典{Vin, Vo, P, k, fr}过来
    def __init__(self, input_para):
        self.Vin_n   = input_para[0]
        self.Vin_min = input_para[1]
        self.Vin_max = input_para[2]
        self.Vo_n    = input_para[3]
        self.Vo_min  = input_para[4]
        self.Vo_max  = input_para[5]
        self.Po      = input_para[6]
        self.k       = input_para[7]
        self.fr      = input_para[8]

    # 计算谐振参数{Lr, Cr, Lm}
    def calc(self):
        # 首先计算隔离变压器匝比
        if self.Vin_n >= self.Vo_n:
            self.np2s = round(self.Vin_n / self.Vo_n)
            self.ns2p = 1 / self.np2s
        else:
            self.ns2p = round(self.Vo_n / self.Vin_n)
            self.np2s = 1 / self.ns2p

        # 计算电路的最小最大增益
        self.Gmin =
        self.Gmax =

        # 根据增益求解开关频率范围
        self.fmax =
        self.fmin =

    # 绘制增益图
    def plot_G(self):