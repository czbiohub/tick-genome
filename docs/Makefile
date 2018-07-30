all: sync readme


sync:
	aws s3 sync s3://tick-genome/multiqc/multiqc_output/ .

readme:
	python3.6 generate_readme.py