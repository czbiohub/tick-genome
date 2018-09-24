all: sync readme


sync:
	aws s3 sync s3://tick-genome/multiqc/multiqc_output/ .
	aws s3 sync s3://tick-genome/dna/2018-06-28/pre-assembly_qc_filter_test_v6_multiqc/ test_pre_assembly

readme:
	python3.6 generate_readme.py