## Rice data download
1. Create the required directories  
    a. If you are working with rice data, create a directory named "rice" in your home directory.    
 	```   
    mkdir rice
 	```   
    b. In the "rice" directory, create two sub-directories, "data" and "module" (see Fig. 1).    
  	```   
   cd rice    
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
    
2.	Go to the "fastq" directory and download FASTQ file.    
    (note) While you can process multiple samples for variant calling, this tutorial uses a single sample to keep the workflow simple.      <br>       
    a. Visit the website: https://www.ebi.ac.uk/ena/browser/view/PRJEB6180?show=reads.       <br>
  	
    b. Search for the sample "SAMEA2569416" for IRIS_313-10889.    <br>
	<img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/c0fd1007-02b4-490f-a654-cf4e4ff6d6a5" /> <br>
	*Fig. 2 : Result of IRIS_313-10889.*
  	
    c. Go to the directory "fastq" and download the matching data (FASTQ) files.    
   	```
    cd fastq    
   	```
	```
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR605/ERR605262/ERR605262_1.fastq.gz    
    ```
    ```
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR605/ERR605262/ERR605262_2.fastq.gz    
    ```
	```
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR605/ERR605263/ERR605263_1.fastq.gz    
    ```
	```
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR605/ERR605263/ERR605263_2.fastq.gz    	   
    ```

    d. Combine the individual FASTQ files, then update the resulting file name as specified.        
    ```
    zcat ERR605262_1.fastq.gz ERR605263_1.fastq.gz | gzip -c > IRIS_313-10889_1.fastq.gz    
    ```
    ```
    zcat ERR605262_2.fastq.gz ERR605263_2.fastq.gz | gzip -c > IRIS_313-10889_2.fastq.gz    
    ```

3.	Go to the "ref" directory and download the reference sequence.    
    ```
    cd ref
    ```
    ```
    wget https://ftp.ncbi.nlm.nih.gov/genomes/genbank/plant/Oryza_sativa/all_assembly_versions/GCA_001433935.1_IRGSP-1.0/GCA_001433935.1_IRGSP-1.0_genomic.fna.gz  
    ```
    ```
    gzip -d GCA_001433935.1_IRGSP-1.0_genomic.fna.gz   #unzip
    ```
    ```
    mv GCA_001433935.1_IRGSP-1.0_genomic.fna IRGSP-1.0_genome_full.fa # change reference name
    ```
	
4.	Go to the "db" directory and download two variant databases: dbSNP and pseudoDB.  <br>
    a.	Download dbSNP of rice and assign a new name to it.
  	```
    wget https://ftp.ncbi.nih.gov/snp/organisms/archive/rice_4530/VCF/00-All.vcf.gz
    ```
    ```  
    mv 00-All.vcf.gz rice_dbSNP.vcf.gz # change dbSNP name
    ```
    ```  
    gatk IndexFeatureFile -I rice_dbSNP.vcf.gz  #creates an index 
    ```
    b.	Download the pseudoDB of rice
  	```
    wget https://zenodo.org/record/7488383/files/rice_pseudoDB.vcf.gz
    ```
    ```
    wget https://zenodo.org/record/7488383/files/rice_pseudoDB.vcf.gz.tbi
    ```  
<br>
