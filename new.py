@click.group()
def main(add argument):
"""
Docstring where information about your CLI application will go
"""

@main.command()
def listsources(ctx, sources):
"""
Enter your choice from the source list
"""
  pass
@main.command()
def topheadlines():
"""
Get a list of top 10 headlines from the sources
"""
  pass