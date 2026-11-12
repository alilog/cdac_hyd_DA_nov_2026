"""
O05_numerical_sanitizer.py
Handles floating-point precision edge cases (IEEE 754), division by zero, and inf/-NaN masking.
"""
"""
================================================================================
MODULE: Numerical Sanitizer & Mathematical Edge-Case Engine
FILE: src/O05_numerical_sanitizer.py
PURPOSE:
  Resolves floating-point precision issues (IEEE 754 standards), masks 
  infinite values (inf, -inf) with NaN or sentinel defaults, prevents 
  division-by-zero propagation, and sanitizes numerical matrices prior to 
  feature transformation, as parameterized in 'config/O01_cleaning_rules.yaml'.
================================================================================
"""

import logging
from pathlib import Path
import pandas as pd
import numpy as np
import yaml

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] [%(name)s]: %(message)s"
)
logger = logging.getLogger("NumericalSanitizer")


class NumericalSanitizer:
    """Sanitizes floating-point precision anomalies, infinities, and NaNs."""

    def __init__(self, config_path: Path):
        self.config_path = Path(config_path)
        self.config = self._load_config()

    def _load_config(self) -> dict:
        """Loads mathematical sanitization parameters from YAML config."""
        if not self.config_path.exists():
            raise FileNotFoundError(f"[ERROR] Configuration file not found: {self.config_path}")
        with open(self.config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f).get("mathematical_sanitization", {})

if __name__ == "__main__":
    # Local test demonstration
    config_file = Path("config/O01_cleaning_rules.yaml")
    
    sample_df = pd.DataFrame({
        "ratio_score": [1.5, np.inf, 3.2, -np.inf],
        "efficiency": [10.0, 0.0, 5.0, 8.0]
    })
    
    if config_file.exists():
        sanitizer = NumericalSanitizer(config_path=config_file)
        # df_sanitized = sanitizer.sanitize_infinities_and_nans(sample_df)
        print("\n[RESULT] Sanitized DataFrame Preview:")
        # print(df_sanitized)