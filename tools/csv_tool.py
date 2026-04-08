import pandas as pd
import os


# ==========================================
# 🔹 LOAD ALL CSV FILES INTO MEMORY
# ==========================================
def load_all_csvs(folder_path):
    csv_data = {}

    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(".csv"):
                file_path = os.path.join(root, file)

                try:
                    df = pd.read_csv(file_path)
                    csv_data[file] = df
                    print(f"✅ Loaded: {file}")

                except Exception as e:
                    print(f"❌ Error loading {file}: {e}")

    return csv_data


# ==========================================
# 🔹 SIMPLE QUERY ENGINE
# ==========================================
def query_csv(csv_data, query):
    query = query.lower()

    results = []

    for name, df in csv_data.items():

        try:
            # Convert everything to string for search
            df_str = df.astype(str)

            # 🔍 Row-wise search
            mask = df_str.apply(
                lambda row: row.str.lower().str.contains(query).any(),
                axis=1
            )

            matched = df[mask]

            if not matched.empty:
                results.append({
                    "file": name,
                    "rows": matched.head(5).to_dict(orient="records")
                })

        except Exception as e:
            print(f"❌ Error querying {name}: {e}")

    return results


# ==========================================
# 🔹 MAIN FUNCTION (TO BE USED BY AGENT)
# ==========================================
def search_csv(query, base_path="dataset/bpss_agentic_dataset/structured"):

    print("📊 Searching structured data...")

    csv_data = load_all_csvs(base_path)

    results = query_csv(csv_data, query)

    if not results:
        return ["No relevant structured data found"]

    return results