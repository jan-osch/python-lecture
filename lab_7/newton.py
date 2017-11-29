#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('func', help='function definition here')
parser.add_argument('-s', '--start', help='start point', type=float, default=-1000)
parser.add_argument('-t', '--step', help='step', type=float, default=0.0)
parser.add_argument('-p', '--precision', help='precision', type=float, default=1e-15)
parser.add_argument('-v', '--verbose', help='increase verbosity', action="store_true")

args = parser.parse_args()


def verbose(*message):
    if args.verbose:
        print(*message)


def derivative(f, x, h):
    return (f(x + h) - f(x - h)) / (2.0 * h)


lam = 'lambda x: ' + args.func
verbose('constructing lambda:', lam)
subject = eval(lam)


def solve(fun, x0, step, precision):
    last_x = x0
    next_x = last_x + step * precision
    while abs(last_x - next_x) > precision:
        new_y = fun(next_x)
        last_x = next_x
        next_x = last_x - new_y / derivative(fun, last_x, precision)
    return next_x


solution = solve(subject, args.start, args.step, args.precision)
print(solution)
