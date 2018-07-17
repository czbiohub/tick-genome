all: sync readme


sync:
	aws s3 sync s3://tick-genome/dna/2018-06-28/pre-assembly_quality_control/ pre-assembly_quality_control/ 

readme:
	python3.6 generate_readme.py