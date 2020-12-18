
-- 병원 현황_인허가
SELECT count(*) FROM gghosptlm;
select * from gghosptlm;
select licensg_cancl_de from gghosptlm;
select * from gghosptlm where licensg_cancl_de != '';

-- 보호수 현황(개방표준)
select COUNT(*) from Nurstree_1;
select * from Nurstree_1;
select * from NURSTREE_1 where TEMP != '';

-- 분뇨처리시설 현황
select COUNT(*) from openapigggokr_NigtsoilProcFaclt;
select * from openapigggokr_nigtsoilprocfaclt;

-- 불법 유동광고물 단속 집계 현황
select COUNT(*) from openapigggokr_UnlawAdRegl;
select * from openapigggokr_UnlawAdRegl;

-- 비점오염 저감시설 현황
select COUNT(*) from openapigggokr_NonpointPollutionSurveillan;
select * from openapigggokr_NonpointPollutionSurveillan;
select * from openapigggokr_NonpointPollutionSurveillan where DO_EXPN != '';

-- 산후 조리업체 현황_인허가
select COUNT(*) from openapigggokr_PostnatalCare;
select * from openapigggokr_PostnatalCare;
select * from openapigggokr_PostnatalCare where LICENSG_CANCL_DE != '';


-- 소방·경찰·지구대·치안센터 현황
select COUNT(*) from openapigggokr_FiresttnPolcsttnM;
select * from openapigggokr_FiresttnPolcsttnM;

-- 소방서 현황 및 관할구역 정보
select COUNT(*) from openapigggokr_GyeonggiFireStation;
select * from openapigggokr_GyeonggiFireStation;

-- 수산자원 보호구역 관리 현황
select COUNT(*) from openapigggokr_WaterResourcesProtectionZone;
select * from openapigggokr_WaterResourcesProtectionZone;

-- 경기도 아동 급식 전자카드 가맹점 현황
select count(*) from openapigggokr_GDreamCard;
select * from openapigggokr_GDreamCard;

-- 확인
select * from openapigggokr_GDreamCard group by REFINE_ROADNM_ADDR having COUNT(REFINE_ROADNM_ADDR);

