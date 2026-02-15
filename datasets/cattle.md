## Cattle data download
1. Create the required directories  
    a. If you are working with cattle data, create a directory named "cattle" in your home directory.    
 	```   
    mkdir cattle
 	```   
    b. In the "cattle" directory, create two sub-directories, "data" and "module" (see Fig. 1).    
 	```   
    cd cattle
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
    a. Visit the website: https://www.ebi.ac.uk/ena/browser/view/PRJNA238491.     <br>
  	
    b. Search for the sample "SRR1293227" (see Fig. 2).    <br>
	  	<img width="800" height="500" alt="image" src="https://github.com/user-attachments/assets/c0f403bd-ce26-4865-8277-d78c6f2f9b61" />    
       *Fig. 2: Result of  SRR1293227.*        <br>
	  	
    c. Go to the directory "fastq" and download the matching data (FASTQ) files.    
  	```   
    cd fastq
    ```
    ```          
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR129/007/SRR1293227/SRR1293227_1.fastq.gz
    ```
    ``` 
  	wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR129/007/SRR1293227/SRR1293227_2.fastq.gz
    ```
    
4.	Go to the "ref" directory and download the reference sequence    
 	```   
    cd ref
   	```
   	```      	    
    wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/003/055/GCF_000003055.6_Bos_taurus_UMD_3.1.1/GCF_000003055.6_Bos_taurus_UMD_3.1.1_genomic.fna.gz    
   	```
   	```      	    
    gzip -d GCF_000003055.6_Bos_taurus_UMD_3.1.1_genomic.fna.gz    # unzip
   	```
   	```      	    
    mv GCF_000003055.6_Bos_taurus_UMD_3.1.1_genomic.fna  Bos_taurus_UMD_3.1.1_genomic.fa   
   	```        
5.	Go to the "db" directory and download two variant databases: dbSNP and pseudoDB.  <br>
    a.	Download dbSNP of cattle and assign a new name to it.   
 	```   
    wget https://ftp.ncbi.nih.gov/snp/organisms/archive/cow_9913/VCF/00-All.vcf.gz  
   	```
   	```   
    mv 00-All.vcf.gz cattle_dbSNP.vcf.gz    # change dbSNP name
   	```  
   	```   
    gatk IndexFeatureFile -I cattle_dbSNP.vcf.gz  # create index
   	```  
  	b.	Download the pseudoDB of cattle    
 	```   
    wget  https://zenodo.org/record/18333082/files/cattle_pseudoDB.vcf.gz   
    ```      
 	```   
    wget  https://zenodo.org/record/18333082/files/cattle_pseudoDB.vcf.gz.tbi   
    ```      
<br>
