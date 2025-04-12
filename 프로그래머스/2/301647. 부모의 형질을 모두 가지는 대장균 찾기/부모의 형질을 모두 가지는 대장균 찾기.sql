SELECT J.ID, J.GENOTYPE, P.genotype AS PARENT_GENOTYPE
FROM ECOLI_DATA AS J, ECOLI_DATA AS P
WHERE J.PARENT_ID = P.ID 
  AND (J.GENOTYPE & P.GENOTYPE = P.GENOTYPE)
ORDER BY J.ID ASC;