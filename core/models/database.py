# By separating the database from the application, we can easily change the database without affecting the application.
# Also, by separating the database code from views, we can make different versions of the views could use a same db functions.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float, Text
from sqlalchemy.orm import relationship, backref
