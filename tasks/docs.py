from invoke import task


@task(default=True)
def build(ctx):
    print('Building docs...')


@task
def publish(ctx):
    print('Publishing docs...')
