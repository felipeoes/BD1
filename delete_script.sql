DELETE FROM account_emailaddress WHERE user_id != 1;
DELETE FROM authtoken_token WHERE user_id != 1;
DELETE FROM users_usuario WHERE id != 1;