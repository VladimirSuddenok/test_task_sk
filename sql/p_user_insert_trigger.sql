CREATE FUNCTION insert_fio() RETURNS trigger AS $$
DECLARE 
	space varchar := ' ';
BEGIN
        NEW.fio := CONCAT(NEW.surname, space, NEW.firstname, space, NEW.middlename);
        RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER p_user_insert_trigger BEFORE INSERT ON p_user
    FOR EACH ROW EXECUTE PROCEDURE insert_fio();
