## Stevia data download
1. Create the required directories  
    a. If you are working with Stevia  data, create a directory named "stevia" in your home directory.    
 	```   
    mkdir stevia
 	```   
    b. In the "stevia" directory, create two sub-directories, "data" and "module" (see Fig. 1).    
 	```   
    cd stevia
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
    a. Visit the website: https://www.ebi.ac.uk/ena/browser/view/PRJNA684944.       <br>
  	
    b. Search for the sample "SRR13325728".    <br>
	<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/1f37263b-a498-43a2-9ba3-44d1dcb4d403" /> <br>
    *Fig. 2 : Result of SRR13325728.* <br><br>

  	c. Go to the directory "fastq" and download the matching data (FASTQ) files.    
 	```   
    cd fastq
    ```   
   	```   
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR148/054/SRR13325728/SRR13325728_1.fastq.gz   
   	```   
	```   
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR148/054/SRR13325728/SRR13325728_2.fastq.gz    
 	```   

4.	Go to the "ref" directory and download the reference sequence.    
 	```   
  	cd ref
   	```
   	```       	    
    wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCA/009/936/405/GCA_009936405.2_ASM993640v2/GCA_009936405.2_ASM993640v2_genomic.fna.gz
    ```
    ```      
    gzip -d GCA_009936405.2_ASM993640v2_genomic.fna.gz # unzip 
    ```
    ```      
    mv GCA_009936405.2_ASM993640v2_genomic.fna ASM993640v2_genomic.fa # change reference name
 	```
    
5.	Go to the "db" directory and download variant database: pseudoDB.  <br>
 	```   
    wget https://zenodo.org/record/18437378/files/stevia_pseudoDB.vcf.gz
   	```          
 	```   
    wget https://zenodo.org/record/18437378/files/stevia_pseudoDB.vcf.gz.tbi
   	```            
<br>
