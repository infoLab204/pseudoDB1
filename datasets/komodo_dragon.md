## Komodo dragon Data download
1. Create the required directories  
    a. If you are working with Komodo dragon  data, create a directory named "komodo" in your home directory.    
 	```   
    mkdir komodo
 	```   
    b. In the "komodo" directory, create two sub-directories, "data" and "module" (see Fig. 1).    
 	```   
    cd komodo
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
    (note) While you can process multiple samples for variant calling, this tutorial uses a single sample to keep the workflow simple.     <br>       
    a. Visit the website: https://www.ebi.ac.uk/ena/browser/view/PRJNA738464.       <br>
  	
    b. Search for the sample "SRR14830854".    <br>
	<img width="800" height="700" alt="image" src="https://github.com/user-attachments/assets/8715933b-ed59-463c-a653-7a845253870a" />    <br>
    *Fig. 2 : Result of SRR14830854.* <br><br>

  	c. Go to the directory "fastq" and download the matching data (FASTQ) files.    
 	```   
    cd fastq
    ```   
   	```   
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR148/054/SRR14830854/SRR14830854_1.fastq.gz   
   	```   
	```   
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR148/054/SRR14830854/SRR14830854_2.fastq.gz    
 	```   

4.	Go to the "ref" directory and download the reference sequence.    
 	```   
  	cd ref
   	```
   	```       	    
    wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/004/798/865/GCF_004798865.1_ASM479886v1/GCF_004798865.1_ASM479886v1_genomic.fna.gz
    ```
    ```      
    gzip -d GCF_004798865.1_ASM479886v1_genomic.fna.gz # unzip 
    ```
    ```      
    mv GCF_004798865.1_ASM479886v1_genomic.fna ASM479886v1_genomic.fa # change reference name
 	```
    
5.	Go to the "db" directory and download variant database: pseudoDB.  <br>
 	```   
    wget https://zenodo.org/record/18437361/files/komodo_pseudoDB.vcf.gz
   	```          
   	```   
    wget https://zenodo.org/record/18437361/files/komodo_pseudoDB.vcf.gz.tbi
   	```          
<br>
