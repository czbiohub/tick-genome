qc: qc_tick1 qc_tick2
	

qc_tick1:
	/home/olga/miniconda3/envs/DeNovoPipeline/bin/deNovo_pipeline.py  \
		--global-config global.yml --sample-config quality_control_tick1.yml

qc_tick2:
	/home/olga/miniconda3/envs/DeNovoPipeline/bin/deNovo_pipeline.py  \
		--global-config global.yml --sample-config quality_control_tick2.yml

assemble:
	/home/olga/miniconda3/envs/DeNovoPipeline/bin/deNovo_pipeline.py \
		--global-config global.yml --sample-config assemble.yml
