from loaders.data_loader import load_all_data

docs = load_all_data("dataset/bpss_agentic_dataset")

print(len(docs))
print(docs[0])