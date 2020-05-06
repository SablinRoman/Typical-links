import matplotlib.pyplot as plt


# Весовая функция
def weight_function():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid()
    ax.set(xlim=[-10, 10])
    ax.hlines(0, -10, 10, color='c')
    ax.set_xlabel(r'$t$', fontsize=14)
    ax.set_ylabel(r'$W(t)$', fontsize=14)

    fig.savefig('Graphics/Inertialess Link/Весовая функция')

# Переходная функция
def transition_function():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid()

    ax.set(xlim=[-10, 10])
    ax.hlines(10, -10, 10, color='c')
    ax.set_xlabel(r'$t$', fontsize=14)
    ax.set_ylabel(r'$h(t)$', fontsize=14)

    fig.savefig('Graphics/Inertialess Link/Переходная функция')

# ФЧХ
def phase_frequency_characteristic():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid()

    ax.set(xlim=[-10, 10])
    ax.hlines(0, -10, 10, color='c')
    ax.set_xlabel(r'$\omega$', fontsize=14)
    ax.set_ylabel(r'$\phi(\omega)$', fontsize=14)

    fig.savefig('Graphics/Inertialess Link/ФЧХ')

# АФЧХ
def amplitude_phase_frequency_response():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid()

    ax.set(xlim=[-5, 30])
    ax.scatter(10, 0)
    ax.set_xlabel(r'$U(\omega)$', fontsize=14)
    ax.set_ylabel(r'$V(\omega)$', fontsize=14)

    fig.savefig('Graphics/Inertialess Link/АФЧХ')

# ЛАЧХ
def logarithmic_amplitude_frequency_response():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.grid()

    ax.set(xlim=[-10, 10])
    ax.hlines(20, -10, 10, color='c')
    ax.set_xlabel(r'$\omega$', fontsize=14)
    ax.set_ylabel(r'$L(\omega)$', fontsize=14)

    fig.savefig('Graphics/Inertialess Link/ЛАЧХ')


# weight_function()

# transition_function()
# phase_frequency_characteristic()
# amplitude_phase_frequency_response()
# logarithmic_amplitude_frequency_response()



