import os
import uuid

import pandas as pd
from django.conf import settings
from ydata_profiling import ProfileReport


def get_html(df: pd.DataFrame) -> str:
    profile = ProfileReport(df, title="Profiling Report", lazy=False)
    unique_id = uuid.uuid4()
    path = os.path.join(settings.MEDIA_ROOT, "reports")
    os.makedirs(path, exist_ok=True)
    namefile = os.path.join(path, f"report_{unique_id}.html")
    profile.to_file(namefile)
    return os.path.join("reports", f"report_{unique_id}.html")
