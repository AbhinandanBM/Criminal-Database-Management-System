-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 23, 2022 at 10:19 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `criminal_database`
--

-- --------------------------------------------------------

--
-- Table structure for table `criminal`
--

CREATE TABLE `criminal` (
  `crmnl_id` int(20) NOT NULL,
  `crmnl_name` varchar(50) NOT NULL,
  `crmnl_gender` varchar(50) NOT NULL,
  `crm_date` date NOT NULL,
  `crm_type` varchar(50) NOT NULL,
  `crmnl_phno` bigint(20) NOT NULL,
  `crmnl_addr` varchar(50) NOT NULL,
  `fir_id` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `criminal`
--

INSERT INTO `criminal` (`crmnl_id`, `crmnl_name`, `crmnl_gender`, `crm_date`, `crm_type`, `crmnl_phno`, `crmnl_addr`, `fir_id`) VALUES
(401, 'John', 'Male', '1992-05-08', 'Robery', 9876543210, 'Mumbai', 2);

-- --------------------------------------------------------

--
-- Table structure for table `fir`
--

CREATE TABLE `fir` (
  `fir_id` int(20) NOT NULL,
  `fir_date` date NOT NULL,
  `stat_id` int(20) NOT NULL,
  `vict_name` varchar(50) NOT NULL,
  `fir_desc` mediumtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `fir`
--

INSERT INTO `fir` (`fir_id`, `fir_date`, `stat_id`, `vict_name`, `fir_desc`) VALUES
(1, '2022-01-14', 201, 'john', 'John roberred the bag that contains a 25kg of gold.');

-- --------------------------------------------------------

--
-- Table structure for table `police`
--

CREATE TABLE `police` (
  `email` varchar(50) NOT NULL,
  `pol_id` int(20) NOT NULL,
  `pol_name` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `pol_dob` date NOT NULL,
  `designation` varchar(50) NOT NULL,
  `pol_phno` bigint(20) NOT NULL,
  `pol_addr` varchar(50) NOT NULL,
  `stat_id` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `police`
--

INSERT INTO `police` (`email`, `pol_id`, `pol_name`, `gender`, `pol_dob`, `designation`, `pol_phno`, `pol_addr`, `stat_id`) VALUES
('bmabhi13@gmail.com', 101, 'Abhinandan', 'Male', '2001-08-13', 'Inspector General of Police', 9353843966, 'Bidadi', 201),
('bmabhi13@gmail.com', 102, 'suma', 'Female', '2004-08-02', 'Deputy Inspector General of Police', 9353553747, 'Mumbai', 203),
('bmabhi13@gmail.com', 103, 'Abhishek', 'Male', '2001-11-28', 'Superintendent of Police', 9435671250, 'Gowribedunuru', 204),
('bmabhi13@gmail.com', 104, 'Ramesh', 'Male', '1996-06-08', 'Deputy Inspector General of Police', 9900887654, 'Delhi', 0),
('bmabhi13@gmail.com', 1234, 'afdef', 'Male', '2022-01-05', 'Deputy Inspector General of Police', 87878787878, 'Bidadi', 0);

-- --------------------------------------------------------

--
-- Table structure for table `station`
--

CREATE TABLE `station` (
  `stat_id` int(20) NOT NULL,
  `stat_name` varchar(50) NOT NULL,
  `stat_phno` bigint(20) NOT NULL,
  `stat_city` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `station`
--

INSERT INTO `station` (`stat_id`, `stat_name`, `stat_phno`, `stat_city`) VALUES
(1, 'john', 87878787878787, 'haja'),
(201, 'Hoyshala', 1234567890, 'Bangalore'),
(202, 'Rajahuli', 2345698710, 'Bangalore');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `email`, `password`) VALUES
(1, 'abhinandan', 'bmabhi13@gmail.com', 'pbkdf2:sha256:260000$jnvOLjSoWNW2NCFV$6e65a3ea99c68b8ba5daa2094a1c385e03d34cdaf9805db41e5669002f91e347'),
(7, 'abcd', 'abcd@gmail.com', 'pbkdf2:sha256:260000$wOQNY2QOSqCFmccw$7aed420c897f841533d4d754559c761b638232e04f97629c8640f0e290b737e6');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `criminal`
--
ALTER TABLE `criminal`
  ADD PRIMARY KEY (`crmnl_id`);

--
-- Indexes for table `fir`
--
ALTER TABLE `fir`
  ADD PRIMARY KEY (`fir_id`);

--
-- Indexes for table `police`
--
ALTER TABLE `police`
  ADD PRIMARY KEY (`pol_id`);

--
-- Indexes for table `station`
--
ALTER TABLE `station`
  ADD PRIMARY KEY (`stat_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
