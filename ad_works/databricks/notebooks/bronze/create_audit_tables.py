# Databricks notebook source
# MAGIC %pip install pyaml pydantic yetl-framework==1.6.4

# COMMAND ----------

dbutils.widgets.text("load_type", "batch")


# COMMAND ----------

from etl import LoadType
from yetl import (
  Config, StageType
)

# COMMAND ----------

param_load_type = dbutils.widgets.get("load_type")

try:
  load_type:LoadType = LoadType(param_load_type)
except Exception as e:
   raise Exception(f"load_type parameter {param_load_type} is not valid")

print(f"""
  load_type: {str(load_type)}
""")

# COMMAND ----------

project = "ad_works"
pipeline = load_type.value

config = Config(
  project=project, 
  pipeline=pipeline
)

# COMMAND ----------

tables = config.tables.create_table(
  stage=StageType.audit_control, 
  first_match=False
)


# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC create database if not exists raw_ad_works

# COMMAND ----------

dbutils.notebook.exit("Success")
