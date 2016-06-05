# -*- coding: utf-8 -*-
import os
import logging

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
from flask.ext.debugtoolbar import DebugToolbarExtension
# from hamlpy.nodes import TagNode
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required, current_user
from config.application import AVAILABLE_CONFIGS
from config.assets import assets

from wtforms import validators

import flask_admin
from flask_admin.contrib import sqla
from flask_admin.contrib.sqla import filters
#import admin
#from flask_admin import helpers as admin_helpers

db = SQLAlchemy()
migrate = Migrate()
toolbar = DebugToolbarExtension()

"""# Create models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    # Required for administrative interface. For python 3 please use __str__ instead.
    def __unicode__(self):
        return self.username


# Create M2M table
post_tags_table = db.Table('post_tags', db.Model.metadata,
                           db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                           db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                           )


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime)

    user_id = db.Column(db.Integer(), db.ForeignKey(User.id))
    user = db.relationship(User, backref='posts')

    tags = db.relationship('Tag', secondary=post_tags_table)

    def __unicode__(self):
        return self.title


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(64))

    def __unicode__(self):
        return self.name


class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    key = db.Column(db.String(64), nullable=False)
    value = db.Column(db.String(64))

    user_id = db.Column(db.Integer(), db.ForeignKey(User.id))
    user = db.relationship(User, backref='info')

    def __unicode__(self):
        return '%s - %s' % (self.key, self.value)


class Tree(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    parent_id = db.Column(db.Integer, db.ForeignKey('tree.id'))
    parent = db.relationship('Tree', remote_side=[id], backref='children')

    def __unicode__(self):
        return self.name
"""
"""
def build_sample_db():

    #Populate a small db with some example entries.


    import random
    import datetime

    db.drop_all()
    db.create_all()

    # Create sample Users
    first_names = [
        'Harry', 'Amelia', 'Oliver', 'Jack', 'Isabella', 'Charlie', 'Sophie', 'Mia',
        'Jacob', 'Thomas', 'Emily', 'Lily', 'Ava', 'Isla', 'Alfie', 'Olivia', 'Jessica',
        'Riley', 'William', 'James', 'Geoffrey', 'Lisa', 'Benjamin', 'Stacey', 'Lucy'
    ]
    last_names = [
        'Brown', 'Smith', 'Patel', 'Jones', 'Williams', 'Johnson', 'Taylor', 'Thomas',
        'Roberts', 'Khan', 'Lewis', 'Jackson', 'Clarke', 'James', 'Phillips', 'Wilson',
        'Ali', 'Mason', 'Mitchell', 'Rose', 'Davis', 'Davies', 'Rodriguez', 'Cox', 'Alexander'
    ]

    user_list = []
    for i in range(len(first_names)):
        user = User()
        user.first_name = first_names[i]
        user.username = first_names[i].lower()
        user.last_name = last_names[i]
        user.email = user.username + "@example.com"
        user_list.append(user)
        db.session.add(user)

    # Create sample Tags
    tag_list = []
    for tmp in ["YELLOW", "WHITE", "BLUE", "GREEN", "RED", "BLACK", "BROWN", "PURPLE", "ORANGE"]:
        tag = Tag()
        tag.name = tmp
        tag_list.append(tag)
        db.session.add(tag)

    # Create sample Posts
    sample_text = [
        {
            'title': "de Finibus Bonorum et Malorum - Part I",
            'content': "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor \
                        incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud \
                        exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure \
                        dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. \
                        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt \
                        mollit anim id est laborum."
        },
        {
            'title': "de Finibus Bonorum et Malorum - Part II",
            'content': "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque \
                        laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto \
                        beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur \
                        aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi \
                        nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, \
                        adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam \
                        aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam \
                        corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum \
                        iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum \
                        qui dolorem eum fugiat quo voluptas nulla pariatur?"
        },
        {
            'title': "de Finibus Bonorum et Malorum - Part III",
            'content': "At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium \
                        voluptatum deleniti atque corrupti quos dolores et quas molestias excepturi sint occaecati \
                        cupiditate non provident, similique sunt in culpa qui officia deserunt mollitia animi, id \
                        est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio. Nam \
                        libero tempore, cum soluta nobis est eligendi optio cumque nihil impedit quo minus id quod \
                        maxime placeat facere possimus, omnis voluptas assumenda est, omnis dolor repellendus. \
                        Temporibus autem quibusdam et aut officiis debitis aut rerum necessitatibus saepe eveniet \
                        ut et voluptates repudiandae sint et molestiae non recusandae. Itaque earum rerum hic tenetur \
                        a sapiente delectus, ut aut reiciendis voluptatibus maiores alias consequatur aut perferendis \
                        doloribus asperiores repellat."
        }
    ]

    for user in user_list:
        entry = random.choice(sample_text)  # select text at random
        post = Post()
        post.user = user
        post.title = entry['title']
        post.text = entry['content']
        tmp = int(1000*random.random())  # random number between 0 and 1000:
        post.date = datetime.datetime.now() - datetime.timedelta(days=tmp)
        post.tags = random.sample(tag_list, 2)  # select a couple of tags at random
        db.session.add(post)

    # Create a sample Tree structure
    trunk = Tree(name="Trunk")
    db.session.add(trunk)
    for i in range(5):
        branch = Tree()
        branch.name = "Branch " + str(i+1)
        branch.parent = trunk
        db.session.add(branch)
        for j in range(5):
            leaf = Tree()
            leaf.name = "Leaf " + str(j+1)
            leaf.parent = branch
            db.session.add(leaf)

    db.session.commit()
    return
"""
"""if __name__ == '__main__':
    # Build a sample db on the fly, if one does not exist yet.
    app_dir = op.realpath(os.path.dirname(__file__))
    database_path = op.join(app_dir, app.config['DATABASE_FILE'])
    if not os.path.exists(database_path):
        build_sample_db()

    # Start app
    app.run(debug=True)"""

"""
# Customized User model admin
class UserAdmin(sqla.ModelView):
    inline_models = (UserInfo,)


# Customized Post model admin
class PostAdmin(sqla.ModelView):
    # Visible columns in the list view
    column_exclude_list = ['text']

    # List of columns that can be sorted. For 'user' column, use User.username as
    # a column.
    column_sortable_list = ('title', ('user', 'user.username'), 'date')

    # Rename 'title' columns to 'Post Title' in list view
    column_labels = dict(title='Post Title')

    column_searchable_list = ('title', User.username, 'tags.name')

    column_filters = ('user',
                      'title',
                      'date',
                      'tags',
                      filters.FilterLike(Post.title, 'Fixed Title', options=(('test1', 'Test 1'), ('test2', 'Test 2'))))

    # Pass arguments to WTForms. In this case, change label for text field to
    # be 'Big Text' and add required() validator.
    form_args = dict(
                    text=dict(label='Big Text', validators=[validators.required()])
                )

    form_ajax_refs = {
        'user': {
            'fields': (User.username, User.email)
        },
        'tags': {
            'fields': (Tag.name,)
        }
    }

    def __init__(self, session):
        # Just call parent class with predefined model.
        super(PostAdmin, self).__init__(Post, session)


class TreeView(sqla.ModelView):
    form_excluded_columns = ['children', ]
"""


def create_app(config):
    instance_path = os.path.abspath(
        os.path.join(
            os.path.dirname(os.path.dirname(__file__)), 'config', 'instance'
        )
    )
    app = Flask(
        __name__, instance_path=instance_path, instance_relative_config=True
    )
    # Create admin
    #admin = flask_admin.Admin(app, name='Example: SQLAlchemy', template_mode='bootstrap3')
    #app.config['SECRET_KEY'] = '123456790'
    # Add views
    #admin.add_view(UserAdmin(User, db.session))
    #admin.add_view(sqla.ModelView(Tag, db.session))
    #admin.add_view(PostAdmin(db.session))
    #admin.add_view(TreeView(Tree, db.session))
    app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False
    configure_app(app, config)
    configure_extensions(app, db)
    configure_logging(app)
    configure_hooks(app)
    configure_template_filters(app)
    configure_template_globals(app)
    configure_error_handlers(app)
    configure_blueprints(app)
    return app



"""@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
    )"""

def configure_app(app, config):
    app.config.from_object(AVAILABLE_CONFIGS[config])
    app.config.from_pyfile('application_instance.py', silent=True)


def configure_extensions(app, db):
    db.init_app(app)
    migrate.init_app(app, db, directory=os.path.join('db', 'migrations'))
    toolbar.init_app(app)
    assets.init_app(app)

    # app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
    # app.jinja_env.pyjade.options['autocloseCode'] = ['assets']

    # app.jinja_env.add_extension('hamlpy.ext.HamlPyExtension')
    # TagNode.self_closing['assets'] = 'endassets'


def configure_logging(app):
    app.logger.setLevel(logging.INFO)


def configure_hooks(app):
    # @app.before_request
    # def before_request():
    #     pass
    pass


def configure_template_filters(app):
    # @app.template_filter()
    # def reverse_filter(s):
    #     return s[::-1]
    #
    # app.jinja_env.filters['imported_filter'] = imported_filter
    pass


def configure_template_globals(app):
    # @app.template_global()
    # def prepare_url(**kwargs):
    #     args = request.args.to_dict()
    #     args.update(kwargs)
    #     return url_for(request.endpoint, **args)
    #
    # app.add_template_global(pformat)
    pass


def configure_error_handlers(app):
    @app.errorhandler(403)
    def forbidden(error):
        return render_template("403.html"), 403

    @app.errorhandler(404)
    def not_found(error):
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template("500.html"), 500


def configure_blueprints(app):
    from .views import welcome_view
    app.register_blueprint(welcome_view.mod)
    from .views import student_view
    app.register_blueprint(student_view.mod)
    #from .views import admin_view
    #app.register_blueprint(admin_view.mod)
    from .views import admin230695_view
    app.register_blueprint(admin230695_view.mod)
