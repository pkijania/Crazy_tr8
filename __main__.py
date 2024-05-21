import click
from run_command import run
from simulate_command import simulate

@click.group()
def main():
    """ Crazy_tr8 trading bot for Zonda Crypto"""
    pass

if __name__ == "__main__":
    #Launch "main" method
    try:
        main.add_command(run.run)
        main.add_command(simulate.simulate)
        main()
    except Exception as error:
        print(f"Error!!, program shut down due to {error}")
