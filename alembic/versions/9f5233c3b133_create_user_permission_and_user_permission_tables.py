"""create user, permission and user_permission tables

Revision ID: 9f5233c3b133
Revises: 
Create Date: 2023-03-13 22:19:24.722956

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = '9f5233c3b133'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
        CREATE TABLE "user"(
            id SERIAL PRIMARY KEY,
            email VARCHAR(50) UNIQUE NOT NULL,
            password VARCHAR(256) NOT NULL,
            name VARCHAR(100) NOT NULL,
            created_at DATE DEFAULT NOW(),
            updated_at DATE DEFAULT NOW(),
            created_by VARCHAR(50) NOT NULL,
            enabled BOOLEAN DEFAULT TRUE
        );

        CREATE INDEX user_email_index ON "user"(email);

        CREATE TABLE permission(
            id SERIAL PRIMARY KEY,
            key VARCHAR(30) UNIQUE
        );
        
        CREATE INDEX permission_key_index ON permission(key);
        
        CREATE TABLE user_permission(
            id SERIAL PRIMARY KEY,
            user_id BIGINT,
            permission_id INTEGER,
            
            UNIQUE (user_id, permission_id),
            CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES "user"(id),
            CONSTRAINT fk_permission_id FOREIGN KEY (permission_id) REFERENCES permission(id)
        );
    """)


def downgrade() -> None:
    op.execute("""
        DROP TABLE user_permission;
        
        DROP TABLE permission;
        
        DROP TABLE "user";
    """)