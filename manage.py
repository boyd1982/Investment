import os
from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand
from webapp import create_app
from webapp.models import db, roles,users

#test git tools
env = os.environ.get('WEBAPP_ENV','dev')
app = create_app('webapp.config.%sConfig' % env.capitalize())
#app = create_stockapp('webapp.config.%sConfig' % env.capitalize())
manager = Manager(app)
manager.add_command("server",Server())
@manager.shell
def make_shell_context():
    return dict(app=app,db=db,users=users,roles=roles)
if __name__=="__main__":
    manager.run()
