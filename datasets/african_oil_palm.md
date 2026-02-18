## African oil palm Data download
1. Create the required directories  
    a. If you are working with African oil palm data, create a directory named "palm" in your home directory.    
 	```   
    mkdir palm
 	```   
    b. In the "palm" directory, create two sub-directories, "data" and "module" (see Fig. 1).    
 	```   
    cd palm
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
    a. Visit the website: https://www.ebi.ac.uk/ena/browser/view/PRJEB21246.       <br>
  	
    b. Search for the sample "ERR2004436".    <br>
	 <img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/7f0362f5-3ebf-4034-9e02-a8e83cad6bd8" />    <br>
    *Fig. 2 : Result of ERR2004436.* <br><br>

  	c. Go to the directory "fastq" and download the matching data (FASTQ) files.    
 	```   
    cd fastq
    ```   
   	```   
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR200/ERR2004436/ERR2004436_1.fastq.gz    
   	```   
	```   
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/ERR200/ERR2004436/ERR2004436_2.fastq.gz    
 	```   

4.	Go to the "ref" directory and download the reference sequence.    
 	```   
  	cd ref
   	```
   	```       	    
    wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/442/705/GCF_000442705.1_EG5/GCF_000442705.1_EG5_genomic.fna.gz
    ```
    ```      
    gzip -d GCF_000442705.1_EG5_genomic.fna.gz # unzip 
    ```
    ```      
    mv GCF_000442705.1_EG5_genomic.fna EG5_genomic.fa # change reference name
 	```
    
5.	Go to the "db" directory and download two variant databases: dbSNP and pseudoDB.  <br>
    a.	Download dbSNP of palmand assign a new name to it.   
 	```   
	wget https://ftp.ebi.ac.uk/pub/databases/eva/rs_releases/release_8/by_species/elaeis_guineensis/EG5/51953_GCA_000442705.1_current_ids.vcf.gz
   	```
   	```   
    mv 51953_GCA_000442705.1_current_ids.vcf.gz palm_dbSNP.vcf.gz # change dbSNP name
    ```       
   	```   
    gatk IndexFeatureFile -I palm_dbSNP.vcf.gz  # create index
   	``` 
    b.	Download the pseudoDB of palm 
 	```   
    wget https://zenodo.org/record/18437285/files/palm_pseudoDB.vcf.gz
   	```          
 	```   
    wget https://zenodo.org/record/18437285/files/palm_pseudoDB.vcf.gz.tbi
   	```          
            
<br>
