
import polars as pl

def read_csv_sample(file_path, sample_size=100):
  # Read the CSV file using Polars
  df = pl.read_csv(file_path)
  # Extract a sample of the data
  sample = df.head(sample_size)
  return sample

