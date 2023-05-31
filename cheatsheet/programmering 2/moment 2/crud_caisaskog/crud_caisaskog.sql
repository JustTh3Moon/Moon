-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Värd: 127.0.0.1
-- Tid vid skapande: 13 feb 2023 kl 00:10
-- Serverversion: 10.4.25-MariaDB
-- PHP-version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Databas: `crud_caisaskog`
--

-- --------------------------------------------------------

--
-- Tabellstruktur `fiction`
--

CREATE TABLE `fiction` (
  `fiction_id` int(3) NOT NULL,
  `title` varchar(255) NOT NULL,
  `director` varchar(255) NOT NULL,
  `fiction_type` varchar(255) NOT NULL,
  `length` int(3) NOT NULL,
  `season` int(3) NOT NULL,
  `episodes` int(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumpning av Data i tabell `fiction`
--

INSERT INTO `fiction` (`fiction_id`, `title`, `director`, `fiction_type`, `length`, `season`, `episodes`) VALUES
(15, 'Saving Hope', 'ngn', 'serie', 0, 12, 12);

-- --------------------------------------------------------

--
-- Tabellstruktur `reviews`
--

CREATE TABLE `reviews` (
  `review_id` int(3) NOT NULL,
  `user_id` int(11) NOT NULL,
  `fiction_id` int(11) NOT NULL,
  `status` varchar(255) NOT NULL,
  `rating` int(3) NOT NULL,
  `comment` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Tabellstruktur `users`
--

CREATE TABLE `users` (
  `user_id` int(3) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `creation_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumpning av Data i tabell `users`
--

INSERT INTO `users` (`user_id`, `username`, `password`, `creation_date`) VALUES
(1, 'yoxenl', '123', '2023-02-11 13:24:12'),
(4, 'oliva', '123', '2023-02-12 19:45:23');

--
-- Index för dumpade tabeller
--

--
-- Index för tabell `fiction`
--
ALTER TABLE `fiction`
  ADD PRIMARY KEY (`fiction_id`);

--
-- Index för tabell `reviews`
--
ALTER TABLE `reviews`
  ADD PRIMARY KEY (`review_id`);

--
-- Index för tabell `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- AUTO_INCREMENT för dumpade tabeller
--

--
-- AUTO_INCREMENT för tabell `fiction`
--
ALTER TABLE `fiction`
  MODIFY `fiction_id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT för tabell `reviews`
--
ALTER TABLE `reviews`
  MODIFY `review_id` int(3) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT för tabell `users`
--
ALTER TABLE `users`
  MODIFY `user_id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
