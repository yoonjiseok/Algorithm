-- 코드를 작성해주세요
select et.ID from
ECOLI_DATA ed
join ECOLI_DATA ea
on ed.ID = ea.PARENT_ID
join ECOLI_DATA et
on ea.ID = et.PARENT_ID
where ed.PARENT_ID is NULL