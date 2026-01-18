

create_demographics_table = (
    """
    CREATE TABLE IF NOT EXSISTS demographics_table(
    demographics_id SERIAL CONSTRAINT demographics_pk PRIMARY KEY,
    country VARCHAR NOT NULL,
    city VARCHART NOT NULL,
    age INT NOT NULL, 
    marriage_status BOOLEAN, 
    employment_id BOOLEAN REFERENCES employment (employment_id)
    )
    """
)

create_employment_table = (
    """
    CREATE TABLE IF NOT EXISTS employment(
    employment_id SERIAL CONSTRAINT employment_pk PRIMARY KEY, 
    work_length INT NOT NULL,
    workplace_city VARCHAR NOT NULL,
    workplace_country VARCHAR NOT NULL,
    
    )
    """
)