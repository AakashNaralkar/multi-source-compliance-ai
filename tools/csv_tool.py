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
                    print(f"✅ Loaded: {file} (rows={len(df)})")

                except Exception as e:
                    print(f"❌ Error loading {file}: {e}")

    return csv_data


# ==========================================
# 🔹 SIMPLE QUERY ENGINE (SAFE SEARCH)
# ==========================================
def query_csv(csv_data, query):
    query = query.lower()
    results = []

    for name, df in csv_data.items():
        try:
            df_str = df.astype(str)

            mask = df_str.apply(
                lambda row: row.str.lower().str.contains(query, regex=False).any(),
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
# 🔥 BPSS LOGIC ENGINE (FINAL PERFECT VERSION)
# ==========================================
def check_bpss_status(base_path="dataset/bpss_agentic_dataset/structured"):

    print("🧠 Running BPSS status analysis...")

    csv_data = load_all_csvs(base_path)

    tracker = csv_data.get("bpps_tracker_export.csv")
    docs = csv_data.get("document_inventory.csv")

    if tracker is None or docs is None:
        return ["❌ Required CSV files not found"]

    # Normalize columns
    tracker.columns = tracker.columns.str.lower()
    docs.columns = docs.columns.str.lower()

    results = []

    # ✅ VALID STATUS (REAL LOGIC)
    valid_status = ["clear", "ready to join", "risk accepted"]

    for _, row in tracker.iterrows():

        candidate_id = str(row.get("candidate_id", "")).strip()

        # ==========================================
        # 🔥 SAFE STATUS DETECTION
        # ==========================================
        status = ""
        for col in tracker.columns:
            if "status" in col:
                status = str(row[col]).lower().strip()
                break

        # ==========================================
        # 🔍 GET CANDIDATE DOCUMENTS
        # ==========================================
        candidate_docs = docs[
            docs["candidate_id"].astype(str).str.contains(candidate_id, regex=False)
        ]

        docs_text = candidate_docs.to_string().lower()

        missing = []

        # ==========================================
        # 🔥 SMART DOCUMENT DETECTION
        # ==========================================

        address_keywords = ["address", "utility bill", "bank statement"]
        if not any(word in docs_text for word in address_keywords):
            missing.append("Missing address proof")

        passport_keywords = ["passport", "id", "photo id"]
        if not any(word in docs_text for word in passport_keywords):
            missing.append("Missing passport / ID")

        if candidate_docs.empty:
            missing.append("No documents submitted")

        # ==========================================
        # 🔥 FINAL DECISION (FIXED LOGIC)
        # ==========================================

        if status not in valid_status or missing:

            reason = []

            if missing:
                reason.extend(missing)

            if status not in valid_status:
                reason.append(f"Status = {status.upper()}")

            results.append({
                "candidate_id": candidate_id,
                "status": "❌ NOT READY",
                "reason": reason
            })

    if not results:
        return ["✅ All candidates ready for BPSS closure"]

    return results


# ==========================================
# 🔹 MAIN FUNCTION (AGENT USE)
# ==========================================
def search_csv(query, base_path="dataset/bpss_agentic_dataset/structured"):

    print("📊 Searching structured data...")

    csv_data = load_all_csvs(base_path)

    results = query_csv(csv_data, query)

    if not results:
        return ["No relevant structured data found"]

    return results