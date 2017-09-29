from invoke import task


@task
def download_stuff(ctx):
    print('Downloading stuff...')


@task
def make_widgets(ctx):
    print('Make widgets...')
