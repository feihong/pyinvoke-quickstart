from invoke import task


@task(default=True)
def build(ctx):
    "Build the docs"
    print('Building docs...')


@task
def publish(ctx):
    "Publish the docs for users to read"
    print('Publishing docs...')
