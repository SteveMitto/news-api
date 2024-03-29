from app import create_app
from flask_script import Manager,Server

app= create_app('development')
manager = Manager(app)
manager.add_command('server',Server)
@manager.command
def test():
    """Run the unit tests."""
    import unittest as unit
    tests = unit.TestLoader().discover('test')
    unit.TextTestRunner(verbosity=2).run(test)

if __name__ == "__main__":
    manager.run()
