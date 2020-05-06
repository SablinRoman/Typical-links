import matplotlib.pyplot as plt
import numpy as np
from math import pi

k = 10
T = 0

fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid()

# Весовая функция
def weight_function():

    ax.set(xlim=[-15, 20])

    ax.hlines(10, -15, 20, colors='c')

    ax.set_xlabel(r'$t$', fontsize=14)
    ax.set_ylabel(r'$W(t)$', fontsize=14)

    fig.savefig('Graphics/Ideal integrating link/Весовая функция')


# Переходная функция
def transition_function():
    ax.set(xlim=[-10, 10])
    ax.set(ylim=[-100, 100])

    x = np.linspace(-10, 10, 40)
    y = k * x
    ax.plot(x, y)

    ax.set_xlabel(r'$t$', fontsize=14)
    ax.set_ylabel(r'$h(t)$', fontsize=14)

    fig.savefig('Graphics/Aperiodic link of the first order/Переходная функция')


# ФЧХ
def phase_frequency_characteristic():
    ax.set(xlim=[-15, 15])

    ax.hlines(pi/2, -15, 15, colors='c')
    ax.set_xlabel(r'$\omega$', fontsize=14)
    ax.set_ylabel(r'$\phi(\omega)$', fontsize=14)

    fig.savefig('Graphics/Aperiodic link of the first order/ФЧХ')


# АФЧХ
def amplitude_phase_frequency_response():
    ax.set(ylim=[-20, 20])
    ax.vlines(0, -20, 20, colors='c')

    ax.set_xlabel(r'$U(\omega)$', fontsize=14)
    ax.set_ylabel(r'$V(\omega)$', fontsize=14)

    fig.savefig('Graphics/Aperiodic link of the first order/АФЧХ')


# ЛАЧХ
def logarithmic_amplitude_frequency_response():

    ax.set(xlim=[0, 10])

    x = np.linspace(0, 10)
    y = np.linspace(20, 0)
    ax.plot(x, y)

    ax.set_xlabel(r'$\omega$', fontsize=14)
    ax.set_ylabel(r'$L(\omega)$', fontsize=14)

    fig.savefig('Graphics/Aperiodic link of the first order/ЛАЧХ')


# weight_function()
# transition_function()
# phase_frequency_characteristic()
# amplitude_phase_frequency_response()
# logarithmic_amplitude_frequency_response()
plt.show()
