#!/usr/bin/env python3
"""
Combine paired TSV files from the exports folder.
Removes model comparison prefix, extracts year-page, and merges -1 and -2 files.
"""

import os
import re
from pathlib import Path
from collections import defaultdict

# Configuration
EXPORTS_DIR = Path("exports")
OUTPUT_DIR = Path("rosenwald-benchmark")
PREFIX_LENGTH = 92  # Length of model comparison prefix to skip

def extract_year_page(filename):
    """Extract year and page number from filename after removing prefix."""
    # Remove prefix
    without_prefix = filename[PREFIX_LENGTH:]
    
    # Extract year-page pattern (e.g., 1887-0029)
    match = re.match(r'(\d{4}-\d{4})', without_prefix)
    if match:
        return match.group(1)
    return None

def combine_files():
    """Combine paired -1 and -2 files into single files."""
    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True)
    
    # Group files by year-page
    file_groups = defaultdict(list)
    
    # Scan all TSV files
    for filepath in sorted(EXPORTS_DIR.glob("*.tsv")):
        filename = filepath.name
        year_page = extract_year_page(filename)
        
        if year_page:
            file_groups[year_page].append(filepath)
    
    # Process each group
    stats = {
        'processed': 0,
        'skipped': 0,
        'total_lines': 0
    }
    
    for year_page, files in sorted(file_groups.items()):
        if len(files) != 2:
            print(f"⚠️  Warning: Expected 2 files for {year_page}, found {len(files)}")
            stats['skipped'] += 1
            continue
        
        # Sort to ensure -1 comes before -2
        files.sort()
        
        output_file = OUTPUT_DIR / f"{year_page}.tsv"
        
        # Combine files
        lines_written = 0
        with open(output_file, 'w', encoding='utf-8') as out_f:
            # Write first file completely
            with open(files[0], 'r', encoding='utf-8') as in_f:
                for i, line in enumerate(in_f):
                    out_f.write(line)
                    lines_written += 1
            
            # Write second file, skipping header
            with open(files[1], 'r', encoding='utf-8') as in_f:
                for i, line in enumerate(in_f):
                    if i == 0:  # Skip header line
                        continue
                    out_f.write(line)
                    lines_written += 1
        
        stats['processed'] += 1
        stats['total_lines'] += lines_written
        print(f"✓ Created {output_file.name} ({lines_written} lines)")
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Files processed: {stats['processed']}")
    print(f"  Files skipped: {stats['skipped']}")
    print(f"  Total lines written: {stats['total_lines']}")
    print(f"  Output directory: {OUTPUT_DIR}")
    print(f"{'='*60}")

if __name__ == "__main__":
    print("Starting file combination process...\n")
    combine_files()
    print("\n✅ Done!")
