"""empty message

Revision ID: fc58019bd853
Revises: af019111fe6c
Create Date: 2019-07-15 13:04:21.634800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fc58019bd853'
down_revision = 'af019111fe6c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bucketlists', sa.Column('CommandID', sa.String(length=255), nullable=True))
    op.add_column('bucketlists', sa.Column('billrefnumber', sa.String(length=255), nullable=True))
    op.add_column('bucketlists', sa.Column('msisdn', sa.Integer(), nullable=True))
    op.add_column('bucketlists', sa.Column('refno', sa.String(length=255), nullable=True))
    op.add_column('bucketlists', sa.Column('shortcode', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('bucketlists', 'shortcode')
    op.drop_column('bucketlists', 'refno')
    op.drop_column('bucketlists', 'msisdn')
    op.drop_column('bucketlists', 'billrefnumber')
    op.drop_column('bucketlists', 'CommandID')
    # ### end Alembic commands ###
