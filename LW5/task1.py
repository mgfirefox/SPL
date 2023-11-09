import random

import numpy


def start():
    pass


def calculate_expression(x):
    return (
        numpy.add(
            numpy.divide(
                numpy.add(
                    numpy.sin(
                        numpy.power(
                            numpy.subtract(
                                numpy.divide(
                                    numpy.pi,
                                    8
                                ),
                                1
                            ),
                            2
                        )
                    ),
                    numpy.power(
                        numpy.add(
                            3,
                            numpy.float_power(
                                x,
                                2
                            )
                        ),
                        numpy.divide(
                            1,
                            4
                        )
                    )
                ),
                numpy.subtract(
                    numpy.arcsin(
                        numpy.divide(
                            x,
                            2
                        )
                    ),
                    numpy.multiply(
                        5.236,
                        numpy.float_power(
                            10,
                            -2
                        )
                    )
                )
            ),
            numpy.log(
                numpy.abs(
                    numpy.subtract(
                        3.12,
                        x
                    )
                )
            )
        )
    )


def calculate_regression_equation_estimation():
    x = numpy.array(
        [[1, random.randint(7, 19), random.randint(60, 82)] for _ in range(12)], float)
    y = numpy.random.uniform(13.5, 18.6, (12, 1))

    x_t = x.transpose()
    a = numpy.dot(numpy.linalg.inv(numpy.dot(x_t, x)), numpy.dot(x_t, y))
    calculated_y = numpy.array([a[0] + a[1] * x[i, 1] + a[2] * x[i, 2] for i in range(12)])

    print("X =")
    print(x)
    print("Y =")
    print(y)
    print("A =")
    print(a)
    print("Y' =")
    print(calculated_y)

