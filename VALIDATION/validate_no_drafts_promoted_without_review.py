#!/usr/bin/env python3
"""Lightweight validator for project-control draft promotion records.

Usage:
  python validate_no_drafts_promoted_without_review.py /path/to/project-control
"""
from pathlib import Path
import sys
pc = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
promo = pc/'REGISTRIES/PROMOTION_REGISTRY.md'
if not promo.exists():
    print('No PROMOTION_REGISTRY.md found; nothing to validate.')
    sys.exit(0)
text = promo.read_text(encoding='utf-8', errors='ignore').lower()
if 'promoted' in text and 'approval' not in text:
    print('Warning: promotion registry mentions promoted items but no approval column/text was found.')
    sys.exit(2)
print('Draft promotion review validation passed or no promotions found.')
