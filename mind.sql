
--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--


INSERT INTO `user` (`id`, `username`, `email`, `password`) VALUES
(1, 'sanyam', 'sanyamsankhala13@gmail.com', 'sanyam12345');

--
-- Indexes for dumped tables
--
--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;





CREATE TABLE `feedback` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `subject` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `message` varchar(700) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


INSERT INTO `feedback` (`id`,`name`, `subject`, `email`, `message`) VALUES
(1,'sanyam','Regaring Your Website','sanyamsankhala13@gmail.com', 'This website is fantastic! I rate it 5 out of 5.');

--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`id`);

--
--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `feedback`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;



COMMIT;