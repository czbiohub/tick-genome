multiqc:
	# Copy FastQC and other reports
	aws s3 sync --exclude "*.fastq.gz" s3://tick-genome/dna/2018-06-28/pre-assembly_quality_control/reports/ s3://tick-genome/multiqc/data-for-multiqc/  
	# Copy adapter trimming reports
	aws s3 sync --exclude "*.fastq.gz" s3://tick-genome/dna/2018-06-28/adapter_trimmed/ s3://tick-genome/multiqc/data-for-multiqc/
	reflow run multiqc.rf -input=s3://tick-genome/multiqc/data-for-multiqc/  -output=s3://tick-genome/multiqc/multiqc_output/

TABULA_MURIS_RUNS = 170907_A00111_0051_BH2HWLDMXX 170907_A00111_0052_AH2HTCDMXX 170910_A00111_0053_BH2HGKDMXX 170910_A00111_0054_AH2HGWDMXX 170914_A00111_0057_BH3FY7DMXX 170914_A00111_0058_AH3FYKDMXX 170918_A00111_0059_BH3G22DMXX 170918_A00111_0060_AH3FYVDMXX 170921_A00111_0062_BH3FYHDMXX 170921_A00111_0063_AH3G23DMXX 170925_A00111_0066_AH3TKNDMXX 170925_A00111_0067_BH3M5YDMXX 170928_A00111_0068_AH3YKKDMXX 170928_A00111_0069_BH52YMDMXX

tabula_muris_copy_logs:
	for TABULA_MURIS_RUN in ${TABULA_MURIS_RUNS} ; do \
		echo Syncing logs from run: $${TABULA_MURIS_RUN} ; \
		aws s3 sync --exclude "*" \
			--include "*htseq-count.txt" --include "*log.final.out" \
			s3://czbiohub-maca/remux_data/$${TABULA_MURIS_RUN}/results/ \
			s3://olgabot-maca/multiqc_test_input/$${TABULA_MURIS_RUN}/; \
	done

test_multiqc:
	reflow -cache=off run multiqc.rf -input s3://olgabot-maca/multiqc_test_input/170907_A00111_0051_BH2HWLDMXX/ -output s3://olgabot-maca/multiqc_test_output/170907_A00111_0051_BH2HWLDMXX/

test_cutadapt:
	reflow run cutadapt.rf -read1=s3://tick-genome/dna/2018-06-28/tick_1_S1_R1_001_first1Mreads.fastq.gz -read2=s3://tick-genome/dna/2018-06-28/tick_1_S1_R2_001_first1Mreads.fastq.gz -libprep=nextera -id=tick_1_S1_first1Mreads -output=s3://tick-genome/dna/2018-06-28/adapter_trimmed

test_adapterremoval:
	reflow run adapter_removal.rf -read1=s3://tick-genome/dna/2018-06-28/tick_1_S1_R1_001_first1Mreads.fastq.gz -read2=s3://tick-genome/dna/2018-06-28/tick_1_S1_R2_001_first1Mreads.fastq.gz -libprep=nextera -id=tick_1_S1_first1Mreads -output=s3://tick-genome/dna/2018-06-28/adapter_trimmed/


test_bbduk_adapterremoval:
	reflow run bbduk.rf -read1=s3://tick-genome/dna/2018-06-28/tick_1_S1_R1_001_first1Mreads.fastq.gz -read2=s3://tick-genome/dna/2018-06-28/tick_1_S1_R2_001_first1Mreads.fastq.gz -id=tick_1_S1_first1Mreads -output=s3://tick-genome/dna/2018-06-28/adapter_trimmed_test/


test_pre_assembly:
	reflow run pre-assembly.rf -read1=s3://tick-genome/dna/2018-06-28/tick_1_S1_R1_001_first1Mreads.fastq.gz -read2=s3://tick-genome/dna/2018-06-28/tick_1_S1_R2_001_first1Mreads.fastq.gz -id=tick_1_S1_first1Mreads -output=s3://tick-genome/dna/2018-06-28/pre-assembly_qc_filter_test/