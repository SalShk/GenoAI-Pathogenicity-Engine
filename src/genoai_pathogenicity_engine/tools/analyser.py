# src/genoai_pathogenicity_engine/tools/analyser.py

from typing import List
import pandas as pd
import numpy as np
import re

from ..models import VariantInput
from ..engine import analyze_variants

ALIAS_MAP = {
    "variant_id": ["variant_id", "Location", "ID"],
    "Consequence": ["Consequence", "Annotation", "Variant_Class"],
    "REVEL": ["REVEL", "Revel_score", "revel"],
    "CADD_PHRED": ["CADD_PHRED", "CADD_phred", "CADD"],
    "CLIN_SIG": ["CLIN_SIG", "ClinVar_Significance", "clinvar_sig"],
}

def parse_and_standardize_variant_id(raw_id: any) -> str:
    if not isinstance(raw_id, str):
        return "unknown_variant"
    standard_id = raw_id.replace(":", "-").replace("_", "-").strip()
    match = re.match(r'^(chr)?(\w+)-(\d+)(?:-([ACGTN]+))?(?:-([ACGTN]+))?', standard_id, re.IGNORECASE)
    if match:
        chrom_num = match.group(2).lower().replace('chr', '')
        pos = match.group(3)
        ref = match.group(4) if match.group(4) else 'N'
        alt = match.group(5) if match.group(5) else 'N'
        return f"chr{chrom_num}-{pos}-{ref}-{alt}"
    return standard_id

def normalize_variant_data(raw_variants: List[dict]) -> List[dict]:
    normalized_list = []
    for raw_variant in raw_variants:
        normalized_variant = {}
        for standard_name, aliases in ALIAS_MAP.items():
            for alias in aliases:
                if alias in raw_variant:
                    normalized_variant[standard_name] = raw_variant[alias]
                    break
        for key, value in raw_variant.items():
            is_an_alias = any(key in alias_list for alias_list in ALIAS_MAP.values())
            if key not in normalized_variant and not is_an_alias:
                normalized_variant[key] = value
        if "variant_id" in normalized_variant:
            normalized_variant["variant_id"] = parse_and_standardize_variant_id(normalized_variant["variant_id"])
        normalized_list.append(normalized_variant)
    return normalized_list

def run_genoai_analysis(variants: List[dict]) -> List[dict]:
    if not variants:
        return {"error": "Input variant list cannot be empty."}

    normalized_data = normalize_variant_data(variants)

    try:
        validated_variants = [VariantInput(**data) for data in normalized_data]
    except Exception as e:
        return {"error": f"Data validation error: {e}"}

    input_df = pd.DataFrame([v.dict() for v in validated_variants])

    all_expected_columns = [
        'variant_id', 'Consequence', 'ZYG', 'IMPACT', 'gnomADe_AF', 'gnomADg_AF', 'AF', 'MAX_AF',
        'CLIN_SIG', 'clinvar_review', 'PUBMED', 'SIFT', 'PolyPhen', 'CADD_PHRED', 'REVEL', 'LoF', 
        'LoF_filter', 'LoF_flags', 'LoF_info', 'DANN_score', 'Eigen-phred_coding', 'FATHMM_pred', 
        'GERP++_RS', 'GenoCanyon_score', 'LRT_pred', 'M-CAP_pred', 'MetaLR_pred', 'MetaSVM_pred', 
        'MutationAssessor_pred', 'MutationTaster_pred', 'PROVEAN_pred', 'Polyphen2_HVAR_pred', 
        'PrimateAI_score', 'SIFT_pred', 'SiPhy_29way_logOdds', 'phastCons100way_vertebrate', 
        'phyloP100way_vertebrate', 'MaxEntScan_diff', 'lof.pLI', 'lof.pNull', 'lof.obs', 'lof.exp', 
        'lof.oe', 'lof.z_score', 'lof.oe_ci.lower', 'lof.oe_ci.upper', 'mis.obs', 'mis.exp', 
        'mis.oe', 'mis.z_score', 'mis_pphen.obs', 'mis_pphen.exp', 'mis_pphen.oe', 
        'mis_pphen.z_score', 'mis.oe_ci.lower', 'mis.oe_ci.upper', 'clinvar_OMIM_id', 
        'clinvar_MedGen_id', 'clinvar_Orphanet_id', 'clinvar_clnsig', 'clinvar_hgvs', 
        'clinvar_id', 'clinvar_trait', 'clinvar_var_source', 'fathmm-MKL_coding_pred', 'genename', 
        'rs_dbSNP', 'am_class', 'am_pathogenicity', 'PrimateAI', 'SpliceAI_pred', 
        'SpliceVault_SpliceAI_delta', 'SpliceVault_out_of_frame_events', 'SpliceVault_site_max_depth', 
        'SpliceVault_site_pos', 'SpliceVault_site_sample_count', 'SpliceVault_site_type', 
        'SpliceVault_top_events', 'CADD_RAW', 'GENE_PHENO', 'DOMAINS', 'GERP_RS', 'GERP__RS'
    ]

    full_df = input_df.reindex(columns=all_expected_columns)
    results_df = analyze_variants(full_df)

    if results_df is None:
        return {"error": "Variant analysis failed."}

    results_df = results_df.replace({np.nan: None})
    return results_df.to_dict(orient="records")