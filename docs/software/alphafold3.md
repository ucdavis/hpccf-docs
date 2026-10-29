# AlphaFold 3

[AlphaFold 3](https://github.com/google-deepmind/alphafold3) predicts the 3D structure of
proteins and their complexes with DNA, RNA, small-molecule ligands, and ions. HPC provides
a ready-to-use Apptainer container, a shared copy of the genetic databases, and an example
run script, so you don't need to install anything.

| Resource | Location |
|---|---|
| Apptainer image | `/cvmfs/hpc.ucdavis.edu/sw/sifs/alphafold/3/alphafold-3.sif` |
| Example run script | `/cvmfs/hpc.ucdavis.edu/sw/sifs/alphafold/3/run-alphafold.sh` |
| Genetic databases | `/quobyte/databases/alphafold3/` |

## How it works

The run script bind-mounts 4 directories into the apptainer:

| On the cluster | Inside the container | Purpose |
|---|---|---|
| `$HOME/.af3/input` | `/root/af_input` | Your input JSON file(s) |
| `$HOME/.af3/output` | `/root/af_output` | Prediction results |
| `$HOME/.af3/models` | `/root/models` | **Your own** AlphaFold 3 model parameters |
| `/quobyte/databases/alphafold3` | `/root/public_databases` | Genetic and structure databases |

    grants them to individual users only, so each user has to request their own copy as the HPC Core does not have the legal authority to agree to the terms of use on behalf of UC Davis. See
    [Getting the model parameters](#getting-the-model-parameters).

!!! important "You create the `~/.af3` directories"
    You need to create
    `$HOME/.af3/input`, `$HOME/.af3/output`, and `$HOME/.af3/models` yourself
    ([step 1](#1-create-your-af3-directories)) before running anything. Apptainer
    can't bind a directory that doesn't exist.


## Quick start

### 1. Create your `.af3` directories

```bash
mkdir -p $HOME/.af3/input $HOME/.af3/output $HOME/.af3/models
chmod 700 $HOME/.af3/models
```

### 2. Get the model parameters

Request and download your own copy, then put `af3.bin` in `$HOME/.af3/models`. See
[Getting the model parameters](#getting-the-model-parameters). Approval can take a few
days, so request access early.

### 3. Write an input file

The example script reads `$HOME/.af3/input/fold_input.json`. A minimal single-protein input:

```json
{
  "name": "my_first_fold",
  "sequences": [
    {
      "protein": {
        "id": "A",
        "sequence": "GMRESYANENQFGFKTINSDIHKIVIVGGYGKLGGLFARYLRASGYPISILDREDWAVAESILANADVVIVSVPINLTLETIERLKPYLTENMLLADLTSVKREPLAKMLEVHTGAVLGLHPMFGADIASMAKQVVVRCDGRFPERYEWLLEQIQIWGAKIYQTNATEHDHNMTYIQALRHFSTFANGLHLSKQPINLANLLALSSPIYRLELAMIGRLFAQDAELYADIIMDKSENLAVIETLKQTYDEALTFFENNDRQGFIDAFHKVRDWFGDYSEQFLKESRQLLQQANDLKQG"
      }
    }
  ],
  "modelSeeds": [1],
  "dialect": "alphafold3",
  "version": 1```

Read more about inputs here [AlphaFold 3 Inputs](https://github.com/google-deepmind/alphafold3/blob/main/docs/input.md)

### 4. Call the example script in a sbatch script

The example script /cvmfs/hpc.ucdavis.edu/sw/sifs/alphafold/3/run-alphafold.sh:
```bash
#!/usr/bin/env sh

module load apptainer
export AF3_DB_DIR="${AF3_DB_DIR:-/quobyte/databases/alphafold3}"

command -v apptainer >/dev/null 2>&1 || echo "apptainer not found" >&2 && exit 1
apptainer exec \
	--nv \
	--bind $HOME/.af3/input:/root/af_input \
	--bind $HOME/.af3/output:/root/af_output \
	--bind $AF3_DB_DIR:/root/public_databases \
	--bind $HOME/.af3/models:/root/models \
	/cvmfs/hpc.ucdavis.edu/sw/sifs/alphafold/3/alphafold3.sif \
	python alphafold3/run_alphafold.py \
	--json_path=/root/af_input/fold_input.json \
	--model_dir=/root/models \
	--db_dir=/root/public_databases \
	--output_dir=/root/af_output $@
```

| Option | Meaning |
|---|---|
| `--nv` | Gives the container access to the node's NVIDIA GPU in case you are using any |
| `--bind A:B` | Makes cluster directory `A` visible inside the container at `B` |
| `--json_path` | The input file to predict |
| `--model_dir` | Model parameters inside the container (your `$HOME/.af3/models`) |
| `--db_dir` | Genetic databases inside the container |
| `--output_dir` | Where results are written (your `$HOME/.af3/output`) |

Add to an sbatch script like so:
```bash
#!/bin/bash
#SBATCH --job-name=af3
#SBATCH --partition=low
#SBATCH --account=<your-account>
#SBATCH --gpus=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --time=8:00:00
#SBATCH --output=/home/%u/%x/%N.af3_%j.out
#SBATCH --error=/home/%u/%x/%N.af3_%j.err

/cvmfs/hpc.ucdavis.edu/sw/sifs/alphafold/3/run-alphafold.sh
```

**For multiple inputs per job.** Name inputs `input_1.json`, `input_2.json`, ... and add:

```bash
#SBATCH --array=1-100%10        # %10 = at most 10 running at once
#SBATCH --output=/home/%u/%x/af3_%A_%a.out
#SBATCH --error=/home/%u/%x/af3_%A_%a.err

INPUT_JSON=input_${SLURM_ARRAY_TASK_ID}.json
```

## Output

Results go in `$HOME/.af3/output/<name>/`:
```text
<name>_model.cif                 # top-ranked structure
<name>_summary_confidences.json  # summary scores of the top model
<name>_confidences.json          # per-atom/per-residue confidences of the top model
<name>_data.json                 # input + MSAs + templates (reusable)
<name>_ranking_scores.csv        # ranking score of every sample
seed-<N>_sample-<M>/             # each individual sample
```

If the folder already exists, a new one with a timestamp suffix is created rather than
overwriting. Structures are mmCIF; open them in ChimeraX, PyMOL, or [Mol*](https://molstar.org/viewer/).

Read more about output here [AlphaFold 3 Output](https://github.com/google-deepmind/alphafold3/blob/main/docs/output.md)

## Getting the model parameters

Google DeepMind provides the AlphaFold 3 model parameters directly to individual users
for non-commercial use. HPC can't download or share them for you.

1. **Request access** with
   [Google DeepMind's request form](https://forms.gle/svvpY4u2jsHEwWYS6). Use your
   institutional (`@ucdavis.edu`) email address and give accurate details. Google DeepMind
   reviews requests manually and usually replies within a few business days.
2. **Download the file.** The approval email has a download link for `af3.bin.zst`
   (about 1 GB). Download it on your computer and copy it to the cluster:

    ```bash
    scp af3.bin.zst <username>@<cluster-login-host>:~/.af3/models/
    ```

    Or, if the link works from the cluster, download it straight into the folder:

    ```bash
    cd $HOME/.af3/models
    wget -O af3.bin.zst "<download link from the email>"
    ```

3. **Decompress it:**

    ```bash
    cd $HOME/.af3/models
    zstd -d af3.bin.zst
    ```

4. **Check that it's there:**

    ```bash
    ls -lh $HOME/.af3/models
    # af3.bin should be listed
    ```

## Troubleshooting

**`no apptainer found` / `apptainer: command not found`** — run `module load apptainer`
on a compute node.

**`mount source ... doesn't exist`**: you haven't created one of your `.af3` directories yet. Run
`mkdir -p $HOME/.af3/input $HOME/.af3/output $HOME/.af3/models`.

**Errors about missing or unloadable model parameters**: check that `af3.bin` is in
`$HOME/.af3/models`, that it's decompressed (not just `af3.bin.zst`), and that your
script has `--bind $HOME/.af3/models:/root/models`. See
[Getting the model parameters](#getting-the-model-parameters).

**`No such file` for `fold_input.json`** — the file must be in `$HOME/.af3/input/`, and
`--json_path` must use the container path `/root/af_input/...`, not your home path.

**No GPU found / running on CPU** — make sure the job requested `--gpus=1` and the
script includes `--nv`. Check with `nvidia-smi` inside the job.

**Out of GPU memory** — reduce the input size, request a larger GPU, or enable unified
memory by adding these before `apptainer exec`:

**Disk quota exceeded** — outputs (especially many seeds) can be large. Move them to
group storage, symlink ~/.af3 to group storage, or bind a different output directory.

If you're still stuck, contact HPC support with your job ID and the `.err` file.
