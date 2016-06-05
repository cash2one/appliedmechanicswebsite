from flask import Blueprint, render_template
from app.models import Alumni, Department
from random import randint
#from app import admin

mod = Blueprint(
    'admin', __name__, url_prefix='/admin'
)


@mod.route('/')
def index():
    return render_template('admin/index.html')
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
