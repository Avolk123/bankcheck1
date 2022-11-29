-- phpMyAdmin SQL Dump
-- version 5.1.2
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 28, 2022 at 08:04 PM
-- Server version: 5.7.24
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `babki`
--

-- --------------------------------------------------------

--
-- Table structure for table `uptime_stat`
--

CREATE TABLE `uptime_stat` (
  `sberbank` int(11) NOT NULL,
  `alfabank` int(11) NOT NULL,
  `rgs` int(11) NOT NULL,
  `pochtabank` int(11) NOT NULL,
  `tinkoff` int(11) NOT NULL,
  `tochka` int(11) NOT NULL,
  `vtb` int(11) NOT NULL,
  `prostobank` int(11) NOT NULL,
  `mtsbank` int(11) NOT NULL,
  `uralsib` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
