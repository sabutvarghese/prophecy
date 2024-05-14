from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from enrich_accounts.config.ConfigStore import *
from enrich_accounts.udfs.UDFs import *

def AggByAccount(spark: SparkSession, select_fields: DataFrame) -> DataFrame:
    df1 = select_fields.groupBy(col("AccountId"))

    return df1.agg(
        count(lit(1)).alias("NumOpportunities"), 
        sum(col("Amount")).alias("Amount"), 
        sum(col("ExpectedRevenue")).alias("ExpectedRevenue"), 
        max(col("CloseQtr")).alias("LastCloseQtr")
    )
