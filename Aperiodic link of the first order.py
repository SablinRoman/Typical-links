import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid()

k = 10
T = 0.1


# Весовая функция
def weight_function():
    ax.set(xlim=[0, 1])

    x = np.linspace(0, 5, 100)
    y = 100 * np.exp(-10 * x)
    ax.plot(x, y)

    ax.set_xlabel(r'$t$', fontsize=14)
    ax.set_ylabel(r'$W(t)$', fontsize=14)

    fig.savefig('Graphics/Aperiodic link of the first order/Весовая функция')


# Переходная функция
def transition_function():
    ax.set(xlim=[0, 2])

    x = np.linspace(0, 5, 100)
    y = k * (1 - np.exp(-x / T))
    ax.plot(x, y)

    ax.set_xlabel(r'$t$', fontsize=14)
    ax.set_ylabel(r'$h(t)$', fontsize=14)

    fig.savefig('Graphics/Aperiodic link of the first order/Переходная функция')


# ФЧХ
def phase_frequency_characteristic():
    # ax.set(xlim=[0, 150])
    w = np.linspace(0, 100)

    ax.plot(x, y)

    ax.set_xlabel(r'$\omega$', fontsize=14)
    ax.set_ylabel(r'$\phi(\omega)$', fontsize=14)

    fig.savefig('Graphics/Aperiodic link of the first order/ФЧХ')


# АФЧХ
def amplitude_phase_frequency_response():
    w = np.linspace(-180, 0, 100)

    ax.plot(k/(T**2 * w**2 + 1), k*T*w/(T**2 * w**2 + 1))

    ax.set_xlabel(r'$U(\omega)$', fontsize=14)
    ax.set_ylabel(r'$V(\omega)$', fontsize=14)

    fig.savefig('Graphics/Aperiodic link of the first order/АФЧХ')


# ЛАЧХ
def logarithmic_amplitude_frequency_response():

    ax.set(xlim=[-10, 10])
    ax.hlines(20, -10, 10, color='c')
    ax.set_xlabel(r'$\omega$', fontsize=14)
    ax.set_ylabel(r'$L(\omega)$', fontsize=14)

    fig.savefig('Graphics/Aperiodic link of the first order/ЛАЧХ')


# weight_function()
# transition_function()
# phase_frequency_characteristic()
amplitude_phase_frequency_response()
# logarithmic_amplitude_frequency_response()
plt.show()
