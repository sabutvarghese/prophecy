from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from enrich_accounts.config.ConfigStore import *
from enrich_accounts.udfs.UDFs import *

def enriched_accounts(spark: SparkSession, by_id_left_outer: DataFrame):
    by_id_left_outer.write\
        .format("delta")\
        .mode("overwrite")\
        .saveAsTable("`hive_metastore`.`bookstore_eng_pro`.`enriched_accounts_demo2`")
