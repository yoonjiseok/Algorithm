-- 코드를 작성해주세요
select ID, fn.FISH_NAME, LENGTH
from FISH_INFO fi
join FISH_NAME_INFO fn
on fi.FISH_TYPE = fn.FISH_TYPE
where (fi.FISH_TYPE, LENGTH) in (select FISH_TYPE, MAX(LENGTH) from FISH_INFO group by FISH_TYPE)
