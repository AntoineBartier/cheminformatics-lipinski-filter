# Cheminformatics Lipinski Filter

A Python tool to evaluate molecules against Lipinski's Rule of 5 using RDKit.

## Overview

Lipinski's Rule of 5 is a rule of thumb to evaluate druglikeness, determining if a chemical compound with a certain pharmacological or biological activity has properties that would make it a likely orally active drug in humans. 

The rule states that an orally active drug has no more than one violation of the following criteria:
* Molecular Weight (MW) $\leq$ 500 Da
* Octanol-water partition coefficient ($\log P$) $\leq$ 5
* Number of Hydrogen Bond Donors (HBD) $\leq$ 5
* Number of Hydrogen Bond Acceptors (HBA) $\leq$ 10

## Installation

Clone this repository and install the required dependencies:

```bash
git clone [https://github.com/](https://github.com/)[TON_PSEUDO_GITHUB]/cheminformatics-lipinski-filter.git
cd cheminformatics-lipinski-filter
pip install -r requirements.txt
