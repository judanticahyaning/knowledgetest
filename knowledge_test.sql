-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 02, 2022 at 03:11 PM
-- Server version: 10.4.18-MariaDB
-- PHP Version: 7.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `knowledge_test`
--

-- --------------------------------------------------------

--
-- Table structure for table `film`
--

CREATE TABLE `film` (
  `id` int(11) NOT NULL,
  `title` varchar(500) NOT NULL,
  `genre` varchar(500) NOT NULL,
  `rating` varchar(500) NOT NULL,
  `duration` varchar(500) NOT NULL,
  `quality` varchar(500) NOT NULL,
  `trailer` varchar(500) NOT NULL,
  `watch` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `film`
--

INSERT INTO `film` (`id`, `title`, `genre`, `rating`, `duration`, `quality`, `trailer`, `watch`) VALUES
(28, 'After We Fell (2021)', 'Drama, Movie, Romance, France', '7.2', '99 min', 'HD', 'https://www.youtube.com/watch?v=NYdNN6C9hfI', 'https://103.136.42.202/after-we-fell-2021/'),
(29, 'The Bewailing (The Nest) (2021)', 'Horror, Movie, Thriller', '6', '100 min', 'HD', 'https://www.youtube.com/watch?v=92kRK9WLNtg', 'https://103.136.42.202/the-bewailing-the-nest-2021/'),
(30, 'Asakusa Kid (2021)', 'Drama, Movie', '7', '123 min', 'HD', 'https://www.youtube.com/watch?v=KhzBFfkvn44', 'https://103.136.42.202/asakusa-kid-2021/'),
(31, 'Hong Xiguan and Demon Gate Witch (2021)', 'Action, Drama, Movie', '', '89 min', 'HD', '', 'https://103.136.42.202/hong-xiguan-and-demon-gate-witch-2021/'),
(32, 'The Unforgivable (2021)', 'Drama, Movie, Thriller, United Kingdom', '7.7', '112 min', 'HD', 'https://www.youtube.com/watch?v=JNUjx7LZoiU', 'https://103.136.42.202/the-unforgivable-2021/'),
(33, 'Back to the Outback (2021)', 'Adventure, Animation, Comedy, Family, Movie', '7.9', '92 min', 'HD', 'https://www.youtube.com/watch?v=FzWyKSsdTCw', 'https://103.136.42.202/back-to-the-outback-2021/'),
(34, 'Anonymously Yours (AnAnima) (2021)', 'Drama, Movie, Romance', '8.3', '101 min', 'HD', '', 'https://103.136.42.202/anonymously-yours-ananima-2021/'),
(35, 'Two (Dos) (2021)', 'Horror, Movie, Thriller', '5.1', '71 min', 'HD', '', 'https://103.136.42.202/two-dos-2021/'),
(36, 'Encounter (2021)', 'Adventure, Movie, Sci-Fi, Thriller, United Kingdom', '6.4', '108 min', 'HD', 'https://www.youtube.com/watch?v=SB44bZVe-c4', 'https://103.136.42.202/encounter-2021/'),
(37, 'The Last Son (2021)', 'Action, Adventure, Drama, Movie, Western', '6.3', '96 min', 'HD', 'https://www.youtube.com/watch?v=KilcySbvmP8', 'https://103.136.42.202/the-last-son-2021/'),
(38, 'Night Night (2021)', 'Movie, Thriller', '6.6', '', 'HD', 'https://www.youtube.com/watch?v=ufo0QyegfPU', 'https://103.136.42.202/night-night-2021/'),
(39, 'American Refugee (2021)', 'Movie, Thriller', '7.2', '95 min', 'HD', 'https://www.youtube.com/watch?v=aGjReL9ByIA', 'https://103.136.42.202/american-refugee-2021/'),
(40, 'Snoopy Presents: For Auld Lang Syne (2021)', 'Animation, Family, Movie', '7.5', '40 min', 'HD', 'https://www.youtube.com/watch?v=feu3E6aSBvE', 'https://103.136.42.202/snoopy-presents-for-auld-lang-syne-2021/'),
(41, 'The Hating Game (2021)', 'Comedy, Movie, Romance', '7', '98 min', 'HD', 'https://www.youtube.com/watch?v=j3qBGOD4b4A', 'https://103.136.42.202/the-hating-game-2021/'),
(42, 'Resident Evil: Welcome to Raccoon City (2021)', 'Action, Horror, Movie, Sci-Fi, France, Germany, United Kingdom', '6.1', '107 min', 'CAM', 'https://www.youtube.com/watch?v=IQqqAWMIIAQ', 'https://103.136.42.202/resident-evil-welcome-to-raccoon-city-2021/'),
(43, 'Agnes (2021)', 'Drama, Horror, Movie', '4.5', '93 min', 'HD', 'https://www.youtube.com/watch?v=WEWQbBOFcz4', 'https://103.136.42.202/agnes-2021/'),
(44, 'Antlers (2021)', 'Drama, Horror, Misteri, Movie, Canada, Mexico', '6.4', '99 min', 'HD', 'https://www.youtube.com/watch?v=2aiYxwVuZ1o', 'https://103.136.42.202/antlers-2021/'),
(45, 'Spider-Man: No Way Home (2021)', 'Action, Adventure, Box Office, Fantasy, Sci-Fi', '8.6', '148 min', 'CAM', 'https://www.youtube.com/watch?v=UV2ZWTSHjSs', 'https://103.136.42.202/spider-man-no-way-home-2021/'),
(46, 'Clifford the Big Red Dog (2021)', 'Animation, Comedy, Family, Movie, Canada, United Kingdom', '7.5', '97 min', 'HD', 'https://www.youtube.com/watch?v=o9ri5DYLvkU', 'https://103.136.42.202/clifford-the-big-red-dog-2021/'),
(47, 'Night Raiders (2021)', 'Movie, Sci-Fi, Canada', '6', '97 min', 'HD', 'https://www.youtube.com/watch?v=Bg4B2smJPKU', 'https://103.136.42.202/night-raiders-2021/');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `film`
--
ALTER TABLE `film`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `film`
--
ALTER TABLE `film`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
