# Installation and Workflow Guide
This tutorial is organized into two sections: tool installation and the genetic variant calling workflow. The first section guides you through using Conda to install essential software, such as BWA, Samtools, Picard, and GATK. The second section provides how to prepare the list of parameters for the workflow script. Please be aware that the installation procedure and workflow may vary depending on the specific GATK version used. The resulting directory structure is highlighted in Fig 1, and the workflow is demonstrated using a single-sample example in a Unix/Linux environment.
In the following examples:
-	Lines starting with # are comments providing context.
-	Commands inside code blocks are executable.
  
Note: Ensure all required data has been fully downloaded before proceeding.

<img width="800" height="350" alt="image" src="https://github.com/user-attachments/assets/60a4d87d-91bb-45a7-a710-52724e63e62b" />  <br>
*Fig. 1 : The overall structure of the directories.*
<br><br>
## Section1: Installation Procedure
This section provides a step-by-step guide for installing the necessary bioinformatics tools, including BWA, Samtools, Picard, and GATK. This guide supports two primary workflows: GATK v3 (UnifiedGenotyper) or GATK v4 (HaplotypeCaller). Please choose the option that best fits your research requirements.

Note: To find the specific version of Conda compatible with your system, visit the Anaconda Archive at https://repo.anaconda.com/archive/

### 1. Install Conda and Update Environment
Download the installer, run the installation script, and refresh your shell environment variables:    

- #### Download the Anaconda installer    
```   
wget https://repo.anaconda.com/archive/Anaconda3-2025.06-0-Linux-x86_64.sh     
```

- #### Execute the installation script    
```   
bash Anaconda3-2025.06-0-Linux-x86_64.sh    
```

- #### Reload environmental variables    
```   
source ~/.bashrc
```

### 2. Tool Installation Options
#### Option A: GATK4 Workflow    
This option sets up a modern environment utilizing the GATK4 HaplotypeCaller engine.    
```   
conda create -n gatk4        # Create a dedicated virtual environment    
```
```   
conda activate gatk4         # Activate the environment    
```
```   
conda install bioconda::bwa-mem2    
```
```   
conda install bioconda::samtools    
```
```   
conda install bioconda::picard    
```
```   
conda install bioconda::gatk4    
```

#### Option B: GATK3 Workflow    
This option is for legacy pipelines requiring the GATK3 UnifiedGenotyper. Note that GATK3 requires manual registration due to licensing.    
```   
conda create -n gatk3        # Create a dedicated virtual environment    
```
```   
conda activate gatk3         # Activate the environment    
```
```   
conda install bioconda::bwa-mem2    
```
```   
conda install bioconda::samtools=1.13    
```
```   
conda install bioconda::picard=2.0    
```
```   
conda install bioconda::gatk=3.8    
```   
Manually download and register GATK 3.8    
```  
wget https://storage.googleapis.com/gatk-software/package-archive/gatk/GenomeAnalysisTK-3.8-1-0-gf15c1c3ef.tar.bz2     
```
```  
bunzip2 GenomeAnalysisTK-3.8-1-0-gf15c1c3ef.tar.bz2    
```
```  
tar -xvf GenomeAnalysisTK-3.8-1-0-gf15c1c3ef.tar    
```
```  
mv GenomeAnalysisTK-3.8-1-0-gf15c1c3ef gatk3.8    
```
```  
gatk-register gatk3.8/GenomeAnalysisTK.jar    
```
<br><br>
## Section2: Variant Calling Workflow    
This section details the execution of the variant calling pipeline. The guide supports two primary engines: GATK v3 (UnifiedGenotyper) and GATK v4 (HaplotypeCaller). Users should select the option that best aligns with their research objectives.
Both workflows require the following input parameters:    
-	species: The target species name (refer to the species list in the dataset directory).
-	ref: The filename of the reference sequence file.
-	sample: The filename of the FASTQ data.
-	db_type: The specific database of known variants to be used (see "Note" below).
-	thread: The number of CPU threads to allocate for the process.    <br><br>

Note on db_type Values:    
    1. null: Use this when constructing a new pseudo-database.    
    2. dbSNP Name: Use this when calling variants using an existing dbSNP.    
    3. pseudoDB Name: Use this when calling variants using a previously generated pseudo-database.    <br><br>
Note: Certain species may lack established dbSNP resources.

#### Option A: GATK4 Workflow Execution
Download "pipeline4.py" module from the github repository into directory "_speices_".   
```   
curl -L -O https://raw.githubusercontent.com/infoLab204/pseudoDB/refs/heads/main/script/pipeline4.py  # download "pipeline4.py" module   
```   

```   
conda activate gatk4         # Activate the environment    
```
This option configures a modern environment utilizing the GATK4 HaplotypeCaller engine. The general command structure for the variant calling function is as follows:    <br><br>
__Command Syntax: python pipeline4.py species ref sample db_type thread__      <br><br>
Using the "human" dataset as an example, the three supported use cases are demonstrated below:    
- ##### Case 1: Generating a New Pseudo-Database
    ```  
    python pipeline4.py human GRCh38_full_analysis_set_plus_decoy_hla.fa HG00096 null 16    
    ```
    Upon completion, output VCF file will be located in the db/ directory.    

- ##### Case 2: Variant Calling with an Existing dbSNP
    ```  
    python pipeline4.py human GRCh38_full_analysis_set_plus_decoy_hla.fa HG00096 human_dbSNP.vcf.gz 16    
    ```  
- ##### Case 3: Variant Calling with a Custom Pseudo-Database 
    ```  
    python pipeline4.py human GRCh38_full_analysis_set_plus_decoy_hla.fa HG00096 human_pseudoDB.vcf.gz 16    
    ```
    Upon completion, all output VCF files will be located in the variants/ directory.

#### Option B: GATK3 Workflow
Download "pipeline3.py" module from the github repository into directory "_species_".   
```   
curl -L -O https://raw.githubusercontent.com/infoLab204/pseudoDB/refs/heads/main/script/pipeline3.py  # download "pipeline3.py" module   
```   

```   
conda activate gatk3         # Activate the environment    
```
This option configures a modern environment utilizing the GATK3 UnifiedGenotyper engine. The general command structure for the variant calling function is as follows:    <br><br>
__Command Syntax: python pipeline3.py species ref sample db_type thread__    <br><br>
Using the "human" dataset as an example, the three supported use cases are demonstrated below:    
- ##### Case 1: Generating a New Pseudo-Database
    ```  
    python pipeline3.py human GRCh38_full_analysis_set_plus_decoy_hla.fa HG00096 null 16
    ```
    Upon completion, output VCF file will be located in the db/ directory.   
- ##### Case 2: Variant Calling with an Existing dbSNP
    ```  
    python pipeline3.py human GRCh38_full_analysis_set_plus_decoy_hla.fa HG00096 human_dbSNP.vcf.gz 16    
    ```  
- ##### Case 3: Variant Calling with a Custom Pseudo-Database 
    ```  
    python pipeline3.py human GRCh38_full_analysis_set_plus_decoy_hla.fa HG00096 human_pseudoDB.vcf.gz 16    
    ```  
    Upon completion, all output VCF files will be located in the variants/ directory.







