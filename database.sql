CREATE TABLE `users` (
  `id` integer PRIMARY KEY,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) UNIQUE NOT NULL,
  `phone_number` varchar(255) UNIQUE NOT NULL,
  `created_at` timestamp NOT NULL
);

CREATE TABLE `sim_cards` (
  `sim_number` varchar(255) PRIMARY KEY,
  `phone_number` varchar(255) UNIQUE NOT NULL,
  `status` varchar(255) NOT NULL DEFAULT 'inactive',
  `activation_date` timestamp,
  `user_id` integer NOT NULL
);

ALTER TABLE `sim_cards` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
