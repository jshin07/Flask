
SELECT * FROM users
LEFT JOIN friendships ON ____=____
LEFT JOIN users as user2 ON ____ = ____


SELECT users.first_name, users.last_name,friendships.first_name,friend_last_name
FROM users
LEFT JOIN friendships ON users.id = friendships.user_id
LEFT JOIN users ON friendships.frienship_id = users2.id
