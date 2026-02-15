## Swan goose data download
1. Create the required directories  
    a. If you are working with swan goose data, create a directory named "goose" in your home directory.    
 	```   
    mkdir goose
 	```   
    b. In the "goose" directory, create two sub-directories, "data" and "module" (see Fig. 1).    
 	```   
    cd goose
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
    a. Visit the website: https://www.ebi.ac.uk/ena/browser/view/PRJNA722049.       <br>
  	
    b. Search for the sample "SRR14534354".    <br>
	<img width="800" height="450" alt="image" src="https://github.com/user-attachments/assets/77b3d9d6-571b-4f84-9597-a52fceeb5edc" /> <br>
    *Fig. 2 : Result of SRR14534354.* <br><br>

  	c. Go to the directory "fastq" and download the matching data (FASTQ) files.    
 	```   
    cd fastq
    ```   
   	```   
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR145/054/SRR14534354/SRR14534354_1.fastq.gz   
   	```   
	```   
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR145/054/SRR14534354/SRR14534354_2.fastq.gz    
 	```   

4.	Go to the "ref" directory and download the reference sequence.    
 	```   
  	cd ref
   	```
   	```       	    
    wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/002/166/845/GCF_002166845.1_GooseV1.0/GCF_002166845.1_GooseV1.0_genomic.fna.gz
    ```
    ```      
    gzip -d GCF_002166845.1_GooseV1.0_genomic.fna.gz # unzip 
    ```
    ```      
    mv GCF_002166845.1_GooseV1.0_genomic.fna GooseV1.0_genomic.fa # change reference name
 	```
    
5.	Go to the "db" directory and download two variant databases: dbSNP and pseudoDB.  <br>
    a.	Download dbSNP of goose and assign a new name to it.   
 	  ```   
	  wget https://ftp.ebi.ac.uk/pub/databases/eva/rs_releases/release_8/by_species/anser_cygnoides/GooseV1.0/8845_GCA_002166845.1_current_ids.vcf.gz
   	```
   	```   
    mv 8845_GCA_002166845.1_current_ids.vcf.gz goose_dbSNP.vcf.gz # change dbSNP name
    ```       
   	```   
    gatk IndexFeatureFile -I goose_dbSNP.vcf.gz  # create index
   	```
    
    b.	Download the pseudoDB of goose    
 	```   
    wget https://zenodo.org/record/18437393/files/goose_pseudoDB.vcf.gz
   	```          
 	```   
    wget https://zenodo.org/record/18437393/files/goose_pseudoDB.vcf.gz.tbi
   	```            
<br>
