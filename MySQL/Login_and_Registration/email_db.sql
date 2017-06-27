#SELECT * FROM users;

#SELECT users.first_name, users.last_name, user_id, messages.message, messages.created_at FROM users JOIN messages ON users.id= messages.user_id;

#SELECT users.first_name, users.last_name, comments.comment, comments.created_at FROM users JOIN comments ON users.id= comments.user_id

SELECT * FROM users;



#DELETE FROM messages WHERE user_id =28

#INSERT INTO messages(message, created_at, updated_at, user_id) VALUES ("so hard!!!", NOW(), NOW(), 3)
#SELECT * FROM comments
INSERT INTO comments(comment, created_at, updated_at, user_id) 
VALUES ("???!!!", NOW(), NOW(), 3)





INSERT INTO messages(message, created_at, updated_at, user_id) 
SELECT comment, created_at, updated_at FROM comments
WHERE message_id=1;

SELECT * FROM users;

SELECT * FROM comments;