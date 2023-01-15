create table sportsman_copy as select  from sportsman
delete from sportsman_copy

DO $$
DECLARE
    sportsman_id int;
    sportsman_name varchar(50);
	country varchar(20);
BEGIN
    sportsman_id = 100;
    sportsman_name = 'sportsman';
	country = 'country';
    FOR counter IN 1..10
        LOOP
            INSERT INTO sportsman_copy(sportsman_id, sportsman_name, country)
            VALUES (counter + sportsman_id, sportsman_name  counter, country  counter);
        END LOOP;
END;
$$