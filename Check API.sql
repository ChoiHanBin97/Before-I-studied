
-- ���� ��Ȳ_���㰡
SELECT count(*) FROM gghosptlm;
select * from gghosptlm;
select licensg_cancl_de from gghosptlm;
select * from gghosptlm where licensg_cancl_de != '';

-- ��ȣ�� ��Ȳ(����ǥ��)
select COUNT(*) from Nurstree_1;
select * from Nurstree_1;
select * from NURSTREE_1 where TEMP != '';

-- �д�ó���ü� ��Ȳ
select COUNT(*) from openapigggokr_NigtsoilProcFaclt;
select * from openapigggokr_nigtsoilprocfaclt;

-- �ҹ� �������� �ܼ� ���� ��Ȳ
select COUNT(*) from openapigggokr_UnlawAdRegl;
select * from openapigggokr_UnlawAdRegl;

-- �������� �����ü� ��Ȳ
select COUNT(*) from openapigggokr_NonpointPollutionSurveillan;
select * from openapigggokr_NonpointPollutionSurveillan;
select * from openapigggokr_NonpointPollutionSurveillan where DO_EXPN != '';

-- ���� ������ü ��Ȳ_���㰡
select COUNT(*) from openapigggokr_PostnatalCare;
select * from openapigggokr_PostnatalCare;
select * from openapigggokr_PostnatalCare where LICENSG_CANCL_DE != '';


-- �ҹ桤�����������롤ġ�ȼ��� ��Ȳ
select COUNT(*) from openapigggokr_FiresttnPolcsttnM;
select * from openapigggokr_FiresttnPolcsttnM;

-- �ҹ漭 ��Ȳ �� ���ұ��� ����
select COUNT(*) from openapigggokr_GyeonggiFireStation;
select * from openapigggokr_GyeonggiFireStation;

-- �����ڿ� ��ȣ���� ���� ��Ȳ
select COUNT(*) from openapigggokr_WaterResourcesProtectionZone;
select * from openapigggokr_WaterResourcesProtectionZone;

-- ��⵵ �Ƶ� �޽� ����ī�� ������ ��Ȳ
select count(*) from openapigggokr_GDreamCard;
select * from openapigggokr_GDreamCard;

-- Ȯ��
select * from openapigggokr_GDreamCard group by REFINE_ROADNM_ADDR having COUNT(REFINE_ROADNM_ADDR);

