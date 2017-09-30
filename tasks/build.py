from invoke import task


@task(default=True)
def build(ctx):
    "Build a bunch of static assets"
    print('Building assets...')


@task
def clean(ctx):
    "Take out the garbage"
    print('Cleaning build directory...')
