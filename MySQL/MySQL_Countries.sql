#1. What query would you run to get all the customers inside city_id = 312? Your query should returm customer first name, last name, email, and address.
SELECT city.city_id, city.city, customer.first_name, customer.last_name, customer.email, CONCAT(" ",address.address, address.address2, " " , city.city)
FROM city
JOIN address ON city.city_id = address.city_id
JOIN customer ON address.address_id = customer.address_id
WHERE city.city_id = 312;


##### ONLY HAVE ONE QUERY ON COMEDY????!!
#2. What query would you run to get all comedy films? Your query would return film title, description, release year, rating, special features and genre.
SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS genre
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.film_id= category.category_id;


# 3. What query would you run to get all the films joined by actor_id=5? Your query shoud return the film title, description and release year.
SELECT actor.actor_id, CONCAT(' ' , actor.first_name, actor.last_name), film_actor.film_id, film.title, film.description, film.release_year
FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film_actor.film_id= film.film_id
WHERE actor.actor_id =5;

#4  What query would you run to get all the customers in store_id = 1 and inside these cities (1, 42, 312 and 459)? Your query should return customer first name, last name, email, and address.
SELECT store.sotre_id, city.city_id, customer.first_name, customer.last_name, customer.email, address.adress
FROM customer
JOIN address ON customer.customer_id = addres.addres_id
JOIN city ON address.address_id= city.city_id
WHERE customer.store_id=1 and city.city_id IN (1, 42, 312, 459);





#5 What query would you run to get all the films with a rating = G and special feature = behind the scenes, joined by actor_id = 15? Your query shoud return the film title, description, release year, rate and special feature.
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, actor.actor_id
FROM film
JOIN film_actor ON film.film_id= film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
WHERE rating ="G" and actor.actor_id =15 and film.special_features LIKE "%behind the scene%";

#6. What query would you run to get all the actors that joined in the film_id = 369? Your query should return the first_name, last name and last_update of the actors
SELECT film.film_id, film.title, actor.actor_id, CONCAT(" ", actor.first_name, actor.last_name) AS actor_name
FROM film
JOIN film_actor ON film.film_id= film_actor.film_id
JOIN actor ON film_actor.actor_id= actor.actor_id
WHERE film.film_id = "369";

#7. What query would you run to get all drama films with a rental rate of 2.99 ? Your query should return film title, description, release year, rating, special features and genre.
SELECT film.film_id, film.title, film.description, film.release_year, film.rating, film.special_features, category.name AS 'genre', film.rental_rate
FROM film
JOIN film_category ON film.film_id = film_category.film_id
JOIN category ON film_category.category_id
WHERE category.name = "Drama" and film.rental_rate = "2.99";


#8






