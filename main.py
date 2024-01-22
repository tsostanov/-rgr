import argparse
import math

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
import cmath
import matplotlib

def setup():
    fig = plt.figure()
    fig, (ax_virtual, ax_physical) = plt.subplots(
            nrows = 1,
            ncols = 2,
            figsize=(12,6),
            )


    ax_virtual.set_title("Виртуальное пространство")
    ax_virtual.set_xlabel(r"$u$")
    ax_virtual.set_ylabel(r"$v$")
    ax_virtual.spines['top'].set_visible(False);
    ax_virtual.spines['right'].set_visible(False);
    ax_virtual.set_aspect('equal', 'box')
    z1 = 1 + cmath.sqrt(1 + 1j)
    z2 = 1 - cmath.sqrt(1 + 1j)
    ax_virtual.scatter([z1.real, z2.real], [0, 0], color='red', s=40, marker='o',
                       label=r'выколотые точки $z = 1 \pm \sqrt{1 + i}$')
    ax_virtual.grid()
    ax_virtual.legend(loc='lower left')

    ax_physical.set_title("Физическое пространство")
    ax_physical.set_xlabel(r"$x$")
    ax_physical.set_ylabel(r"$y$")
    ax_physical.spines['top'].set_visible(False);
    ax_physical.spines['right'].set_visible(False);
    ax_physical.set_aspect('equal', 'box')
    # ax_physical.scatter(0, 0, color='red', s=40, marker='o', label=r'выколотая точка $z = 0$')
    ax_physical.scatter(-1, 0, color='red', s=40, marker='o', label=r'выколотая точка $z = -1$')
    ax_physical.grid()
    ax_physical.legend(loc='upper right')

    return fig, (ax_virtual, ax_physical)


def w(z: complex):
    return (1j + z) / (1j - z)


# def main():
#     fig, (ax_virtual, ax_physical) = setup()
#     ax_virtual.set_aspect('auto')
#     ax_physical.set_aspect('auto')
#
#
#     c_array = [0, 0.5, 1]
#     colors = plt.get_cmap("twilight")
#
#     sampling_rate = 10_000
#
#     def plot_complex(ax, numbers, color):
#         x = [z.real for z in numbers]
#         y = [z.imag for z in numbers]
#
#         ax.plot(x, y, color=color)
#
#     u_lim = 10
#
#     def draw_horizontal_line(c, cntolor):
#         u_virtual = np.linspace(-u_lim, u_lim, sampling_rate)
#         v_virtual = np.array([c] * len(u_virtual))
#         virtual = np.array([ complex(u_virtual[i], v_virtual[i]) for i in range(len(u_virtual)) ])
#         w_virtual = np.array([w(complex(u_virtual[i], v_virtual[i])) for i in range(len(u_virtual))])
#
#         plot_complex(ax_virtual, virtual, color)
#         plot_complex(ax_physical, w_virtual, color)
#
#     def draw_vertical_line(c, color):
#         v_virtual = np.linspace(-u_lim, u_lim, sampling_rate)
#         u_virtual = np.array([c] * len(v_virtual))
#         virtual = np.array([ complex(u_virtual[i], v_virtual[i]) for i in range(len(u_virtual))])
#         w_virtual = np.array([ w(complex(u_virtual[i], v_virtual[i])) for i in range(len(u_virtual))])
#
#         plot_complex(ax_virtual, virtual, color)
#         plot_complex(ax_physical, w_virtual, color)
#
#     x_center = 0
#     y_center = 0
#     for i in range(len(c_array)):
#         c = c_array[i]
#         color = colors(i / len(c_array) )
#         draw_vertical_line(x_center + c, color)
#         draw_horizontal_line(y_center + c, color)
#         if c > 0:
#             draw_vertical_line(x_center - c, color)
#             draw_horizontal_line (y_center - c, color)
#     # особые точки
#     draw_vertical_line(cmath.pi / 2, colors(0.88))
#     draw_vertical_line(- cmath.pi / 2, colors(0.88))
#
#
#
#     ax_virtual.set_xlim([-4, 4])
#     ax_virtual.set_ylim([-np.max(c_array) - 2, np.max(c_array) + 2])
#
#     ax_physical.set_xlim([-5, 5])
#     ax_physical.set_ylim([-5, 5])
#
#     plt.legend()
#
#
#     plt.savefig('resulter.png')
#
#

def main():
    fig, (ax_virtual, ax_physical) = setup()
    sampling_rate = 100_000

    def plot_complex(ax, numbers):
        x = [z.real for z in numbers]
        y = [z.imag for z in numbers]

        ax.plot(x, y)

    for r in [0.7, np.sqrt(2), np.sqrt(3), np.sqrt(5), np.pi / 2]:
      u_virtual_1 = np.linspace(-r, r, sampling_rate)
      v_virtual_1 = np.sqrt(r**2 - u_virtual_1 ** 2)
      u_virtual_2 = np.array(u_virtual_1[::-1])
      v_virtual_2 = -np.sqrt(r**2 - u_virtual_2 ** 2)
      u_virtual = np.concatenate([u_virtual_1, u_virtual_2])
      v_virtual = np.concatenate([v_virtual_1, v_virtual_2])
      virtual_numbers = np.array([complex(u_virtual[i], v_virtual[i]) for i in range(len(u_virtual))])
      w_numbers = np.array([w(complex(u_virtual[i], v_virtual[i])) for i in range(len(u_virtual))])
      plot_complex(ax_virtual, virtual_numbers)
      plot_complex(ax_physical, w_numbers)


    plt.savefig('resulter.png')


if __name__ == '__main__':
    main()


