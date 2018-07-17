#!/usr/bin/env python
# coding: utf-8
import os
import glob

readme = '''# Tick Genome Assembly and Annotation

[MultiQC Summary](pre-assembly_quality_control/multiqc/multiqc_report.html)

## Pre-Assembly FastQC reports

'''
for fastqc in glob.iglob('pre-assembly_quality_control/reports/*fastqc.html'):
    basename = os.path.basename(fastqc)
    sample_id = basename.split('_fastqc')[0]
    sample_name = sample_id.replace('_', ' ').title().replace("R1", "- Read 1").replace("R2", "- Read 2")
    readme += f'- [{sample_name}]({fastqc})\n'

with open("README.md", "w") as f:
	f.write(readme)
