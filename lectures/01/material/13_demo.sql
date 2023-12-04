
-- why is this not working with POSTGRES? (will lead to a syntax error) 
-- aks copilot!

DELETE
FROM
    datastream d
    LEFT JOIN digital_object dig_obj ON d.digital_object_id = dig_obj.id
    LEFT JOIN project cur_proj ON cur_proj.project_abbr = dig_obj.project_project_abbr
WHERE
    cur_proj.project_abbr = 'demo'