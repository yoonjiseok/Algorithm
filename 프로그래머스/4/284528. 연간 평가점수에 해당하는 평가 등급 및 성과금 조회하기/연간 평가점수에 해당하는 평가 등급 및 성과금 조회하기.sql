-- 코드를 작성해주세요
select he.EMP_NO, he.EMP_NAME, 
(CASE
WHEN AVG(hg.score) >= 96 then 'S'
WHEN AVG(hg.score) >= 90 then 'A'
WHEN AVG(hg.score) >= 80 then 'B'
ELSE 'C'
END) as GRADE,
(CASE
WHEN AVG(hg.score) >= 96 then he.SAL * 0.2
WHEN AVG(hg.score) >= 90 then he.SAL * 0.15
WHEN AVG(hg.score) >= 80 then he.SAL * 0.1
ELSE 0
END) as BONUS
from HR_EMPLOYEES he
join HR_DEPARTMENT hd
on he.DEPT_ID = hd.DEPT_ID
join HR_GRADE hg
on he.EMP_NO = hg.EMP_NO
group by he.EMP_NO
