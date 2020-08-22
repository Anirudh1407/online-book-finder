-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 12, 2020 at 08:36 PM
-- Server version: 8.0.19
-- PHP Version: 7.2.24-0ubuntu0.18.04.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `BOOKFINDER1`
--

-- --------------------------------------------------------

--
-- Table structure for table `admins_adminparent`
--

CREATE TABLE `admins_adminparent` (
  `created_id` int NOT NULL,
  `creator_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `admins_adminreason`
--

CREATE TABLE `admins_adminreason` (
  `id` int NOT NULL,
  `reason` longtext NOT NULL,
  `bannedadmin_id` int DEFAULT NULL,
  `banneduser_id` int DEFAULT NULL,
  `reportedadmin_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `admins_adminrequest`
--

CREATE TABLE `admins_adminrequest` (
  `user_id` int NOT NULL,
  `assigned_to_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `admins_bannedadmin`
--

CREATE TABLE `admins_bannedadmin` (
  `user_id` int NOT NULL,
  `rejection_date` datetime(6) NOT NULL,
  `assigned_admin_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `admins_rejectedadmin`
--

CREATE TABLE `admins_rejectedadmin` (
  `user_id` int NOT NULL,
  `rejection_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `admins_reportedadmin`
--

CREATE TABLE `admins_reportedadmin` (
  `admin_id` int NOT NULL,
  `comment` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add book', 1, 'add_book'),
(2, 'Can change book', 1, 'change_book'),
(3, 'Can delete book', 1, 'delete_book'),
(4, 'Can view book', 1, 'view_book'),
(5, 'Can add tag', 2, 'add_tag'),
(6, 'Can change tag', 2, 'change_tag'),
(7, 'Can delete tag', 2, 'delete_tag'),
(8, 'Can view tag', 2, 'view_tag'),
(9, 'Can add delete book request', 3, 'add_deletebookrequest'),
(10, 'Can change delete book request', 3, 'change_deletebookrequest'),
(11, 'Can delete delete book request', 3, 'delete_deletebookrequest'),
(12, 'Can view delete book request', 3, 'view_deletebookrequest'),
(13, 'Can add book image', 4, 'add_bookimage'),
(14, 'Can change book image', 4, 'change_bookimage'),
(15, 'Can delete book image', 4, 'delete_bookimage'),
(16, 'Can view book image', 4, 'view_bookimage'),
(17, 'Can add author', 5, 'add_author'),
(18, 'Can change author', 5, 'change_author'),
(19, 'Can delete author', 5, 'delete_author'),
(20, 'Can view author', 5, 'view_author'),
(21, 'Can add banned user', 6, 'add_banneduser'),
(22, 'Can change banned user', 6, 'change_banneduser'),
(23, 'Can delete banned user', 6, 'delete_banneduser'),
(24, 'Can view banned user', 6, 'view_banneduser'),
(25, 'Can add reported user', 7, 'add_reporteduser'),
(26, 'Can change reported user', 7, 'change_reporteduser'),
(27, 'Can delete reported user', 7, 'delete_reporteduser'),
(28, 'Can view reported user', 7, 'view_reporteduser'),
(29, 'Can add user profile', 8, 'add_userprofile'),
(30, 'Can change user profile', 8, 'change_userprofile'),
(31, 'Can delete user profile', 8, 'delete_userprofile'),
(32, 'Can view user profile', 8, 'view_userprofile'),
(33, 'Can add user reason', 9, 'add_userreason'),
(34, 'Can change user reason', 9, 'change_userreason'),
(35, 'Can delete user reason', 9, 'delete_userreason'),
(36, 'Can view user reason', 9, 'view_userreason'),
(37, 'Can add issue', 10, 'add_issue'),
(38, 'Can change issue', 10, 'change_issue'),
(39, 'Can delete issue', 10, 'delete_issue'),
(40, 'Can view issue', 10, 'view_issue'),
(41, 'Can add change', 11, 'add_change'),
(42, 'Can change change', 11, 'change_change'),
(43, 'Can delete change', 11, 'delete_change'),
(44, 'Can view change', 11, 'view_change'),
(45, 'Can add admin parent', 12, 'add_adminparent'),
(46, 'Can change admin parent', 12, 'change_adminparent'),
(47, 'Can delete admin parent', 12, 'delete_adminparent'),
(48, 'Can view admin parent', 12, 'view_adminparent'),
(49, 'Can add rejected admin', 13, 'add_rejectedadmin'),
(50, 'Can change rejected admin', 13, 'change_rejectedadmin'),
(51, 'Can delete rejected admin', 13, 'delete_rejectedadmin'),
(52, 'Can view rejected admin', 13, 'view_rejectedadmin'),
(53, 'Can add reported admin', 14, 'add_reportedadmin'),
(54, 'Can change reported admin', 14, 'change_reportedadmin'),
(55, 'Can delete reported admin', 14, 'delete_reportedadmin'),
(56, 'Can view reported admin', 14, 'view_reportedadmin'),
(57, 'Can add banned admin', 15, 'add_bannedadmin'),
(58, 'Can change banned admin', 15, 'change_bannedadmin'),
(59, 'Can delete banned admin', 15, 'delete_bannedadmin'),
(60, 'Can view banned admin', 15, 'view_bannedadmin'),
(61, 'Can add admin request', 16, 'add_adminrequest'),
(62, 'Can change admin request', 16, 'change_adminrequest'),
(63, 'Can delete admin request', 16, 'delete_adminrequest'),
(64, 'Can view admin request', 16, 'view_adminrequest'),
(65, 'Can add admin reason', 17, 'add_adminreason'),
(66, 'Can change admin reason', 17, 'change_adminreason'),
(67, 'Can delete admin reason', 17, 'delete_adminreason'),
(68, 'Can view admin reason', 17, 'view_adminreason'),
(69, 'Can add log entry', 18, 'add_logentry'),
(70, 'Can change log entry', 18, 'change_logentry'),
(71, 'Can delete log entry', 18, 'delete_logentry'),
(72, 'Can view log entry', 18, 'view_logentry'),
(73, 'Can add permission', 19, 'add_permission'),
(74, 'Can change permission', 19, 'change_permission'),
(75, 'Can delete permission', 19, 'delete_permission'),
(76, 'Can view permission', 19, 'view_permission'),
(77, 'Can add group', 20, 'add_group'),
(78, 'Can change group', 20, 'change_group'),
(79, 'Can delete group', 20, 'delete_group'),
(80, 'Can view group', 20, 'view_group'),
(81, 'Can add user', 21, 'add_user'),
(82, 'Can change user', 21, 'change_user'),
(83, 'Can delete user', 21, 'delete_user'),
(84, 'Can view user', 21, 'view_user'),
(85, 'Can add content type', 22, 'add_contenttype'),
(86, 'Can change content type', 22, 'change_contenttype'),
(87, 'Can delete content type', 22, 'delete_contenttype'),
(88, 'Can view content type', 22, 'view_contenttype'),
(89, 'Can add session', 23, 'add_session'),
(90, 'Can change session', 23, 'change_session'),
(91, 'Can delete session', 23, 'delete_session'),
(92, 'Can view session', 23, 'view_session');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$180000$EUe1Ux7bv5VB$G3LipGHJVsiGhLJxSVo7ClyTb4ezcuJSx6KDZHKL6hY=', '2020-04-12 13:26:09.040981', 1, 'superuser', '', '', 'msrianirudh.is17@rvce.edu.in', 1, 1, '2020-04-12 12:57:20.441237');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `books_author`
--

CREATE TABLE `books_author` (
  `id` int NOT NULL,
  `author` varchar(20) NOT NULL,
  `book_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `books_author`
--

INSERT INTO `books_author` (`id`, `author`, `book_id`) VALUES
(1, 'Raj Patel', 1),
(2, 'Bri Miles', 2),
(3, 'Terence Smart', 3),
(4, 'Sun Tzu', 4),
(5, 'Liam Scully', 5),
(6, 'Renate M Kaufmann', 6),
(7, 'Adam LaValley', 7),
(8, 'Ashley berrett', 8),
(9, 'otteri selvakumar', 9),
(10, 'otteri selvakumar', 10),
(11, 'Sander R.B.E. Beals', 11),
(12, 'J. Fenimore cooper', 12),
(13, 'Dennis M Ritche', 13),
(14, ' Bri', 13),
(15, 'Dewi Mulyani', 14),
(16, 'Dr Deepak Pant', 15),
(17, 'Sarah Joshway', 16),
(18, 'Jesus Villalobos', 17),
(19, 'Harish Damodaran', 18),
(20, 'Benjamin franklin', 19),
(21, 'Annie Besant', 20),
(22, 'C.F.Allison', 21),
(23, 'Jemma Grey', 22),
(24, 'Forest Ostrander', 23);

-- --------------------------------------------------------

--
-- Table structure for table `books_book`
--

CREATE TABLE `books_book` (
  `book` int NOT NULL,
  `name` longtext NOT NULL,
  `link` varchar(200) NOT NULL,
  `edition` int NOT NULL,
  `status` varchar(20) NOT NULL,
  `added_by_id` int NOT NULL,
  `assigned_admin_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `books_book`
--

INSERT INTO `books_book` (`book`, `name`, `link`, `edition`, `status`, `added_by_id`, `assigned_admin_id`) VALUES
(1, 'India', 'https://www.bookrix.com/_ebook-raj-patel-india-1/', 1, 'Accepted', 1, 1),
(2, 'Ancient Egyptian social classes', 'https://www.bookrix.com/_ebook-bri-miles-ancient-egyptian-social-classes/', 1, 'Accepted', 1, 1),
(3, 'The truth about Germany and the world wars', 'https://www.bookrix.com/_ebook-terence-smart-the-truth-about-germany-and-the-world-wars/', 1, 'Accepted', 1, 1),
(4, 'The art of war', 'https://www.bookrix.com/_ebook-sun-tzu-the-art-of-war/', 1, 'Accepted', 1, 1),
(5, 'The valley  of  the kings', 'https://www.bookrix.com/_ebook-liam-scully-the-valley-of-the-kings/', 1, 'Accepted', 1, 1),
(6, 'Soul Paintings', 'https://www.bookrix.com/_ebook-renate-m-kaufmann-soul-paintings/', 1, 'Accepted', 1, 1),
(7, 'Sketchbook', 'https://www.bookrix.com/_ebook-adam-lavalley-sketchbook/', 1, 'Accepted', 1, 1),
(8, 'my art', 'https://www.bookrix.com/_ebook-ashley-berrett-my-art/', 1, 'Accepted', 1, 1),
(9, 'funny art', 'https://www.bookrix.com/_ebook-otteri-selvakumar-funny-art/', 1, 'Accepted', 1, 1),
(10, 'line art', 'https://www.bookrix.com/_ebook-otteri-selvakumar-line-art/', 1, 'Accepted', 1, 1),
(11, 'Art of war once moore', 'https://www.bookrix.com/_ebook-sander-r-b-e-beals-art-of-war-once-moore/', 1, 'Accepted', 1, 1),
(12, 'The Pilot', 'https://www.bookrix.com/_ebook-j-fenimore-cooper-the-pilot-1/', 1, 'Accepted', 1, 1),
(13, 'The C programming language', 'http://www2.cs.uregina.ca/~hilder/cs833/Other%20Reference%20Materials/The%20C%20Programming%20Language.pdf', 2, 'Accepted', 1, 1),
(14, 'Related database(MySQL and CMD)', 'https://www.bookrix.com/_ebook-dewi-mulyani-related-database-mysql-and-cmd/', 1, 'Accepted', 1, 1),
(15, 'Inorganic chemistry practical', 'https://www.bookrix.com/_ebook-dr-deepak-pant-inorganic-chemistry-practical/', 1, 'Accepted', 1, 1),
(16, 'Newton laws', 'https://www.bookrix.com/_ebook-sarah-joshway-newton-039-s-laws/', 1, 'Accepted', 1, 1),
(17, 'Quantum physics', 'https://www.bookrix.com/_ebook-jesus-villalobos-quantum-physics/', 1, 'Accepted', 1, 1),
(18, 'The uncertainty principle', 'https://www.bookrix.com/_ebook-harish-damodaran-the-uncertainty-principle/', 1, 'Accepted', 1, 1),
(19, 'Autobiography of Benjamin franklin', 'https://www.bookrix.com/_ebook-benjamin-franklin-autobiography-of-benjamin-franklin/', 1, 'Accepted', 1, 1),
(20, 'Annie Besant', 'https://www.bookrix.com/_ebook-annie-besant-annie-besant/', 1, 'Accepted', 1, 1),
(21, 'The Gentleman Gunfighter', 'https://www.bookrix.com/_ebook-c-f-allison-the-gentleman-gunfighter/', 1, 'Accepted', 1, 1),
(22, 'Leave Me Breathless', 'https://www.bookrix.com/_ebook-jemma-grey-leave-me-breathless/', 1, 'Accepted', 1, 1),
(23, 'Spells of magic', 'https://www.bookrix.com/_ebook-forest-ostrander-spells-of-magic/', 1, 'Accepted', 1, 1);

-- --------------------------------------------------------

--
-- Table structure for table `books_bookimage`
--

CREATE TABLE `books_bookimage` (
  `id` int NOT NULL,
  `image` varchar(100) NOT NULL,
  `book_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `books_bookimage`
--

INSERT INTO `books_bookimage` (`id`, `image`, `book_id`) VALUES
(1, 'images/book1.png', 1),
(2, 'images/book2.png', 2),
(3, 'images/book3.png', 3),
(4, 'images/book4.png', 4),
(5, 'images/book5.png', 5),
(6, 'images/book6.png', 6),
(7, 'images/book7.png', 7),
(8, 'images/book8.png', 8),
(9, 'images/book9.png', 9),
(10, 'images/book10.png', 10),
(11, 'images/book11.png', 11),
(12, 'images/book12.png', 12),
(13, 'images/book13.jpg', 13),
(14, 'images/book14.png', 14),
(15, 'images/book15.png', 15),
(16, 'images/book16.png', 16),
(17, 'images/book17.png', 17),
(18, 'images/npa.png', 18),
(19, 'images/book19.png', 19),
(20, 'images/book20.png', 20),
(21, 'images/book21.png', 21),
(22, 'images/book22.png', 22),
(23, 'images/book23.png', 23);

-- --------------------------------------------------------

--
-- Table structure for table `books_deletebookrequest`
--

CREATE TABLE `books_deletebookrequest` (
  `id` int NOT NULL,
  `time` int NOT NULL,
  `assigned_admin_id` int NOT NULL,
  `book_id` int NOT NULL,
  `user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `books_tag`
--

CREATE TABLE `books_tag` (
  `id` int NOT NULL,
  `tag` varchar(20) NOT NULL,
  `book_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `books_tag`
--

INSERT INTO `books_tag` (`id`, `tag`, `book_id`) VALUES
(1, 'history', 1),
(2, 'india', 1),
(3, 'history', 2),
(4, ' social', 2),
(5, 'history', 3),
(6, 'social', 3),
(7, 'war', 3),
(8, 'war', 4),
(9, 'history', 5),
(10, 'art', 6),
(11, 'poetry', 6),
(12, 'art', 7),
(13, 'art', 8),
(14, 'art', 9),
(15, 'modernart', 9),
(16, 'art', 10),
(17, 'modernart', 10),
(18, 'technology', 11),
(19, 'history', 11),
(20, 'technology', 12),
(21, 'technology', 13),
(22, ' program', 13),
(23, 'technology', 14),
(24, ' program', 14),
(25, 'chemistry', 15),
(26, 'science', 15),
(27, 'physics', 16),
(28, 'science', 16),
(29, 'physics', 17),
(30, 'science', 17),
(31, 'physics', 18),
(32, 'science', 18),
(33, 'autobiography', 19),
(34, 'autobiography', 20),
(35, 'biography', 21),
(36, 'fantasy', 22),
(37, 'love', 22),
(38, 'fantasy', 23),
(39, 'magic', 23);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL
) ;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(18, 'admin', 'logentry'),
(12, 'admins', 'adminparent'),
(17, 'admins', 'adminreason'),
(16, 'admins', 'adminrequest'),
(15, 'admins', 'bannedadmin'),
(13, 'admins', 'rejectedadmin'),
(14, 'admins', 'reportedadmin'),
(20, 'auth', 'group'),
(19, 'auth', 'permission'),
(21, 'auth', 'user'),
(5, 'books', 'author'),
(1, 'books', 'book'),
(4, 'books', 'bookimage'),
(3, 'books', 'deletebookrequest'),
(2, 'books', 'tag'),
(22, 'contenttypes', 'contenttype'),
(11, 'issues', 'change'),
(10, 'issues', 'issue'),
(23, 'sessions', 'session'),
(6, 'users', 'banneduser'),
(7, 'users', 'reporteduser'),
(8, 'users', 'userprofile'),
(9, 'users', 'userreason');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-04-12 12:54:09.598325'),
(2, 'auth', '0001_initial', '2020-04-12 12:54:11.983767'),
(3, 'admin', '0001_initial', '2020-04-12 12:54:17.674267'),
(4, 'admin', '0002_logentry_remove_auto_add', '2020-04-12 12:54:19.545132'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2020-04-12 12:54:19.633102'),
(6, 'books', '0001_initial', '2020-04-12 12:54:22.209301'),
(7, 'issues', '0001_initial', '2020-04-12 12:54:28.511542'),
(8, 'contenttypes', '0002_remove_content_type_name', '2020-04-12 12:54:31.705369'),
(9, 'auth', '0002_alter_permission_name_max_length', '2020-04-12 12:54:32.274410'),
(10, 'auth', '0003_alter_user_email_max_length', '2020-04-12 12:54:32.498280'),
(11, 'auth', '0004_alter_user_username_opts', '2020-04-12 12:54:32.646214'),
(12, 'auth', '0005_alter_user_last_login_null', '2020-04-12 12:54:33.163142'),
(13, 'auth', '0006_require_contenttypes_0002', '2020-04-12 12:54:33.184904'),
(14, 'auth', '0007_alter_validators_add_error_messages', '2020-04-12 12:54:33.262875'),
(15, 'auth', '0008_alter_user_username_max_length', '2020-04-12 12:54:33.982612'),
(16, 'auth', '0009_alter_user_last_name_max_length', '2020-04-12 12:54:34.705486'),
(17, 'auth', '0010_alter_group_name_max_length', '2020-04-12 12:54:34.853114'),
(18, 'auth', '0011_update_proxy_permissions', '2020-04-12 12:54:34.966598'),
(19, 'users', '0001_initial', '2020-04-12 12:54:35.978619'),
(20, 'admins', '0001_initial', '2020-04-12 12:54:43.817960'),
(21, 'admins', '0002_auto_20200412_1253', '2020-04-12 12:54:50.038076'),
(22, 'sessions', '0001_initial', '2020-04-12 12:54:50.261841');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('adwqk4nurcfixewl920l1dmh9zntw2ic', 'ZmRmODlmNjk3NWY3YWJmOTVkY2EyMDFmYWNjYmZkNTIwYmNlZTk4ZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzMzdkZGI0NDI1MGE5NjBhMjE4ZmFlMTE2ZjZjM2E2ZDYyYzUzMTYxIn0=', '2020-04-26 13:26:09.128045');

-- --------------------------------------------------------

--
-- Table structure for table `issues_change`
--

CREATE TABLE `issues_change` (
  `id` int NOT NULL,
  `change` varchar(100) NOT NULL,
  `issue_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `issues_issue`
--

CREATE TABLE `issues_issue` (
  `issue` int NOT NULL,
  `status` varchar(20) NOT NULL,
  `description` varchar(200) NOT NULL,
  `time` int NOT NULL,
  `added_by_id` int NOT NULL,
  `assigned_to_id` int NOT NULL,
  `book_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users_banneduser`
--

CREATE TABLE `users_banneduser` (
  `user_id` int NOT NULL,
  `time` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users_reporteduser`
--

CREATE TABLE `users_reporteduser` (
  `id` int NOT NULL,
  `comment` longtext NOT NULL,
  `bookadder_id` int DEFAULT NULL,
  `deleterequest_id` int DEFAULT NULL,
  `issue_id` int DEFAULT NULL,
  `reporting_admin_id` int NOT NULL,
  `user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `users_userprofile`
--

CREATE TABLE `users_userprofile` (
  `user_id` int NOT NULL,
  `creation_date` datetime(6) NOT NULL,
  `gender` varchar(1) NOT NULL,
  `name` varchar(20) NOT NULL,
  `dob` datetime(6) NOT NULL,
  `country` varchar(20) NOT NULL,
  `email` varchar(254) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `users_userprofile`
--

INSERT INTO `users_userprofile` (`user_id`, `creation_date`, `gender`, `name`, `dob`, `country`, `email`) VALUES
(1, '2020-04-12 00:00:00.000000', 'M', 'Anirudh-Prahalad', '1999-07-14 00:00:00.000000', 'India', 'msrianirudh.is17@rvce.edu.in');

-- --------------------------------------------------------

--
-- Table structure for table `users_userreason`
--

CREATE TABLE `users_userreason` (
  `id` int NOT NULL,
  `reason` longtext NOT NULL,
  `banneduser_id` int DEFAULT NULL,
  `reporteduser_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admins_adminparent`
--
ALTER TABLE `admins_adminparent`
  ADD PRIMARY KEY (`created_id`),
  ADD KEY `admins_adminparent_creator_id_c2b0644e_fk_auth_user_id` (`creator_id`);

--
-- Indexes for table `admins_adminreason`
--
ALTER TABLE `admins_adminreason`
  ADD PRIMARY KEY (`id`),
  ADD KEY `admins_adminreason_bannedadmin_id_88d5cd0d_fk_admins_ba` (`bannedadmin_id`),
  ADD KEY `admins_adminreason_banneduser_id_75b89df5_fk_users_ban` (`banneduser_id`),
  ADD KEY `admins_adminreason_reportedadmin_id_df6c4790_fk_admins_re` (`reportedadmin_id`);

--
-- Indexes for table `admins_adminrequest`
--
ALTER TABLE `admins_adminrequest`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `admins_adminrequest_assigned_to_id_0e3fda7e_fk_auth_user_id` (`assigned_to_id`);

--
-- Indexes for table `admins_bannedadmin`
--
ALTER TABLE `admins_bannedadmin`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `admins_bannedadmin_assigned_admin_id_d4a5b1a5_fk_auth_user_id` (`assigned_admin_id`);

--
-- Indexes for table `admins_rejectedadmin`
--
ALTER TABLE `admins_rejectedadmin`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `admins_reportedadmin`
--
ALTER TABLE `admins_reportedadmin`
  ADD PRIMARY KEY (`admin_id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `books_author`
--
ALTER TABLE `books_author`
  ADD PRIMARY KEY (`id`),
  ADD KEY `books_author_book_id_607064dd_fk_books_book_book` (`book_id`);

--
-- Indexes for table `books_book`
--
ALTER TABLE `books_book`
  ADD PRIMARY KEY (`book`),
  ADD KEY `books_book_added_by_id_cf55bf7a_fk_auth_user_id` (`added_by_id`),
  ADD KEY `books_book_assigned_admin_id_effe11bd_fk_auth_user_id` (`assigned_admin_id`);

--
-- Indexes for table `books_bookimage`
--
ALTER TABLE `books_bookimage`
  ADD PRIMARY KEY (`id`),
  ADD KEY `books_bookimage_book_id_d8732b64_fk_books_book_book` (`book_id`);

--
-- Indexes for table `books_deletebookrequest`
--
ALTER TABLE `books_deletebookrequest`
  ADD PRIMARY KEY (`id`),
  ADD KEY `books_deletebookrequ_assigned_admin_id_85adc94c_fk_auth_user` (`assigned_admin_id`),
  ADD KEY `books_deletebookrequest_book_id_f624bea2_fk_books_book_book` (`book_id`),
  ADD KEY `books_deletebookrequest_user_id_c2c9485b_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `books_tag`
--
ALTER TABLE `books_tag`
  ADD PRIMARY KEY (`id`),
  ADD KEY `books_tag_book_id_d0c733b9_fk_books_book_book` (`book_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `issues_change`
--
ALTER TABLE `issues_change`
  ADD PRIMARY KEY (`id`),
  ADD KEY `issues_change_issue_id_00a20cbd_fk_issues_issue_issue` (`issue_id`);

--
-- Indexes for table `issues_issue`
--
ALTER TABLE `issues_issue`
  ADD PRIMARY KEY (`issue`),
  ADD KEY `issues_issue_added_by_id_79120d18_fk_auth_user_id` (`added_by_id`),
  ADD KEY `issues_issue_assigned_to_id_c6054289_fk_auth_user_id` (`assigned_to_id`),
  ADD KEY `issues_issue_book_id_5b66dfa6_fk_books_book_book` (`book_id`);

--
-- Indexes for table `users_banneduser`
--
ALTER TABLE `users_banneduser`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `users_reporteduser`
--
ALTER TABLE `users_reporteduser`
  ADD PRIMARY KEY (`id`),
  ADD KEY `users_reporteduser_bookadder_id_364bee7a_fk_books_book_book` (`bookadder_id`),
  ADD KEY `users_reporteduser_deleterequest_id_99b74207_fk_books_del` (`deleterequest_id`),
  ADD KEY `users_reporteduser_issue_id_2d8dffa0_fk_issues_issue_issue` (`issue_id`),
  ADD KEY `users_reporteduser_reporting_admin_id_f7ab4162_fk_auth_user_id` (`reporting_admin_id`),
  ADD KEY `users_reporteduser_user_id_bd519ea6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `users_userprofile`
--
ALTER TABLE `users_userprofile`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `users_userreason`
--
ALTER TABLE `users_userreason`
  ADD PRIMARY KEY (`id`),
  ADD KEY `users_userreason_banneduser_id_acab5b35_fk_users_ban` (`banneduser_id`),
  ADD KEY `users_userreason_reporteduser_id_828392fc_fk_users_rep` (`reporteduser_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admins_adminreason`
--
ALTER TABLE `admins_adminreason`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=93;
--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `books_author`
--
ALTER TABLE `books_author`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;
--
-- AUTO_INCREMENT for table `books_book`
--
ALTER TABLE `books_book`
  MODIFY `book` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
--
-- AUTO_INCREMENT for table `books_bookimage`
--
ALTER TABLE `books_bookimage`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
--
-- AUTO_INCREMENT for table `books_deletebookrequest`
--
ALTER TABLE `books_deletebookrequest`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `books_tag`
--
ALTER TABLE `books_tag`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;
--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;
--
-- AUTO_INCREMENT for table `issues_change`
--
ALTER TABLE `issues_change`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `issues_issue`
--
ALTER TABLE `issues_issue`
  MODIFY `issue` int NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `users_reporteduser`
--
ALTER TABLE `users_reporteduser`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `users_userreason`
--
ALTER TABLE `users_userreason`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `admins_adminparent`
--
ALTER TABLE `admins_adminparent`
  ADD CONSTRAINT `admins_adminparent_created_id_33e0e8d6_fk_auth_user_id` FOREIGN KEY (`created_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `admins_adminparent_creator_id_c2b0644e_fk_auth_user_id` FOREIGN KEY (`creator_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `admins_adminreason`
--
ALTER TABLE `admins_adminreason`
  ADD CONSTRAINT `admins_adminreason_bannedadmin_id_88d5cd0d_fk_admins_ba` FOREIGN KEY (`bannedadmin_id`) REFERENCES `admins_bannedadmin` (`user_id`),
  ADD CONSTRAINT `admins_adminreason_banneduser_id_75b89df5_fk_users_ban` FOREIGN KEY (`banneduser_id`) REFERENCES `users_banneduser` (`user_id`),
  ADD CONSTRAINT `admins_adminreason_reportedadmin_id_df6c4790_fk_admins_re` FOREIGN KEY (`reportedadmin_id`) REFERENCES `admins_reportedadmin` (`admin_id`);

--
-- Constraints for table `admins_adminrequest`
--
ALTER TABLE `admins_adminrequest`
  ADD CONSTRAINT `admins_adminrequest_assigned_to_id_0e3fda7e_fk_auth_user_id` FOREIGN KEY (`assigned_to_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `admins_adminrequest_user_id_d7800f94_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `admins_bannedadmin`
--
ALTER TABLE `admins_bannedadmin`
  ADD CONSTRAINT `admins_bannedadmin_assigned_admin_id_d4a5b1a5_fk_auth_user_id` FOREIGN KEY (`assigned_admin_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `admins_bannedadmin_user_id_6cfae823_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `admins_rejectedadmin`
--
ALTER TABLE `admins_rejectedadmin`
  ADD CONSTRAINT `admins_rejectedadmin_user_id_eed0bb47_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `admins_reportedadmin`
--
ALTER TABLE `admins_reportedadmin`
  ADD CONSTRAINT `admins_reportedadmin_admin_id_56e789ff_fk_auth_user_id` FOREIGN KEY (`admin_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `books_author`
--
ALTER TABLE `books_author`
  ADD CONSTRAINT `books_author_book_id_607064dd_fk_books_book_book` FOREIGN KEY (`book_id`) REFERENCES `books_book` (`book`);

--
-- Constraints for table `books_book`
--
ALTER TABLE `books_book`
  ADD CONSTRAINT `books_book_added_by_id_cf55bf7a_fk_auth_user_id` FOREIGN KEY (`added_by_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `books_book_assigned_admin_id_effe11bd_fk_auth_user_id` FOREIGN KEY (`assigned_admin_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `books_bookimage`
--
ALTER TABLE `books_bookimage`
  ADD CONSTRAINT `books_bookimage_book_id_d8732b64_fk_books_book_book` FOREIGN KEY (`book_id`) REFERENCES `books_book` (`book`);

--
-- Constraints for table `books_deletebookrequest`
--
ALTER TABLE `books_deletebookrequest`
  ADD CONSTRAINT `books_deletebookrequ_assigned_admin_id_85adc94c_fk_auth_user` FOREIGN KEY (`assigned_admin_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `books_deletebookrequest_book_id_f624bea2_fk_books_book_book` FOREIGN KEY (`book_id`) REFERENCES `books_book` (`book`),
  ADD CONSTRAINT `books_deletebookrequest_user_id_c2c9485b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `books_tag`
--
ALTER TABLE `books_tag`
  ADD CONSTRAINT `books_tag_book_id_d0c733b9_fk_books_book_book` FOREIGN KEY (`book_id`) REFERENCES `books_book` (`book`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `issues_change`
--
ALTER TABLE `issues_change`
  ADD CONSTRAINT `issues_change_issue_id_00a20cbd_fk_issues_issue_issue` FOREIGN KEY (`issue_id`) REFERENCES `issues_issue` (`issue`);

--
-- Constraints for table `issues_issue`
--
ALTER TABLE `issues_issue`
  ADD CONSTRAINT `issues_issue_added_by_id_79120d18_fk_auth_user_id` FOREIGN KEY (`added_by_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `issues_issue_assigned_to_id_c6054289_fk_auth_user_id` FOREIGN KEY (`assigned_to_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `issues_issue_book_id_5b66dfa6_fk_books_book_book` FOREIGN KEY (`book_id`) REFERENCES `books_book` (`book`);

--
-- Constraints for table `users_banneduser`
--
ALTER TABLE `users_banneduser`
  ADD CONSTRAINT `users_banneduser_user_id_79e7b183_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `users_reporteduser`
--
ALTER TABLE `users_reporteduser`
  ADD CONSTRAINT `users_reporteduser_bookadder_id_364bee7a_fk_books_book_book` FOREIGN KEY (`bookadder_id`) REFERENCES `books_book` (`book`),
  ADD CONSTRAINT `users_reporteduser_deleterequest_id_99b74207_fk_books_del` FOREIGN KEY (`deleterequest_id`) REFERENCES `books_deletebookrequest` (`id`),
  ADD CONSTRAINT `users_reporteduser_issue_id_2d8dffa0_fk_issues_issue_issue` FOREIGN KEY (`issue_id`) REFERENCES `issues_issue` (`issue`),
  ADD CONSTRAINT `users_reporteduser_reporting_admin_id_f7ab4162_fk_auth_user_id` FOREIGN KEY (`reporting_admin_id`) REFERENCES `auth_user` (`id`),
  ADD CONSTRAINT `users_reporteduser_user_id_bd519ea6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `users_userprofile`
--
ALTER TABLE `users_userprofile`
  ADD CONSTRAINT `users_userprofile_user_id_87251ef1_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `users_userreason`
--
ALTER TABLE `users_userreason`
  ADD CONSTRAINT `users_userreason_banneduser_id_acab5b35_fk_users_ban` FOREIGN KEY (`banneduser_id`) REFERENCES `users_banneduser` (`user_id`),
  ADD CONSTRAINT `users_userreason_reporteduser_id_828392fc_fk_users_rep` FOREIGN KEY (`reporteduser_id`) REFERENCES `users_reporteduser` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
