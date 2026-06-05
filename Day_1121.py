

import pandas as pd

dates = pd.to_datetime([
    "2026-01-01",
    "2026-02-08",
    "2026-03-24",
    "2026-04-21"
])

print(pd.infer_freq(dates))










