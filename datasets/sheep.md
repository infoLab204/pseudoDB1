## Sheep data download
1. Create the required directories  
    a. If you are working with sheep data, create a directory named "sheep" in your home directory.    
 	```   
    mkdir sheep
 	```   
    b. In the "sheep" directory, create two sub-directories, "data" and "module" (see Fig. 1).    
 	```   
    cd sheep
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
    a. Visit the website: https://www.ebi.ac.uk/ena/browser/view/PRJNA160933.       <br>
  	
    b. Search for the sample "SRR501898".    <br>
	<img width="800" height="400" alt="image" src="https://github.com/user-attachments/assets/c2e98ebe-8cd8-4402-8ea8-f2cf2384f5f4" /> <br>
    *Fig. 2 : Result of SRR501898.* <br><br>

  	c. Go to the directory "fastq" and download the matching data (FASTQ) files.    
 	```   
    cd fastq
    ```   
   	```   
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR501/SRR501898/SRR501898_1.fastq.gz    
   	```   
	```   
    wget ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR501/SRR501898/SRR501898_2.fastq.gz    
 	```   

4.	Go to the "ref" directory and download the reference sequence.    
 	```   
  	cd ref
   	```
   	```       	    
    wget https://ftp.ncbi.nlm.nih.gov/genomes/genbank/vertebrate_mammalian/Ovis_aries/latest_assembly_versions/GCA_000298735.2_Oar_v4.0/GCA_000298735.2_Oar_v4.0_genomic.fna.gz
    ```
    ```      
    gzip -d GCA_000298735.2_Oar_v4.0_genomic.fna.gz # unzip 
    ```
    ```      
    mv GCA_000298735.2_Oar_v4.0_genomic.fna oar_ref_Oar_v4.0_full.fa # change reference name
 	```
    
5.	Go to the "db" directory and download two variant databases: dbSNP and pseudoDB.  <br>
    a.	Download dbSNP of sheep and assign a new name to it.   
 	```   
	wget https://ftp.ncbi.nih.gov/snp/organisms/archive/sheep_9940/VCF/00-All.vcf.gz
   	```
   	```   
    mv 00-All.vcf.gz sheep_dbSNP.vcf.gz # change dbSNP name
    ```       
   	```   
    gatk IndexFeatureFile -I sheep_dbSNP.vcf.gz  # create index
   	``` 
    b.	Download the pseudoDB of sheep    
 	```   
    wget https://zenodo.org/record/7488425/files/sheep_pseudoDB.vcf.gz
   	```          
      
<br>
