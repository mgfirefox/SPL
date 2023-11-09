import numpy
import pylab
from matplotlib import pyplot


def start1():
    cs = numpy.arange(-10, 1.1, 0.25, dtype=float)
    x = 3.67
    ls = numpy.array([calculate_l(x, c) for c in cs])
    max_l = numpy.max(ls)
    average_l = numpy.average(ls)

    print("-10 ≤ с ≤ -1, 𝚫c = 0.25")
    print(f"x = {x}")
    print("l =")
    print(ls)
    print()

    print(f"Максимальное значение l: {max_l}")
    print(f"Минимальное значение l: {numpy.min(ls)}")
    print(f"Среднее значение l: {average_l}")
    print(f"Количество значений l: {numpy.size(ls)}")
    print()
    print("Отсортированный по возрастанию l =")
    print(numpy.sort(ls))

    figure, ax = pyplot.subplots()

    ax.axvline(x=0, color="black")
    ax.axhline(y=0, color="black")
    ax.set_xlabel("c")
    ax.set_ylabel("l")

    pyplot.scatter(0, numpy.floor(max_l) + 1, marker="^", color="black", label="y")
    pyplot.scatter(numpy.max(cs) + 1, 0, marker=">", color="black", label="x")

    pyplot.grid(True, which="both")
    pyplot.xticks(range(-10, 3))

    lines = ax.plot(cs, ls, cs, [average_l for _ in range(len(cs))])

    pyplot.setp(lines, linewidth=2.)
    pyplot.setp(lines[0], color="blue")
    pyplot.setp(lines[1], color="green")

    pyplot.scatter((cs[0], cs[-1]), (ls[0], ls[-1]), color="blue")
    pyplot.scatter((cs[0], cs[-1]), (average_l, average_l), color="green")

    pyplot.show()


def calculate_l(x, c):
    return (
        numpy.add(
            numpy.float_power(
                numpy.abs(
                    numpy.subtract(
                        numpy.multiply(
                            2,
                            x
                        ),
                        c
                    )
                ),
                numpy.divide(
                    3,
                    5
                )
            ),
            0.567
        )
    )


def start2():
    xs = numpy.array([range(0, 10)])
    ys = numpy.array([range(0, 10)])
    xs, ys = pylab.meshgrid(xs, ys)

    zs = calculate_z(xs, ys)
    zs1 = calculate_z1(xs, ys)
    zs2 = calculate_z2(xs, ys)
    zs3 = calculate_z3(xs, ys)
    zs4 = calculate_z4(xs, ys)

    ax = pyplot.figure().add_subplot(projection="3d")
    ax.plot_surface(xs, ys, zs, color="blue")

    ax = pyplot.figure().add_subplot(projection="3d")
    ax.plot_surface(xs, ys, zs1, color="green")

    ax = pyplot.figure().add_subplot(projection="3d")
    ax.plot_surface(xs, ys, zs2, color="yellow")

    ax = pyplot.figure().add_subplot(projection="3d")
    ax.plot_surface(xs, ys, zs3, color="red")

    ax = pyplot.figure().add_subplot(projection="3d")
    ax.plot_surface(xs, ys, zs4, color="white")

    pyplot.show()


def calculate_z(x,  y):
    return (
        numpy.add(
            numpy.float_power(
                x,
                numpy.divide(
                    1,
                    4
                )
            ),
            numpy.float_power(
                y,
                numpy.divide(
                    1,
                    4
                )
            )
        )
    )


def calculate_z1(x,  y):
    return (
        numpy.subtract(
            numpy.float_power(
                x,
                2
            ),
            numpy.float_power(
                y,
                2
            )
        )
    )


def calculate_z2(x,  y):
    return (
        numpy.add(
            numpy.multiply(
                2,
                x
            ),
            numpy.multiply(
                3,
                y
            )
        )
    )


def calculate_z3(x,  y):
    return (
        numpy.add(
            numpy.float_power(
                x,
                2
            ),
            numpy.float_power(
                y,
                2
            )
        )
    )


def calculate_z4(x,  y):
    return (
        numpy.subtract(
            numpy.multiply(
                numpy.add(
                    1,
                    numpy.add(
                        x,
                        y
                    )
                ),
                2
            ),
            calculate_z3(x, y)
        )
    )
