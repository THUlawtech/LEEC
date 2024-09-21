# leec: A Legal Element Extraction Dataset with an Extensive Domain-Specific Label System

LEEC is a comprehensive, large-scale criminal element extraction dataset, comprising 15754 judicial documents and 128 labels. 
This dataset was constructed through two main steps: First, designing the label system by our team of legal experts based on 
prior legal research which identified critical factors driving and processes generating sentencing outcomes in criminal cases; 
Second, employing the legal knowledge to annotate judicial documents according to the label system and annotation guideline.
The Legal Element ExtraCtion dataset (LEEC) represents the most extensive and domain-specific legal element extraction dataset in China.

More details can be found in our paper: 
https://arxiv.org/abs/2310.01271

### Dataset

- 2023/8/29 - v1.0.0: Release LEEC-DEE dataset

We provided the original LEEC dataset and the preprocessed LEEC-DEE dataset.

[LEEC]() : 【待更新】

the original LEEC dataset.

| #LEEC | With Trigger |  Without Trigger  | 
| ---------: | :-----: | :---: | 
|  Size         | 4182      |11572     | 

[LEEC-DEE](https://pan.baidu.com/s/1vg3ecHhsaNSUD419SKC8qg?pwd=nqab): key（提取码）: nqab

the preprocessed dataset fo Document Event Extraction (DEE) task.

| #LEEC-DEE | Train |  Dev  | Test |
| ---------: | :-----: | :---: | :-------: |
|  Size         | 3325      |415     | 416       |


## DEE task

For the DEE task, we selected some representative labels in LEEC labeling system to extract important event information of the de-
fendant.

- Since most legal cases do not typically demonstrate a direct correspondence relation between defendants and victims when there
are multiple defendants and victims involved, we uniformly set the name of the victim in the event table as the first victim appear-
ing in the document. 
- The maximum number of defendants to be drawn from a judgment document is 7. 

Our code mainly references the implementation of [DocEE-Toolkit](https://github.com/Spico197/DocEE) 

### Installation

Make sure you have the following dependencies installed.

- Python 3.7.7
  - torch==1.5.1  # should be OK with higher torch version
  - pytorch-mcrf==0.0.3 # for MaskedCRF
  - gpu-watchmen==0.3.8 # if you wanna wait for a vacant GPU via `gpu-watchmen`
  - loguru==0.5.3
  - matplotlib==3.3.0
  - numpy==1.19.0
  - transformers==4.9.1
  - dgl-cu92==0.6.1  # find a version that is compatable with your CUDA version
  - tqdm==4.53.0
  - networkx==2.4
  - tensorboard==2.4.1

### Quick Start
Before running any bash script, please ensure `bert_model` has been correctly set.

**Tip:** At least 4 * NVIDIA V100 GPU (at least 16GB) cards are required to run Doc2EDAG models.

```bash
# run DCFEE
$ nohup bash scripts/run_dcfee_legal_wo_tgg.sh 1>Logs/DCFEE_reproduction.log 2>&1 &
$ tail -f Logs/DCFEE_reproduction.log

# run Doc2EDAG
$ nohup bash scripts/run_doc2edag_legal_wo_tgg.sh 1>Logs/Doc2EDAG_reproduction.log 2>&1 &
$ tail -f Logs/Doc2EDAG_reproduction.log

# run on PTPCG
$ nohup bash scripts/run_ptpcg_legal_wo_tgg.sh 1>Logs/PTPCG_reproduction.log 2>&1 &
$ tail -f Logs/PTPCG_reproduction.log
```

### Some tips

- `dee` has evoluted to a toolkit package, make sure to install the package first: `pip install -e .`
- Please change the path to BERT to load the tokenizer.

## Licence

MIT Licence

