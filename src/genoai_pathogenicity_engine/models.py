from pydantic import BaseModel
from typing import Optional


class VariantInput(BaseModel):
    """
    Defines the strict structure for a single variant input to the API.
    Most fields are now mandatory to ensure a complete analysis.
    """
    # === Core Identifiers & Annotations ===
    variant_id: str
    Consequence: str
    ZYG: str
    IMPACT: str
    genename: str
    rs_dbSNP: Optional[str] = None # Can be optional

    # === Frequency Data ===
    gnomADe_AF: float
    gnomADg_AF: float
    AF: float
    MAX_AF: float

    # === Clinical & Publication Data ===
    CLIN_SIG: str
    clinvar_review: str
    PUBMED: Optional[str] = None # Can be optional
    clinvar_OMIM_id: Optional[str] = None
    clinvar_MedGen_id: Optional[str] = None
    clinvar_Orphanet_id: Optional[str] = None
    clinvar_clnsig: str
    clinvar_hgvs: str
    clinvar_id: str
    clinvar_trait: str
    clinvar_var_source: str
    GENE_PHENO: str
    
    # === In-silico Predictor Scores (Numeric) ===
    CADD_PHRED: float
    CADD_RAW: float
    REVEL: float
    DANN_score: float
    Eigen_phred_coding: float
    GenoCanyon_score: float
    PrimateAI_score: float
    PrimateAI: float
    am_pathogenicity: float
    BayesDel_noAF_pred: float
    ClinPred_pred: float
    DEOGEN2_pred: float
    
    # === In-silico Predictor Scores (String Predictions) ===
    SIFT: str
    SIFT_pred: str
    PolyPhen: str
    Polyphen2_HVAR_pred: str
    FATHMM_pred: str
    fathmm_MKL_coding_pred: str
    LRT_pred: str
    M_CAP_pred: str
    MetaLR_pred: str
    MetaSVM_pred: str
    MutationAssessor_pred: str
    MutationTaster_pred: str
    PROVEAN_pred: str
    am_class: str

    # === Conservation Scores ===
    GERP_RS: float
    GERP__RS: Optional[float] = None 
    phastCons100way_vertebrate: float
    phyloP100way_vertebrate: float
    SiPhy_29way_logOdds: float

    # === Splice Predictors ===
    MaxEntScan_diff: float
    SpliceAI_pred: float
    SpliceVault_SpliceAI_delta: float
    SpliceVault_site_max_depth: float
    SpliceVault_site_sample_count: float
    SpliceVault_site_pos: float
    SpliceVault_out_of_frame_events: str
    SpliceVault_site_type: str
    SpliceVault_top_events: str

    # === LoF Metrics ===
    LoF: str
    LoF_filter: str
    LoF_flags: str
    LoF_info: str

    # === Gene Intolerance & Constraint Metrics ===
    lof_pLI: float
    lof_pNull: float
    lof_obs: float
    lof_exp: float
    lof_oe: float
    lof_z_score: float
    lof_oe_ci_lower: float
    lof_oe_ci_upper: float
    mis_obs: float
    mis_exp: float
    mis_oe: float
    mis_z_score: float
    mis_oe_ci_lower: float
    mis_oe_ci_upper: float
    mis_pphen_obs: float
    mis_pphen_exp: float
    mis_pphen_oe: float
    mis_pphen_z_score: float

    # === Other Domain/Protein info ===
    DOMAINS: str