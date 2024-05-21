import uuid

import pandas as pd
from ydata_profiling import ProfileReport


def get_html(df: pd.DataFrame) -> str:
    profile = ProfileReport(df, title="Profiling Report")
    unique_id = uuid.uuid4()
    namefile = f"media/report_{unique_id}.html"
    profile.to_file(namefile)
    return namefile
