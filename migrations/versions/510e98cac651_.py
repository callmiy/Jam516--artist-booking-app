"""empty message

Revision ID: 510e98cac651
Revises: d778d9f77c75
Create Date: 2020-05-17 17:12:16.538857

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '510e98cac651'
down_revision = 'd778d9f77c75'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Show', sa.Column('artist_id', sa.Integer(), nullable=True))
    op.add_column('Show', sa.Column('start_time', sa.DateTime(), nullable=True))
    op.add_column('Show', sa.Column('venue_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'Show', 'Artist', ['artist_id'], ['id'])
    op.create_foreign_key(None, 'Show', 'Venue', ['venue_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.drop_constraint(None, 'Show', type_='foreignkey')
    op.drop_column('Show', 'venue_id')
    op.drop_column('Show', 'start_time')
    op.drop_column('Show', 'artist_id')
    # ### end Alembic commands ###