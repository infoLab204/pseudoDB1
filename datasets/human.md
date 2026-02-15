## Human Data download
1. Create the required directories  
    a. If you are working with human data, create a directory named "human" in your home directory.    
 	```   
    mkdir human
 	```   
    b. In the "human" directory, create two sub-directories, "data" and "module" (see Fig. 1).    
 	```   
    cd human
   	```
   	```      
    mkdir data module
    ```   
   
    c. Go to the "data" directory and create the three sub-directories: "fastq", "ref", and "db" (see Fig. 1).    
 	```   
    cd data
   	```
   	```       
    mkdir fastq ref db
    ```       

3.	Go to the "fastq" directory and download FASTQ file.    
    (Note)  While you can process multiple samples for variant calling, this tutorial uses a single sample to keep the workflow simple.      <br>       
    a. Visit the website: https://www.internationalgenome.org/data-portal/sample.       <br>
  	
    b. Search for the sample "HG00096" (see Fig. 2).    <br>
	
    <img width="800" height="450" alt="image" src="https://github.com/user-attachments/assets/0be6f70d-c055-4623-9e62-d3f8786156c1" />      <br>
    *Fig. 2: https://www.internationalgenome.org/data-portal/sample.*        <br>
	
    c.  Locate the "1 matching sample" tag and click on "HG00096".
  	<img width="800" height="300" alt="image" src="https://github.com/user-attachments/assets/8cd1cdbb-79fc-42e3-934d-ea87b9b86e45" /> <br>
    *Fig. 3: Result of  HG00096.*        <br>
	
    d. In the filtering options, set the Data Type to "sequence" and the Technology to "Low coverage WGS". For this specific sample, you will see six available FASTQ files (as shown in Figure 4).    
    <img width="800" height="450" alt="image" src="https://github.com/user-attachments/assets/0cad54e6-98d2-4371-8a4b-a393464b9305" />     <br> 
    *Fig. 4: Result of  HG00096.*
  	
    e. Go to the directory "fastq" and download the matching data (FASTQ) files.    
  	```   
    cd fastq
    ```
    ```          
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR062/SRR062634/SRR062634_1.fastq.gz
    ```
    ``` 
  	wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR062/SRR062634/SRR062634_2.fastq.gz
    ```
    ``` 
  	wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR062/SRR062635/SRR062635_1.fastq.gz
    ```
    ``` 
  	wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR062/SRR062635/SRR062635_2.fastq.gz
    ```
    ``` 
  	wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR062/SRR062641/SRR062641_1.fastq.gz
  	```
    ``` 
  	wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR062/SRR062641/SRR062641_2.fastq.gz
    ```       	  

    f. Combine the individual FASTQ files, then update the resulting file name as specified.    
 	```   
  	zcat SRR062634_1.fastq.gz SRR062635_1.fastq.gz SRR062641_1.fastq.gz | gzip -c > HG00096_1.fastq.gz
   	```
   	```       
    zcat SRR062634_2.fastq.gz SRR062635_2.fastq.gz SRR062641_2.fastq.gz | gzip -c > HG00096_2.fastq.gz
    ```       

4.	Go to the "ref" directory and download the reference sequence    
 	```   
    cd ref
   	```
   	```      	    
    wget http://ftp.1000genomes.ebi.ac.uk/vol1/ftp/technical/reference/GRCh38_reference_genome/GRCh38_full_analysis_set_plus_decoy_hla.fa    
   	```
    
5.	Go to the "db" directory and download two variant databases: dbSNP and pseudoDB.  <br>
    a.	Download dbSNP of human and assign a new name to it.   
 	```   
    wget https://ftp.ncbi.nih.gov/snp/organisms/human_9606/VCF/00-All.vcf.gz  
   	```
   	```   
    mv 00-All.vcf.gz human_dbSNP.vcf.gz    # change dbSNP name
   	```
    ```   
    gatk IndexFeatureFile -I human_dbSNP.vcf.gz  # create index
   	```  

  	b.	Download the pseudoDB of human    
 	```   
    wget  https://zenodo.org/record/7488070/files/human_pseudoDB.vcf.gz   
    ```      
<br>
