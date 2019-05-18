"""empty message

Revision ID: 42336e1d295b
Revises: 
Create Date: 2019-05-17 00:05:13.621579

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '42336e1d295b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=False),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=False)
    op.drop_index('filehash', table_name='pastefile')
    op.drop_table('pastefile')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pastefile',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('filename', mysql.VARCHAR(length=5000), nullable=False),
    sa.Column('filehash', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('filemd5', mysql.VARCHAR(length=128), nullable=False),
    sa.Column('uploadtime', mysql.DATETIME(), nullable=False),
    sa.Column('mimetype', mysql.VARCHAR(length=256), nullable=False),
    sa.Column('size', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_index('filehash', 'pastefile', ['filehash'], unique=True)
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
