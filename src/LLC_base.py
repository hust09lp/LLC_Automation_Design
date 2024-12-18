import math

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

        if self.Vin_n >= self.Vo_n:
            self.np2s = round(self.Vin_n / self.Vo_n)
            self.ns2p = 1 / self.np2s
        else:
            self.ns2p = round(self.Vo_n / self.Vin_n)
            self.np2s = 1 / self.ns2p

        # 计算电路的最小最大增益
        self.Gmin = self.np2s * self.Vo_min / self.Vin_max
        self.Gmax = self.np2s * self.Vo_max / self.Vin_min

        # 计算等效交流内阻
        self.Rac_n = 2 * self.np2s**2 * self.Vo_n**2 / (math.pi**2 * self.Po)
        self.Rac_min = 2 * self.np2s ** 2 * self.Vo_min ** 2 / (math.pi ** 2 * self.Po)
        self.Rac_max = 2 * self.np2s ** 2 * self.Vo_max ** 2 / (math.pi ** 2 * self.Po)

        # 根据增益求解开关频率范围
        self.fmin = self.fr / math.sqrt(self.k * (1 - 1/self.Gmax**2) + 1)
        self.fmax = self.fr / math.sqrt(1 + self.k*(1-1/self.Gmin))

        # 计算最大品质因数，保留0.95的裕量
        self.Qmax = 0.95 * math.sqrt((self.Gmax**2 * (1+self.k) - self.k) / (self.Gmax**2 * self.k**2 * (self.Gmax**2-1)))

        # 计算谐振参数
        self.Lr = self.Qmax * self.Rac_min / (2 * math.pi * self.fr)
        self.Cr = 1 / (self.Qmax * self.Rac_min * 2 * math.pi * self.fr)
        self.Lm = self.k * self.Lr

    def output(self):
        print(f'Gmax is {self.Gmax}.')
        print(f'Gmin is {self.Gmin}.')
        print(f'Qmax is {self.Qmax}.')
        print(f'Lr is {self.Lr} H.')
        print(f'Cr is {self.Cr} F.')
        print(f'Lm is {self.Lm} H.')

# 做一个参数输入的交互
Vin_n = float(input('Please input the nominal input voltage (V): '))
Vin_min = float(input('Please input the minimum input voltage (V): '))
Vin_max = float(input('Please input the maximum input voltage (V): '))
Vo_n = float(input('Please input the nominal output voltage (V): '))
Vo_min = float(input('Please input the minimum output voltage (V): '))
Vo_max = float(input('Please input the maximum output voltage (V): '))
P = float(input('Please input the nominal power (W): '))
k = float(input('Please input the ratio of Lm/Lr: '))
fr = float(input('please input the resonant frequency (Hz): '))

para = [Vin_n, Vin_min, Vin_max, Vo_n, Vo_min, Vo_max, P, k, fr]

# 新建对象，并输出参数
LLC_converter = LLC(para)
LLC_converter.output()