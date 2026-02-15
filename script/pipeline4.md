## Part III: Variant calling with analysis
1.	Download "gatk4.py" module from the github repository into directory "tools".   
    ```
    curl -L -O https://raw.githubusercontent.com/infoLab204/pseudoDB/refs/heads/main/pipeline/gatk4.py    
    ```

2.	Go to the directory "tools" and import the module as follows.   
    ```
    import  gatk4       # import the "gatk.py" module   
    ```  

3.	Create subdirectories under directory "module".    <br>

    ```
    gatk4.set_wd("human") 
    ```

    The list of subdirectories created under directory "module":   
    *	__align__ : results of aligning FASTQ to reference   
    *	___error___ : result of estimating sample error rate   
    *	___machine___ : result of recalibrating machine-provided base quality score    
    *	___model___ : result of estimating model-adjusted base quality score   
    *	___variants___ : result of genetic variant calling   
    
<br>

4.	Create file names for the alignment under directory "ref".  <br>  

    ```
	 gatk4.pre_align("human", "GRCh38_full_analysis_set_plus_decoy_hla.fa")   
    ```    
    The following files have been generated in the "ref" directory:
    *	GRCh38_full_analysis_set_plus_decoy_hla.fa.amb
    *	GRCh38_full_analysis_set_plus_decoy_hla.fa.ann
    *	GRCh38_full_analysis_set_plus_decoy_hla.fa.bwt.2bit.64
    *	GRCh38_full_analysis_set_plus_decoy_hla.fa.fai
    *	GRCh38_full_analysis_set_plus_decoy_hla.fa.pac
    *	GRCh38_full_analysis_set_plus_decoy_hla.fa.0123
    *	GRCh38_full_analysis_set_plus_decoy_hla.dict 
<br>

5.	Align FASTQ file of single samples to the reference.    <br>
    
    ```
    gatk4.align_fastq("human", "GRCh38_full_analysis_set_plus_decoy_hla.fa","HG00096")       
    ``` 
    (Note) Files "HG00096_aligned.bam" and "HG00096_aligned.bai" are created in the directory "align".    <br>        

    <br>

6.	Construct a pseudo-database using all samples located in the "align" directory.    
       
    ``` 
    gatk.pseudo_db("human","GRCh38_full_analysis_set_plus_decoy_hla.fa", "HaplotypeCaller")       
    ``` 
    (Note) File "human_pseudoDB.vcf.gz" and "human_pseudoDB.vcf.gz.tbi" are created in the directory "db".        
<br>

7.	Recalibrate base quality score from samples    

     ```
     gatk4.qs_recal("human", "GRCh38_full_analysis_set_plus_decoy_hla.fa", "dbSNP", "HG00096")     
     ```
     (Note) Files "HG00096_dbSNP_recalibrated.bam" and "HG00096_dbSNP_recalibrated.bai" are created in the directory "machine".  <br><br> 
     ```
     gatk4.qs_recal("human","GRCh38_full_analysis_set_plus_decoy_hla.fa", "pseudoDB", "HG00096")          
     ```     
     (Note) Files "HG00096_pseudoDB_recalibrated.bam" and "HG00096_pseudoDB_recalibrated.bai" are created in the directory "machine".  <br><br> 
     
  <br>

8.	Call genetic variants.    
 
	```
    gatk4.variant_call("human","GRCh38_full_analysis_set_plus_decoy_hla.fa", "dbSNP","HaplotypeCaller")
    ```  
     (Note) Files "human_dbSNP_variant_calling.vcf.gz" and "human_dbSNP_variant_calling.vcf.gz.tbi" are created in the directory "variants". <br><br>      
    ```
    gatk.variant_call("human","GRCh38_full_analysis_set_plus_decoy_hla.fa", "pseudoDB","HaplotypeCaller") 
    ```
    (Note) Files "human_pseudoDB_variant_calling.vcf.gz" and "human_pseudoDB_variant_calling.vcf.gz.tbi" are created in the directory "variants".    
<br>

 9.	Estimate sample error rate.   
  
    ```
    gatk4.error_rate("human", "GRCh38_full_analysis_set_plus_decoy_hla.fa", "dbSNP", "HG00096")   
    ```    
    (Note) File "HG00096_dbSNP_erate" is created in the directory "error".    <br><br>
    ```    
    gatk4.error_rate("human","GRCh38_full_analysis_set_plus_decoy_hla.fa", "pseudoDB", "HG00096")   
    ```    
    (Note) File "HG00096_pseudoDB_erate" is created in the directory "error".
  
  <br>

10.	Estimate model-adjusted base quality score.   
    ``` 
    gatk4.qs_model("human", "dbSNP", "HG00096")      
    ```  
    (Note) File "HG00096_dbSNP_qs" is created in the directory "model"    <br><br>
    ```
    gatk4.qs_model("human","pseudoDB", "HG00096") 
    ```  
    (Note) File "HG00096_pseudoDB_qs" is created in directory "model"   
  
<br><br>
####  End of tutorial  
