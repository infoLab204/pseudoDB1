import os
import sys
import subprocess
import argparse

# home directory setting
home_path=os.path.expanduser("~")
home_path=home_path+"/gatk3"


# working directory 
def set_wd(species) :
    path_dir=f"{home_path}/{species}/module"
    dict_list=os.listdir(path_dir)

    dict_exts=["align","machine","error","model","variants"]

    missing_dict=[]

    for f in dict_exts :
        full_path=os.path.join(path_dir,f)
        if not os.path.exists(full_path) :
            missing_dict.append(f)

    if not missing_dict :
        print("The directorys are already ready")
    else :    
        # result of aligning FASTQ to reference resulting BAM
        os.mkdir(f"{home_path}/{species}/module/align")

        # result of recalibrating maching-provided base quality score
        os.mkdir(f"{home_path}/{species}/module/machine")
 
        # result of estimating sample error rate
        os.mkdir(f"{home_path}/{species}/module/error")

        # result of estimating model-adjusted base quality score
        os.mkdir(f"{home_path}/{species}/module/model")

        # result of genetic variant calling
        os.mkdir(f"{home_path}/{species}/module/variants")

# end of set_wd()



# reference section
def pre_align(species, reference_file) :
    path_dir=f"{home_path}/{species}/data/ref"
    file_list=os.listdir(path_dir)

    file_exts=[f"{reference_file}.0123",f"{reference_file}.amb",f"{reference_file}.ann",f"{reference_file}.fai",\
            f"{reference_file}.amb",f"{reference_file}.bwt.2bit.64",f"{reference_file}.pac",f"{reference_file[:reference_file.find('.f')]}.dict"]

    missing_files=[]

    for f in file_exts :
        full_path=os.path.join(path_dir,f)
        if not os.path.exists(full_path) :
            missing_files.append(f)

    if not missing_files :
        print("The reference files are already ready")

    else :   
        # if ".dict" file exists, delete it
        os.system(f"rm -rf {home_path}/{species}/data/ref/*.dict")

        # preparing the reference sequence
        os.system(f"bwa-mem2 index {home_path}/{species}/data/ref/{reference_file}")      

        # generate the fasta file index by running the following SAMtools command
        os.system(f"samtools faidx {home_path}/{species}/data/ref/{reference_file}")

        # generate the sequence dictionary 
        os.system(f"picard CreateSequenceDictionary \
                REFERENCE={home_path}/{species}/data/ref/{reference_file} \
                OUTPUT={home_path}/{species}/data/ref/{reference_file[:reference_file.find('.f')]}.dict")

# end of pre_align()



# Align FASTQ file of single samples to the reference
def align_fastq(species, reference_file, n_thread, sample_name) :

    # mapping to reference
    os.system(f"bwa-mem2 mem -M -t {n_thread} -R '@RG\\tID:{sample_name}\\tLB:{sample_name}\\tSM:{sample_name}\\tPL:ILLUMINA'  \
            {home_path}/{species}/data/ref/{reference_file} \
            {home_path}/{species}/data/fastq/{sample_name}_1.fastq.gz {home_path}/{species}/data/fastq/{sample_name}_2.fastq.gz \
            > {home_path}/{species}/module/align/{sample_name}_init.sam") 

 
    # Mark Duplicate and Sort
    subprocess.run(["picard","SortSam",f"I={home_path}/{species}/module/align/{sample_name}_init.sam", "TMP_DIR=temp",  \
            f"O={home_path}/{species}/module/align/{sample_name}_sorted.sam", "SORT_ORDER=coordinate"],check=True)
    
    if os.path.exists(f"{home_path}/{species}/module/align/{sample_name}_init.sam"):
        os.remove(f"{home_path}/{species}/module/align/{sample_name}_init.sam")
    
    subprocess.run(["picard","MarkDuplicates", f"I={home_path}/{species}/module/align/{sample_name}_sorted.sam", \
            f"O={home_path}/{species}/module/align/{sample_name}_aligned.bam",  \
            f"M={home_path}/{species}/module/align/{sample_name}_metrics.txt","MAX_FILE_HANDLES_FOR_READ_ENDS_MAP=1000"],check=True)
    
    if os.path.exists(f"{home_path}/{species}/module/align/{sample_name}_sorted.sam"):
        os.remove(f"{home_path}/{species}/module/align/{sample_name}_sorted.sam")

    # make index file
    os.system(f"picard BuildBamIndex I={home_path}/{species}/module/align/{sample_name}_aligned.bam \
            O={home_path}/{species}/module/align/{sample_name}_aligned.bai")

    os.system(f"rm -rf {home_path}/{species}/module/align/{sample_name}_metrics.txt");

# end of align_fastq()


# Construct a pseudo database by using all samples in the align directory
def pseudo_db(species, reference_file):
    path_dir=f"{home_path}/{species}/module/align"
    
    file_list=os.listdir(path_dir)

    sample=[]
    sample_list=""

    for file_name in file_list  :
        if file_name.find("_aligned.bam") !=-1 :
            sample.append(file_name)
    
    # UnifiedGenotyper caller
    for i in range(len(sample)) :  
        sample_list=sample_list + f"-I {home_path}/{species}/module/align/{sample[i]} "
    sample_list=sample_list + f"-o {home_path}/{species}/data/db/{species}_pseudoDB.vcf.gz --genotype_likelihoods_model BOTH "

    os.system(f"gatk  -T UnifiedGenotyper -R {home_path}/{species}/data/ref/{reference_file} {sample_list}")

# end of pseudo_db()


# Recalibrate base quality score from samples
def qs_recal(species, reference_file, dbtype, sample_name) : 
    vcf_dir=f"{home_path}/{species}/data/db"
    vcf_list=os.listdir(vcf_dir)

    database=f"{species}_{dbtype}.vcf.gz"
    if database not in vcf_list :
        sys.exit("Not found database")		


    # run each sample
    # BaseRecalibrator
    os.system(f"gatk -T BaseRecalibrator -R {home_path}/{species}/data/ref/{reference_file} \
            -I {home_path}/{species}/module/align/{sample_name}_aligned.bam  -knownSites {home_path}/{species}/data/db/{database} \
            -o {home_path}/{species}/module/machine/{sample_name}_{dbtype}_recalibration_table &> \
            {home_path}/{species}/module/machine/{sample_name}_{dbtype}_recalibration_table.log")

    # PrintReads
    os.system(f"gatk -T PrintReads -R {home_path}/{species}/data/ref/{reference_file} \
            -I {home_path}/{species}/module/align/{sample_name}_aligned.bam  -BQSR {home_path}/{species}/module/machine/{sample_name}_{dbtype}_recalibration_table \
            -o {home_path}/{species}/module/machine/{sample_name}_{dbtype}_recalibrated.bam &> \
            {home_path}/{species}/module/machine/{sample_name}_{dbtype}_recalibrated_bam.log")

    # delete file
    os.system(f"rm -rf {home_path}/{species}/module/machine/{sample_name}_{dbtype}_recalibration_table  \
            {home_path}/{species}/module/machine/{sample_name}_{dbtype}_recalibration_table.log \
            {home_path}/{species}/module/machine/{sample_name}_{dbtype}_recalibrated_bam.log")


# end of qs_recal()

# Call genetic variants - step 1 : Call variants from each samples. 
def variant_call(species, reference_file, dbtype):
    path_dir=f"{home_path}/{species}/module/machine"
    file_list=os.listdir(path_dir)

    sample=[]
    sample_list=""
    type_name=f"_{dbtype}_recalibrated.bam"
    for file_name in file_list  :
        if file_name.find(type_name) !=-1 :
            sample.append(file_name[:file_name.find(type_name)])
   
    # UnifiedGenotyper caller
    cmd_line=""
    for i in range(len(sample)) :
        cmd_line=cmd_line + f"-I {home_path}/{species}/module/machine/{sample[i]}_{dbtype}_recalibrated.bam "
    cmd_line=cmd_line + f"-o {home_path}/{species}/module/variants/{species}_{dbtype}_UC_variant_calling.vcf.gz \
            --genotype_likelihoods_model BOTH &> {home_path}/{species}/module/variants/{species}_{dbtype}_variant_calling.vcf.gz.log"
    print(cmd_line)
    os.system(f"gatk  -T UnifiedGenotyper -R {home_path}/{species}/data/ref/{reference_file} {cmd_line}" );
    os.system(f"rm -rf {home_path}/{species}/module/variants/{species}_{dbtype}_variant_calling.vcf.gz.log" );

# end of variant_call()


# Estimate sample error rate
def error_rate(species, reference_file, dbtype,sample) :
    database=f"{species}_{dbtype}.vcf.gz"

    ## database check
    vcf_dir=f"{home_path}/{species}/data/db"
    vcf_list=os.listdir(vcf_dir)

    if database not in vcf_list :
        sys.exitprint("Not found database")		

    if database in vcf_list and ".gz" in database :
        os.system(f"zcat {home_path}/{species}/data/db/{database} > {home_path}/{species}/data/db/{species}_{dbtype}.vcf")
    database=database[:database.find(".gz")]

    os.system(f"samtools mpileup -Bf {home_path}/{species}/data/ref/{reference_file} \
            {home_path}/{species}/module/align/{sample}_aligned.bam > {home_path}/{species}/module/error/{sample}_error\n")
    
    infile_name=f"{home_path}/{species}/module/error/{sample}_error"  # mileup output file load
    infile=open(infile_name,"r")

    
    outfile_name=f"{home_path}/{species}/module/error/{sample}_error_analysis"
    outfile=open(outfile_name,"w")

    line=infile.readline()
    line_list=line.strip().split("\t")

    while line !="" :
        if line_list[3]!="0" :
            d=line_list[4].find("^")   # start of read segment 
            while d !=-1 :
                line_list[4]=line_list[4].replace(line_list[4][d:d+2],"")
                d=line_list[4].find("^")

            line_list[4]=line_list[4].replace("$","")   # end of a read segment
            line_list[4]=line_list[4].replace("*","")   #
            line_list[4]=line_list[4].replace(".","")   # match to the refernece base on the forward strand
            line_list[4]=line_list[4].replace(",","")   # match to the reference base on the reverse strand

            if line_list[4]!="" :
                indelnum=0
                indelnum=indelnum+line_list[4].count("+")   # insertion from the reference
                indelnum=indelnum+line_list[4].count("-")   # deletion from the reference
                tmpgeno=line_list[4]
                i=tmpgeno.find("+")
                while i!=-1 :
                    if tmpgeno[i+1:i+3].isdigit()==True :
                        n=int(tmpgeno[i+1:i+3])
                        tmpgeno=tmpgeno.replace(tmpgeno[i:i+3+n],"")
                    else :
                        n=int(tmpgeno[i+1:i+2])
                        tmpgeno=tmpgeno.replace(tmpgeno[i:i+2+n],"")
                    i=tmpgeno.find("+")
                i=tmpgeno.find("-")
                while i!=-1 :
                    if tmpgeno[i+1:i+3].isdigit()==True :
                        n=int(tmpgeno[i+1:i+3])
                        tmpgeno=tmpgeno.replace(tmpgeno[i:i+3+n],"")         
                    else :
                        n=int(tmpgeno[i+1:i+2])
                        tmpgeno=tmpgeno.replace(tmpgeno[i:i+2+n],"")
                    i=tmpgeno.find("-")           
                mnum=len(tmpgeno)+indelnum
                outfile.write(f"{line_list[0]}\t{line_list[1]}\t{line_list[2]}\t{line_list[3]}\t{mnum}\t{line_list[4]}\n")
        line=infile.readline()
        line_list=line.strip().split("\t")

    os.system(f"rm -rf {home_path}/{species}/module/error/{sample}_error")
    infile.close()
    outfile.close()
    
	
   
    ## database unique position check
    db_name=f"{home_path}/{species}/data/db/{database}"
    db_uniq_check=f"{home_path}/{species}/data/db/{species}_{dbtype}_uniq_pos"

    db_dir=f"{home_path}/{species}/data/db"
    db_list=os.listdir(db_dir)
    if db_uniq_check not in db_list :
        snp_extract=f'grep -v "^#" {db_name}  | cut -f1,2 | uniq > {home_path}/{species}/data/db/{species}_{dbtype}_uniq_pos'    # database uniq position search
        os.system(snp_extract)
    
    sample_uniq_check=f"{home_path}/{species}/module/error/{sample}_error_analysis_uniq_pos"
    sample_dir=f"{home_path}/{species}/module/error"
    sample_list=os.listdir(sample_dir)

    if sample_uniq_check not in sample_list :
        sample_name=f"{home_path}/{species}/module/error/{sample}_error_analysis"
        sample_extract=f"cut -f1,2 {sample_name} > {home_path}/{species}/module/error/{sample}_error_analysis_uniq_pos"     # sample uniq position search
        os.system(sample_extract)

    sdiff_exe=f"sdiff {home_path}/{species}/data/db/{species}_{dbtype}_uniq_pos  {home_path}/{species}/module/error/{sample}_error_analysis_uniq_pos \
            > {home_path}/{species}/module/error/{sample}_{dbtype}_analysis"   ## database and sample analysis file 
    os.system(sdiff_exe)

    rm_cmd=f"rm -rf {home_path}/{species}/module/error/{sample}_error_analysis_uniq_pos"
    os.system(rm_cmd)

    awk_cmd="awk '{if(NF==4) print $0;}'"
    sdiff_extract=f"{awk_cmd} {home_path}/{species}/module/error/{sample}_{dbtype}_analysis > {home_path}/{species}/module/error/{sample}_{dbtype}_common"
    os.system(sdiff_extract)

    rm_cmd=f"rm -rf {home_path}/{species}/module/error/{sample}_{dbtype}_analysis"
    os.system(rm_cmd)

    eff_variant=f"cut -f1,2 {home_path}/{species}/module/error/{sample}_{dbtype}_common  > {home_path}/{species}/module/error/{sample}_{dbtype}_variant_pos"
    os.system(eff_variant)
   
    rm_cmd=f"rm -rf {home_path}/{species}/module/error/{sample}_{dbtype}_common"  
    os.system(rm_cmd)
    
    sample_name=f"{home_path}/{species}/module/error/{sample}_error_analysis"
    eff_name=f"{home_path}/{species}/module/error/{sample}_{dbtype}_variant_pos"

    sample_infile=open(sample_name,"r")
    eff_infile=open(eff_name,"r")

    error_rate_file=f"{home_path}/{species}/module/error/{sample}_{dbtype}_erate"
    error_rate=open(error_rate_file,"w")

    mismatch_str="awk '{ sum+=$5} END { print sum;}'"
    mismatch_cmd=f"{mismatch_str} {sample_name} > {home_path}/{species}/module/error/{sample}_mismatch"
    os.system(mismatch_cmd)

    mismatch_name=f"{home_path}/{species}/module/error/{sample}_mismatch"

    mismatch_infile=open(mismatch_name,"r")
    mismatch_num=int(mismatch_infile.readline())

    eff_num=0
    while True :
        eff_base=eff_infile.readline()

        if eff_base=="" :
            break

        eff_list=eff_base.strip().split("\t")
        
        while True :
            base_sample=sample_infile.readline()

            if base_sample=="" :
                break

            base_list=base_sample.split('\t') 
            if eff_list[0]==base_list[0] and eff_list[1]==base_list[1] :
                eff_num=eff_num+int(base_list[4])
                break

    error_rate.write(f"{sample}\t{(mismatch_num-eff_num)/mismatch_num}")

    rm_cmd=f"rm -rf {home_path}/{species}/module/error/{sample}_{dbtype}_variant_pos"
    os.system(rm_cmd)
    
    rm_cmd=f"rm -rf {home_path}/{species}/module/error/{sample}_mismatch"
    os.system(rm_cmd)
    
    rm_cmd=f"rm -rf {home_path}/{species}/module/error/{sample}_error_analysis"
    os.system(rm_cmd)
    
    rm_cmd=f"rm -rf {home_path}/{species}/data/db/{species}_{dbtype}.vcf"
    os.system(rm_cmd)
	
	
    sample_infile.close()
    eff_infile.close()
    error_rate.close()

# end of error_rate()

# Estimate model-adjusted base quality score.
def qs_model(species, dbtype, sample_name) :
    
    os.system(f"samtools view -h {home_path}/{species}/module/machine/{sample_name}_{dbtype}_recalibrated.bam \
            > {home_path}/{species}/module/model/{sample_name}_{dbtype}_recalibrated.sam")
     
    sample_file=f"{home_path}/{species}/module/model/{sample_name}_{dbtype}_recalibrated.sam"

    sample_infile=open(sample_file,"r")
    
    q_count=[]
    for i in range(100) :
        q_count.append(0)

    line=sample_infile.readline()

    while line[0]=="@" :
        line=sample_infile.readline()

    while line!="" :
        line_list=line.strip().split("\t")
        i=0
        while i < len(line_list[10]) :
            qscore=ord(line_list[10][i])-33
            q_count[qscore]=q_count[qscore]+1
            i=i+1
        line=sample_infile.readline()
   
    
    sample_infile.close()
	
    sample_outname=f"{home_path}/{species}/module/model/{sample_name}_{dbtype}_qs"
    sample_outfile=open(sample_outname,"w")

    hap=0
    hhap=0
  
    for i in range(len(q_count)) :
        hap=hap+q_count[i]
        hhap=hhap+i*q_count[i]
    
    sample_outfile.write(f"{sample_name}\t{hhap/hap}")
    sample_outfile.close()

    os.system(f"rm -rf {home_path}/{species}/module/model/{sample_name}_{dbtype}_recalibrated.sam")

# end of qs_model()


def main() :
    #os.system("curl -L -O https://raw.githubusercontent.com/infoLab204/pseudoDB/refs/heads/main/pipeline/pipeline3.py")
    """
    parser = argparse.ArgumentParser(usage='python %(prog)s [options]', prog='pipeline3.py' )

    parser.add_argument('--species', '-sp', help='the target speices name', required=True)
    parser.add_argument('--reference', '-ref', help='the filename of the reference sequence file', required=True)
    parser.add_argument('--sample', '-s', help='the filename of the sample data', required=True)
    parser.add_argument('--database', '-db', help='the specific database of known variants to be used', required=True)
    parser.add_argument('--thread', '-nt', type=int, help='the number of CPU threads to allocate for the process', required=True)

    args = parser.parse_args()

    species=args.species # the target species name
    ref=args.reference  # the filename of the reference sequence file
    sample=args.sample  # the filename of the FASTQ data
    dbtype=args.database  # the specific database of known variants to be used
    thread=args.thread  # the number of CPU threads to allocate for the process
    """

    species=sys.argv[1] # the target species name
    ref=sys.argv[2]  # the filename of the reference sequence file
    sample=sys.argv[3]  # the filename of the FASTQ data
    dbtype=sys.argv[4]  # the specific database of known variants to be used
    thread=int(sys.argv[5]) # the number of CPU threads to allocate for the process

    # Create subdirectories under directory "module".
    set_wd(species)
    
    # Create file names for the alignment under directory "ref".
    pre_align(species, ref)

    # Align FASTQ file of single samples to the reference.
    align_fastq(species, ref,thread,sample)

    if dbtype.upper()=="NULL" :
        pseudo_db(species,ref)  # Construct a pseudo-database using all samples located in the "align" directory.
    else :
        # Recalibrate base quality score from sample.
        qs_recal(species, ref, dbtype, sample)

        # Estimate sample error rate.
        error_rate(species,ref, dbtype, sample)

        # Estimate model-adjusted base quality score.
        qs_model(species, dbtype, sample)

        # Call genetic variants.
        variant_call(species, ref, dbtype)
    
# end of main()

if __name__ == "__main__":
    main()

