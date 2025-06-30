-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Jun 30, 2025 at 01:09 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `portfolio`
--

-- --------------------------------------------------------

--
-- Table structure for table `blogs`
--

CREATE TABLE `blogs` (
  `id` int(11) NOT NULL,
  `published_at` datetime DEFAULT NULL,
  `link` text DEFAULT NULL,
  `author` varchar(100) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `created_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_date` date DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `blogs`
--

INSERT INTO `blogs` (`id`, `published_at`, `link`, `author`, `title`, `description`, `created_date`, `updated_date`, `created_by`, `updated_by`) VALUES
(1, NULL, '/blog-details', 'Admin', 'Support Vector Machines', 'Support Vector Machines are supervised learning models used for classification and regression tasks.', '2025-06-30 11:07:17', NULL, NULL, NULL),
(2, NULL, '/blog-details', 'Admin', 'Random Forest', 'Random Forest is a powerful machine learning algorithm used for both classification and regression tasks.', '2025-06-30 11:07:17', NULL, NULL, NULL),
(3, NULL, '/blog-details', 'Admin', 'Principal Component Analysis', 'Principal Component Analysis is an unsupervised dimensionality reduction technique.', '2025-06-30 11:09:19', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(150) DEFAULT NULL,
  `message` text DEFAULT NULL,
  `status` enum('pending','seen','responded') NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_date` date DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`id`, `name`, `email`, `message`, `status`, `created_date`, `updated_date`, `created_by`, `updated_by`) VALUES
(1, 'John Doe', 'jeremykurwa02@gmail.com', 'Hi, I\'m in need of your services', 'pending', '2025-06-27 21:00:00', NULL, NULL, NULL),
(2, 'Jane Doe', 'texdata.analytic@gmail.com', 'Hi, I\'m in need of your services', 'pending', '2025-06-27 21:00:00', NULL, NULL, NULL),
(4, 'Jere', 'jere@example.com', 'Message', 'pending', '2025-06-27 21:00:00', '2025-06-28', 0, 0),
(5, 'Jane Doe', 'johndoe@gmail.com', 'My message two', 'pending', '2025-06-27 21:00:00', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `interests`
--

CREATE TABLE `interests` (
  `id` int(11) NOT NULL,
  `icon_class` varchar(100) DEFAULT NULL,
  `title` varchar(100) NOT NULL,
  `description` text DEFAULT NULL,
  `created_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_date` date DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `interests`
--

INSERT INTO `interests` (`id`, `icon_class`, `title`, `description`, `created_date`, `updated_date`, `created_by`, `updated_by`) VALUES
(1, 'fa-book', 'Reading', 'I\'m passionate about learning through books and articles.', '2025-06-28 21:00:00', NULL, NULL, NULL),
(2, 'fa-code', 'Coding', 'I love creating software and solving real-world problems.', '2025-06-28 21:00:00', NULL, NULL, NULL),
(3, 'fa-music', 'Music', 'Music fuels my creativity and keeps me inspired.', '2025-06-28 21:00:00', NULL, NULL, NULL),
(4, 'fa-plane', 'Travel', 'Exploring new cultures broadens my perspective.', '2025-06-28 21:00:00', NULL, NULL, NULL),
(5, 'fa-camera', 'Phototgraphy', 'Capturing moments and visual storytelling is one of my passions.', '2025-06-28 21:00:00', NULL, NULL, NULL),
(6, 'fa-gamepad', 'Gaming', 'I enjoy immersive game worlds and competitive strategy games during leisure.', '2025-06-28 21:00:00', NULL, NULL, NULL),
(7, 'fa-hands-helping', 'Volunteering', 'Giving back to the community gives me purpose and joy.', '2025-06-28 21:00:00', NULL, NULL, NULL),
(8, 'fa-blog', 'Tech Blogging', 'I write about technology trends, tutorials, and coding tips.', '2025-06-28 21:00:00', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `projects`
--

CREATE TABLE `projects` (
  `id` int(11) NOT NULL,
  `image_number` enum('one','two') NOT NULL,
  `title` varchar(255) NOT NULL,
  `category` varchar(100) DEFAULT NULL,
  `link` text DEFAULT NULL,
  `image_link` text DEFAULT NULL,
  `created_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_date` date DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `projects`
--

INSERT INTO `projects` (`id`, `image_number`, `title`, `category`, `link`, `image_link`, `created_date`, `updated_date`, `created_by`, `updated_by`) VALUES
(1, 'one', 'Corporate Website', 'Web Development', 'https://imarika-ui.vercel.app', 'imarika', '2025-06-30 07:31:43', NULL, NULL, NULL),
(2, 'two', 'Corporate Website', 'Web Development', 'https://cipk-app.vercel.app', 'cipk', '2025-06-30 07:31:43', NULL, NULL, NULL),
(3, 'one', 'SMS Based Jobs App Wireframe', 'Designing, Wireframing', 'https://miro.com/app/board/uXjVIBfOL_4=/?share_link_id=861520531822', 'wireframe', '2025-06-30 07:31:43', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `resumes`
--

CREATE TABLE `resumes` (
  `id` int(11) NOT NULL,
  `start_year` varchar(15) DEFAULT NULL,
  `completion_year` varchar(15) DEFAULT NULL,
  `title` varchar(255) NOT NULL,
  `school` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `created_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_date` date DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `resumes`
--

INSERT INTO `resumes` (`id`, `start_year`, `completion_year`, `title`, `school`, `description`, `created_date`, `updated_date`, `created_by`, `updated_by`) VALUES
(1, '2018', '2023', 'Bsc in Statistics', 'Taita Taveta University', 'Graduated with a bachelor\'s degree in statistics.\nThese are some of the units covered in this period:\n\n1. Calculus,\n2. Parametric and Non-parametric Methods,\n3. Time Series Analysis,\n4. Demographic Techniques,\n5. Epidemiology,\n6. Stochastic Processes,\n7. Survival Analysis,\n8. Experimental Design Analysis,\n9. Bayesian Inference,\n10. Statistical Quality Control Methods,\n11. Probability and Statistics,\n...and more.', '2025-06-29 11:12:55', NULL, NULL, NULL),
(2, '2022', '2023', 'Full-Stack Web Development Bootcamp', 'Udemy', 'Completed a comprehensive course on full-stack web development, covering both front-end and back-end technologies:\n1. HTML and CSS,\n2. JavaScript, jQuery,\n3. Node.js, Express.js, APIs,\n4. PostgreSQL,\n5. React.js,\n6. Web design and deployment,\n7. Web3 and Blockchain,\n8. Token contract development,\n9. NFT minting, buying and selling logic.', '2025-06-29 11:12:55', NULL, NULL, NULL),
(3, '2025', 'Ongoing', 'Software Engineering', 'PLP Academy', 'The topics and skills covered were:\n1. Python Programming,\n2. Database Design and Programming with SQL,\n3. Startup Building for Developers,\n4. Software Engineering,\n5. Web Development V2,\n6. Ethics in Artificial Intelligence.', '2025-06-29 11:12:55', NULL, NULL, NULL),
(4, '2025', 'Ongoing', 'Data Science', 'ALX Africa', 'The topics and skills covered included the following:\n1. Self Awareness,\n2. Teamwork and Leadership,\n3. Communication and Quantitative Reasoning,\n4. Entrepreneurial Thinking,\n5. Critical Thinking,\n6. Task Management,\n7. Technical Skills.', '2025-06-29 11:12:55', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `services`
--

CREATE TABLE `services` (
  `id` int(11) NOT NULL,
  `category` varchar(100) DEFAULT NULL,
  `icon` varchar(100) DEFAULT NULL,
  `title` varchar(255) NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_date` date DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `services`
--

INSERT INTO `services` (`id`, `category`, `icon`, `title`, `created_date`, `updated_date`, `created_by`, `updated_by`) VALUES
(2, 'top', 'flaticon-analysis', 'Responsive Design', '2025-06-29 19:12:56', NULL, NULL, NULL),
(3, 'top', 'flaticon-flasks', 'Data Analysis', '2025-06-29 19:12:56', NULL, NULL, NULL),
(4, 'top', 'flaticon-ideas', 'Web Development, Hosting and Maintenance', '2025-06-29 19:12:56', NULL, NULL, NULL),
(5, 'bottom', 'flaticon-analysis', 'Software Development', '2025-06-29 19:12:56', NULL, NULL, NULL),
(6, 'bottom', 'flaticon-flasks', 'Machine Learning', '2025-06-29 19:12:56', NULL, NULL, NULL),
(7, 'bottom', 'flaticon-ideas', 'Consultation', '2025-06-29 19:12:56', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `skills`
--

CREATE TABLE `skills` (
  `id` int(11) NOT NULL,
  `icon_class` varchar(100) DEFAULT NULL,
  `title` varchar(100) NOT NULL,
  `created_date` timestamp NOT NULL DEFAULT current_timestamp(),
  `updated_date` date DEFAULT NULL,
  `created_by` int(11) DEFAULT NULL,
  `updated_by` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `skills`
--

INSERT INTO `skills` (`id`, `icon_class`, `title`, `created_date`, `updated_date`, `created_by`, `updated_by`) VALUES
(1, 'fab fa-python', 'Python', '2025-06-28 14:59:23', NULL, NULL, NULL),
(5, 'fab fa-r-project', 'R programming', '2025-06-28 15:00:38', NULL, NULL, NULL),
(8, 'fab fa-php', 'PHP', '2025-06-28 15:16:38', NULL, NULL, NULL),
(9, 'fab fa-js', 'JavaScript', '2025-06-28 15:16:46', NULL, NULL, NULL),
(11, 'fab fa-git-alt', 'Git', '2025-06-28 15:18:05', NULL, NULL, NULL),
(15, 'fas fa-pencil-ruler', 'UI/UX Design', '2025-06-28 15:19:52', NULL, NULL, NULL),
(17, 'fas fa-calculator', 'Quantitative Reasoning', '2025-06-28 17:42:07', NULL, NULL, NULL),
(19, 'fas fa-brain', 'Critical Thinking', '2025-06-28 17:44:57', NULL, NULL, NULL),
(20, 'fas fa-chart-line', 'Analytical Skills', '2025-06-28 17:44:57', NULL, NULL, NULL),
(21, 'fas fa-tasks', 'Task Management', '2025-06-28 17:44:57', NULL, NULL, NULL),
(22, 'fas fa-users', 'Teamwork', '2025-06-28 17:44:57', NULL, NULL, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blogs`
--
ALTER TABLE `blogs`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_blogs_id` (`id`);

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_contacts_id` (`id`);

--
-- Indexes for table `interests`
--
ALTER TABLE `interests`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_interests_id` (`id`);

--
-- Indexes for table `projects`
--
ALTER TABLE `projects`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_projects_id` (`id`);

--
-- Indexes for table `resumes`
--
ALTER TABLE `resumes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_resumes_id` (`id`);

--
-- Indexes for table `services`
--
ALTER TABLE `services`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_services_id` (`id`);

--
-- Indexes for table `skills`
--
ALTER TABLE `skills`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_skills_id` (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `blogs`
--
ALTER TABLE `blogs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `interests`
--
ALTER TABLE `interests`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `projects`
--
ALTER TABLE `projects`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `resumes`
--
ALTER TABLE `resumes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `services`
--
ALTER TABLE `services`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `skills`
--
ALTER TABLE `skills`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
