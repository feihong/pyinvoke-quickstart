from invoke import task


@task
def download_stuff(ctx):
    "Download some stuff to your computer"
    print('Downloading stuff...')


@task
def make_widgets(ctx):
    "Make a cool widget, yo"
    print('Make widgets...')
