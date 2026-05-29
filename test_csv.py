import pandas as pd

data = {
    "name": ["test"],
    "value": [123]
}

df = pd.DataFrame(data)

df.to_csv("app/evals/evaluation_results.csv", index=False)

print("CSV created successfully")