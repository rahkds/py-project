from types import MappingProxyType
from app.validators.env_validator import EnvSchema
import os
 
app_config = MappingProxyType(EnvSchema().load(os.environ, unknown='exclude'))