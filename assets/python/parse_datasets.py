"""
This file is used to parse the data used in ILAMB analysis and generate html code for
the website. Note that it assumes that the data is local on the system where it is run
and the environment variable ILAMB_ROOT.
"""
import os
import site

import pandas as pd


def parse_ilamb_configure_file(filename):
    """Configure parsing for ILAMB configure files."""
    lines = open(filename, encoding="utf-8").readlines()
    col_h1 = []
    col_h2 = []
    col_ds = []
    col_src = []
    cur_v = []
    cur_h1 = cur_h2 = cur_ds = None
    for line in lines:
        line = line.strip()
        if line.startswith("[h1:"):
            cur_h1 = line.strip("[h1:").strip("]").strip()
        elif line.startswith("[h2:"):
            cur_h2 = line.strip("[h2:").strip("]").strip()
        elif line.startswith("["):
            cur_ds = line.strip("[").strip("]").strip()
        elif "=" in line:
            key, val = line.split("=")
            key = key.strip()
            val = val.strip()
            if key.startswith("variable"):
                cur_v = [val.strip().strip('"').strip("'")]
            elif key.startswith("alternate_vars"):
                cur_v += [val.strip().strip('"').strip("'")]
            elif key == "source":
                col_h1.append(cur_h1)
                col_h2.append(cur_h2)
                col_ds.append(cur_ds)
                col_src.append(val.strip('"').strip("'"))
    ilamb_df = pd.DataFrame(
        {"Section": col_h1, "Variable": col_h2, "Dataset": col_ds, "Source": col_src}
    )
    return ilamb_df


def ilamb_dataframe_to_html_table(cfg, html_root, dataset_ignores=["Koven"]):
    """Take a dataframe with 'Variable', 'Source', and 'Dataset' and render a
    html table which sorts by Variables."""
    html = """
    <table>"""
    for grp, dfg in cfg.groupby("Variable"):
        html += f"""
      <tr>
        <td>{grp}</td>"""
        row_data = []
        for row, data in dfg.iterrows():
            if data["Dataset"] in dataset_ignores:
                continue
            row_data.append(
                '<a href="%s">%s</a>'
                % (os.path.join(html_root, data["Source"]), data["Dataset"])
            )
        html += "<td>" + ", ".join(row_data) + "</td>"
        html += """
      </tr>"""
    html += """
    </table>"""
    return html


mode = "IOMB"
ilamb_root = os.path.join(os.environ["ILAMB_ROOT"])
ilamb_cfg = os.path.join(site.getsitepackages()[0], f"ILAMB/data/{mode.lower()}.cfg")
ilamb_df = parse_ilamb_configure_file(ilamb_cfg)
ilamb_df.sort_values("Variable")

html = ilamb_dataframe_to_html_table(ilamb_df, f"https://www.ilamb.org/{mode}-Data/")
print(html)
