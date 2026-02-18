## Brown bear data download
1. Create the required directories  
    a. If you are working with brown bear data, create a directory named "bear" in your home directory.    
    ```   
    mkdir bear
 	```   
    b. In the "bear" directory, create two sub-directories, "data" and "module" (see Fig. 1).    
 	```   
    cd bear
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
    (note) While you can process multiple samples for variant calling, this tutorial uses a single sample to keep the workflow simple.     <br>       
    a. Visit the website: https://www.ebi.ac.uk/ena/browser/view/PRJNA1139383.       <br>
  	
    b. Search for the sample "SRR29938644".    <br>
	<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/e926f650-3e3a-4b05-a2da-347674a88c35" />    <br>
    *Fig. 2 : Result of SRR29938644.* <br><br>

  	c. Go to the directory "fastq" and download the matching data (FASTQ) files.    
 	```   
    cd fastq
    ```   
   	```   
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR299/044/SRR29938644/SRR29938644_1.fastq.gz   
   	```   
	```   
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR299/044/SRR29938644/SRR29938644_2.fastq.gz    
 	```   

4.	Go to the "ref" directory and download the reference sequence.    
 	```   
  	cd ref
   	```
   	```       	    
    wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/023/065/955/GCF_023065955.2_UrsArc2.0/GCF_023065955.2_UrsArc2.0_genomic.fna.gz
    ```
    ```      
    gzip -d GCF_023065955.2_UrsArc2.0_genomic.fna.gz # unzip 
    ```
    ```      
    mv GCF_023065955.2_UrsArc2.0_genomic.fna UrsArc2.0_genomic.fa # change reference name
 	```
    
5.	Go to the "db" directory and download variant database: pseudoDB.  <br>
 	```   
    wget https://zenodo.org/record/18437343/files/bear_pseudoDB.vcf.gz
   	```          
  	```   
    wget https://zenodo.org/record/18437343/files/bear_pseudoDB.vcf.gz.tbi
   	```         
<br>
