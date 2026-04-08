SELECT 
    A.ID, 
    B.FISH_NAME, 
    A.LENGTH
FROM 
    FISH_INFO A
JOIN 
    FISH_NAME_INFO B ON A.FISH_TYPE = B.FISH_TYPE
WHERE (a.fish_type, a.length) in (select fish_type, max(length)
                          from FISH_INFO
                          group by fish_type)
order by A.id