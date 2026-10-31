-- Write your query below
select name, COALESCE(SUM(rides.distance), 0) as travelled_distance
from users
left join rides
    on users.id = rides.user_id
group by users.name
ORDER BY travelled_distance DESC, users.name ASC;