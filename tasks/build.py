from invoke import task


@task(default=True)
def build(ctx):
    print('Building assets...')


@task
def clean(ctx):
    print('Cleaning build directory...')
