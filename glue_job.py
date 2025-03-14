import os
from pyspark.sql import SparkSession

# Détecter si on est en mode local ou AWS Glue
IS_LOCAL = os.getenv("IS_LOCAL", "true").lower() == "true"

# Initialiser Spark
spark = SparkSession.builder.appName("Test PySpark").getOrCreate()

# Définir les chemins en fonction de l'environnement

# Récupérer les variables d’environnement
IS_LOCAL = os.getenv("IS_LOCAL", "true").lower() == "true"
AWS_S3_BUCKET_INPUT = os.getenv("AWS_S3_BUCKET_INPUT")
AWS_S3_BUCKET_OUTPUT = os.getenv("AWS_S3_BUCKET_OUTPUT")

if IS_LOCAL:
    input_path = "data/data.csv"  # Fichier local
    output_path = "output/"       # Dossier local
else:
    input_path = AWS_S3_BUCKET_INPUT
    output_path = AWS_S3_BUCKET_OUTPUT

def process_data(spark, input_path):
    """Lit un fichier CSV, renomme une colonne et retourne un DataFrame."""
    df = spark.read.csv(input_path, header=True, inferSchema=True,sep=';')
    return df.withColumnRenamed("Username", "full_name")

if __name__ == "__main__":
    print(f"📂 Input Path: {input_path}")
    print(f"📂 Output Path: {output_path}")
    df_transformed = process_data(spark, input_path)
    df_transformed.show()
    df_transformed.write.mode("overwrite").parquet(output_path)
    print("Traitement terminé avec succès!")
    spark.stop()
