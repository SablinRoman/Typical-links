import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
ax.grid()


# Весовая функция--
def weight_function():

    # ax.set(xlim=[-3, 10])
    # ax.set(ylim=[0, 80])

    x = np.linspace(0, 800, 800)
    y = (166.7 * np.exp(-12.5 / x) - 166.7 * np.exp(-50 / x))
    ax.plot(x/1000, y)

    ax.set_xlabel(r'$t$', fontsize=14)
    ax.set_ylabel(r'$W(t)$', fontsize=14)

    fig.savefig('Graphics/Aperiodic link of the second order/Весовая функция')


# Переходная функция--
def transition_function():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid()
    ax.set(xlim=[0, 2])

    x = np.linspace(0, 5, 100)
    y = k * (1 - np.exp(-x / T))
    ax.plot(x, y)

    ax.set_xlabel(r'$t$', fontsize=14)
    ax.set_ylabel(r'$h(t)$', fontsize=14)

    fig.savefig('Graphics/Aperiodic link of the second order/Переходная функция')


# ФЧХ
def phase_frequency_characteristic():
    # ax.set(xlim=[0, 150])

    w = np.linspace(0, 300, 1000)
    y = y = 10 / (np.sqrt((1 - 0.0016**2 * w**2)**2) + 0.1**2 * w**2)
    ax.plot(w, y)

    ax.set_xlabel(r'$\omega$', fontsize=14)
    ax.set_ylabel(r'$\phi(\omega)$', fontsize=14)

    fig.savefig('Graphics/Aperiodic link of the second order/ФЧХ')


# АФЧХ
def amplitude_phase_frequency_response():
    w = np.linspace(-300, 300, 1000)
    y = y = 10 / (np.sqrt(((1 - 0.0016 ** 2 * w ** 2) ** 2) + 0.1 ** 2 * w ** 2))
    ax.plot(w, y)

    ax.set_xlabel(r'$U(\omega)$', fontsize=14)
    ax.set_ylabel(r'$V(\omega)$', fontsize=14)

    fig.savefig('Graphics/Aperiodic link of the second order/АФЧХ')


# ЛАЧХ
def logarithmic_amplitude_frequency_response():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid()
    ax.set(xlim=[0, 40])

    w = np.linspace(0, 50, 100)
    ax.plot(w, 20 * np.log10(k) - 20 * np.log10(np.sqrt(1 + T ** 2 * w ** 2)), color='c')

    ax.set_xlabel(r'$\omega$', fontsize=14)
    ax.set_ylabel(r'$L(\omega)$', fontsize=14)

    fig.savefig('Graphics/Aperiodic link of the second order/ЛАЧХ')


# weight_function()
# transition_function()
# phase_frequency_characteristic()
amplitude_phase_frequency_response()
# logarithmic_amplitude_frequency_response()
plt.show()
