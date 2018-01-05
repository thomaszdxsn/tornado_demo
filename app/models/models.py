# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, SmallInteger, String, text

from .base import Base

__all__ = ["SysOrganization", 'SysResource', 'SysRole', 'SysRoleResource',
           'SysUser', 'SysUserRole', 'TEvidence', 'TEvidenceBack',
           'TUser', 'UserEvidenceConfig']


class SysOrganization(Base):
    __tablename__ = 'sys_organization'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    parent_id = Column(Integer, index=True)
    country_code = Column(String(50), server_default=text("'0'"))
    credential = Column(String(255))
    credential_name = Column(String(50))
    status_code = Column(SmallInteger, server_default=text("'1'"))
    email = Column(String(255), nullable=False, server_default=text("''"))
    create_time = Column(DateTime)
    update_time = Column(DateTime)


class SysResource(Base):
    __tablename__ = 'sys_resource'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    type = Column(SmallInteger, nullable=False, server_default=text("'1'"))
    url = Column(String(200))
    parent_id = Column(Integer, index=True)
    permission = Column(String(50), server_default=text("'GET'"))
    status_code = Column(SmallInteger, server_default=text("'1'"))
    create_time = Column(DateTime)
    update_time = Column(DateTime)


class SysRole(Base):
    __tablename__ = 'sys_role'

    id = Column(Integer, primary_key=True)
    role = Column(String(100))
    description = Column(String(100))
    status_code = Column(SmallInteger, server_default=text("'1'"))
    create_time = Column(DateTime)
    update_time = Column(DateTime)


class SysRoleResource(Base):
    __tablename__ = 'sys_role_resource'

    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, nullable=False)
    resource_id = Column(Integer, nullable=False)
    create_time = Column(DateTime)
    update_time = Column(DateTime)


class SysUser(Base):
    __tablename__ = 'sys_user'

    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, index=True)
    username = Column(String(100), unique=True)
    password = Column(String(128))
    salt = Column(String(128))
    status_code = Column(SmallInteger, server_default=text("'1'"))
    allow_ips = Column(String(1024))
    is_org_admin = Column(Integer, nullable=False, server_default=text("'0'"))
    evidence_config_id = Column(Integer, nullable=False, server_default=text("'0'"))
    create_time = Column(DateTime)
    update_time = Column(DateTime)


class SysUserRole(Base):
    __tablename__ = 'sys_user_role'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    role_id = Column(Integer, nullable=False)
    create_time = Column(DateTime)
    update_time = Column(DateTime)


class TEvidence(Base):
    __tablename__ = 't_evidence'

    id = Column(Integer, primary_key=True)
    file_md5 = Column(String(50), nullable=False, server_default=text("''"))
    callback = Column(String(255))
    upload_time = Column(DateTime)
    title = Column(String(255))
    remark = Column(String(255))
    file_name = Column(String(255))
    file_size = Column(Integer)
    update_time = Column(DateTime)
    status = Column(Integer, server_default=text("'1'"))
    consumer = Column(String(50))
    evidence_sign = Column(String(100), nullable=False, server_default=text("''"))
    zip_password = Column(String(50), server_default=text("''"))
    file_temp_path = Column(String(255), nullable=False, server_default=text("''"))
    status_code = Column(SmallInteger, server_default=text("'1'"))


class TEvidenceBack(Base):
    __tablename__ = 't_evidence_back'

    id = Column(Integer, primary_key=True)
    file_md5 = Column(String(50), nullable=False, server_default=text("''"))
    callback = Column(String(255))
    upload_time = Column(DateTime)
    title = Column(String(255))
    remark = Column(String(255))
    file_name = Column(String(255))
    file_size = Column(Integer)
    update_time = Column(DateTime)
    status = Column(Integer, server_default=text("'1'"))
    consumer = Column(String(50))
    evidence_sign = Column(String(100), nullable=False, server_default=text("''"))
    zip_password = Column(String(50), server_default=text("''"))
    file_temp_path = Column(String(255), nullable=False, server_default=text("''"))


class TUser(Base):
    __tablename__ = 't_user'

    id = Column(Integer, primary_key=True)
    login_email = Column(String(50), nullable=False, server_default=text("''"))
    password = Column(String(100), nullable=False, server_default=text("''"))
    user_type = Column(Integer, nullable=False, server_default=text("'1'"))
    name = Column(String(255), server_default=text("''"))
    credential_name = Column(String(255), server_default=text("''"))
    credential_code = Column(String(255), server_default=text("''"))
    status_code = Column(Integer, server_default=text("'0'"))
    country_code = Column(String(255))
    allow_ips = Column(String(1024), server_default=text("''"))


class UserEvidenceConfig(Base):
    __tablename__ = 'user_evidence_config'

    id = Column(Integer, primary_key=True)
    evidence_count = Column(Integer, nullable=False, server_default=text("'0'"))
    storage_size = Column(Integer, nullable=False, server_default=text("'0'"))
    storage_used = Column(Integer, nullable=False, server_default=text("'0'"))
    storage_create_time = Column(DateTime)
    expire_time = Column(DateTime)
    create_time = Column(DateTime)
    update_time = Column(DateTime)
