""" 
    ridaakh.__main__

    Alias for ridaakh.run for the command line.

"""

if __name__ == '__main__':
    from .cli import main
    main(as_module=True)
