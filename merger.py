import nbformat as nbf

def merge_notebooks(filenames):
    merged = nbf.v4.new_notebook()
    for fname in filenames:
        try:
            with open(fname, 'r', encoding='utf-8') as f:
                nb = nbf.read(f, as_version=4)
                merged.cells.extend(nb.cells)
        except FileNotFoundError:
            print(f"File {fname} not found.")
        except Exception as e:
            print(f"An error occurred while reading {fname}: {e}")
    return merged

notebooks_to_merge = ["scraper.ipynb", "preprocess.ipynb", "distributions_outliers.ipynb", "top10.ipynb", "tests.ipynb"]
merged_notebook = merge_notebooks(notebooks_to_merge)

try:
    with open("merged_notebook.ipynb", "w", encoding='utf-8') as f:
        nbf.write(merged_notebook, f)
    print("Notebooks merged successfully into 'merged_notebook.ipynb'.")
except Exception as e:
    print(f"An error occurred while writing the merged notebook: {e}")
