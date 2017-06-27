INSERT INTO users ('first_name', 'last_name', 'phone_number','email_address')
VALUES ('Jenny', 'Shin','1234567','jenny@example.com');

INSERT INTO users ('first_name', 'last_name', 'phone_number','email_address')
VALUES ('Grant', 'Chong','123456','grant@example.com');

UPDATE users SET first_name = 'Leah', last_name='Chong' WHERE id = '2';

DELETE FROM first_name
WHERE id = 2;
