import random
import string

import click


@click.command()
@click.option(
    '-t', '--target',
    type=str,
    default='METHINKS IT IS LIKE A WEASEL',
    show_default=True)
@click.option(
    '-p', '--population-size',
    type=int,
    default=100,
    show_default=True)
@click.option(
    '-r', '--mutation-rate',
    type=float,
    default=.05,
    show_default=True)
@click.option(
    '--color/--no-color', 'is_colorized',
    default=True,
    is_flag=True,
    show_default=True,
    help='Tries to use ANSI colors when reporting generation results')
def cli(target, population_size, mutation_rate, is_colorized):
    charset = string.ascii_uppercase + ' '
    best_subject = ''.join(random.choices(charset, k=len(target)))
    generation = 0

    def mutate(subject):
        return ''.join(
            c if random.random() >= mutation_rate
            else random.choice(charset) for c in subject)

    def evaluate(subject):
        return sum(a == b for a, b in zip(subject, target))

    def report(subject):
        click.echo(f'{generation: 6}: ', nl=False)
        styled_subject = ''.join(
            click.style(a, bold=True, fg='green' if a == b else 'red')
            for a, b in zip(subject, target))
        click.echo(styled_subject, color=is_colorized, nl=False)
        score = evaluate(subject)
        click.echo(f' -- {score}/{len(target)}')

    while True:
        population = population_size * [best_subject]
        population = map(mutate, population)
        best_subject = max(population, key=evaluate)
        report(best_subject)
        if best_subject == target:
            return 0
        generation += 1
