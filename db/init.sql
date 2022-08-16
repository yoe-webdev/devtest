-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 09, 2018 at 05:51 AM
-- Server version: 5.7.14
-- PHP Version: 7.0.10

-- SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
-- SET time_zone = "+00:00";

--
-- Database: `crud`
--

-- --------------------------------------------------------

--
-- Table structure for table `students`
--
CREATE DATABASE crud;
USE crud;

CREATE TABLE records (
  id int(11) NOT NULL AUTO_INCREMENT,
  elevator_id INT NOT NULL DEFAULT 0 CHECK(elevator_id > 0),
  number_of_floors INT NOT NULL DEFAULT 0 CHECK(number_of_floors > 0),
  current_floor INT NOT NULL DEFAULT 0 CHECK(current_floor > 0),
  capacity INT NOT NULL DEFAULT 0 CHECK(capacity > 0),
  occupancy INT NOT NULL DEFAULT 0 CHECK(occupancy > 0),
  is_moving BOOLEAN DEFAULT 1 CHECK(is_moving = true OR is_moving = false),
  next_stop_floor INT NOT NULL DEFAULT 0 CHECK(next_stop_floor > 0),
  resting_floor INT NOT NULL DEFAULT 0 CHECK(resting_floor > 0),
  PRIMARY KEY (id)
)ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `records`
--

INSERT INTO records (elevator_id, number_of_floors, current_floor, capacity, occupancy, is_moving, next_stop_floor, resting_floor) VALUES
(2, 16, 13, 2, 4, 1, 12, 20),
(12, 16, 13, 2, 14, 1, 21, 14),
(4, 42, 24, 14, 30, 0, 24, 15);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `records`
--

--
-- AUTO_INCREMENT for dumped tables
--

-- --
-- -- AUTO_INCREMENT for table `records`
-- --
-- ALTER TABLE `records`
--   MODIFY id int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
-- /*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
-- /*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
-- /*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
