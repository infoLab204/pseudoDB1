## Chickpea Data download
1. Create the required directories  
    a. If you are working with chickpea data, create a directory named "chickpea" in your home directory.    
 	```   
    mkdir chickpea
 	```   

   b. In the "chickpea" directory, create two sub-directories, "data" and "module" (see Fig. 1).    
  	```   
    cd chickpea
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

2.	Go to the "fastq" directory and download FASTQ file
    (note) While you can process multiple samples for variant calling, this tutorial uses a single sample to keep the workflow simple.      <br>       
    a. Visit the website: https://db.cngb.org/search/project/CNP0000370/       <br>
  	
    b. Search for sample ID "CNS0051757" for "SRR5183095".    <br>
 	<img width="800" height="350" alt="image" src="https://github.com/user-attachments/assets/4fe25609-287e-427d-bf50-bef314a35006" /> <br>
	<img width="800" height="200" alt="image" src="https://github.com/user-attachments/assets/d3babd74-874c-4160-88b4-f6c6dd872bdb" />

    *Fig 2. Result of SRR5183095.*
  	
    c. Go to the directory "fastq" and download the matching data (FASTQ) files.    
    ```  
    cd fastq    
    ```
    ```  
    wget ftp://ftp2.cngb.org/pub/CNSA/data1/CNP0000370/CNS0051757/CNX0043911/CNR0062050/SRR5183095_1.fastq.gz
    ```
    ```        
    wget ftp://ftp2.cngb.org/pub/CNSA/data1/CNP0000370/CNS0051757/CNX0043911/CNR0062050/SRR5183095_2.fastq.gz
    ```      	

5.	Go to the "ref" directory and download the reference sequence.    
    ```  
    cd ref    	
    ```  
    ```  	
    wget https://ftp.ncbi.nlm.nih.gov/genomes/genbank/plant/Cicer_arietinum/all_assembly_versions/GCA_000331145.1_ASM33114v1/GCA_000331145.1_ASM33114v1_genomic.fna.gz    	
    ```
    ```  	
    gzip -d GCA_000331145.1_ASM33114v1_genomic.fna.gz  # unzip     
    ```
    ```  	
    mv GCA_000331145.1_ASM33114v1_genomic.fna  car_ref_ASM33114v1_full.fa  # change reference name
    ```
    
6.	Go to the "db" directory and download two variant databases: dbSNP and pseudoDB.  <br>
    a.	Download dbSNP of chickpea and assign a new name to it.
  	```  
    wget https://ftp.ncbi.nih.gov/snp/organisms/archive/chickpea_3827/VCF/vcf_chr_Ca1.vcf.gz
   	```
  	```        
    wget https://ftp.ncbi.nih.gov/snp/organisms/archive/chickpea_3827/VCF/vcf_chr_Ca2.vcf.gz    
  	```
    ```   
	wget https://ftp.ncbi.nih.gov/snp/organisms/archive/chickpea_3827/VCF/vcf_chr_Ca3.vcf.gz    
  	```
    ```  
    wget https://ftp.ncbi.nih.gov/snp/organisms/archive/chickpea_3827/VCF/vcf_chr_Ca4.vcf.gz    
  	```
   	```     
    wget https://ftp.ncbi.nih.gov/snp/organisms/archive/chickpea_3827/VCF/vcf_chr_Ca5.vcf.gz    
  	```
    ```  
    wget https://ftp.ncbi.nih.gov/snp/organisms/archive/chickpea_3827/VCF/vcf_chr_Ca6.vcf.gz    
  	```
  	```      
    wget https://ftp.ncbi.nih.gov/snp/organisms/archive/chickpea_3827/VCF/vcf_chr_Ca7.vcf.gz    
  	```
    ```  
    wget https://ftp.ncbi.nih.gov/snp/organisms/archive/chickpea_3827/VCF/vcf_chr_Ca8.vcf.gz    
  	```
	```  
    cat vcf_chr_Ca1.vcf.gz vcf_chr_Ca2.vcf.gz vcf_chr_Ca3.vcf.gz vcf_chr_Ca4.vcf.gz vcf_chr_Ca5.vcf.gz vcf_chr_Ca6.vcf.gz vcf_chr_Ca7.vcf.gz vcf_chr_Ca8.vcf.gz > chickpea_dbSNP.vcf.gz
    ```     
	```  
    gatk IndexFeatureFile -I chickpea_dbSNP.vcf.gz # create index
    ```
  
    b.	Download the pseudoDB of chickpea    
	```  
    wget https://zenodo.org/record/7487929/files/chickpea_pseudoDB.vcf.gz
  	```         
      
<br>
