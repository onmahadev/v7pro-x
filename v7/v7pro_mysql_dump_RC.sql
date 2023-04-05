-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: localhost
-- Время создания: Апр 05 2023 г., 01:59
-- Версия сервера: 10.4.27-MariaDB
-- Версия PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `v7`
--

-- --------------------------------------------------------

--
-- Структура таблицы `cities`
--

CREATE TABLE `cities` (
  `id` int(10) UNSIGNED NOT NULL,
  `id_region` int(10) UNSIGNED NOT NULL,
  `id_country` mediumint(8) UNSIGNED NOT NULL,
  `name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `cities`
--

INSERT INTO `cities` (`id`, `id_region`, `id_country`, `name`) VALUES
(1, 1, 1, 'Лангепас'),
(2, 1, 1, 'Сургут'),
(3, 1, 1, 'ОМск'),
(6, 1, 44, 'Пало-Алто'),
(7, 1, 1, 'Георгиевка'),
(8, 1, 122, 'Маяпур'),
(9, 1, 122, 'Бирнагар'),
(10, 1, 134, 'Бангладеш'),
(11, 1, 134, 'Бангладеш'),
(12, 1, 123, 'Вриндаван');

-- --------------------------------------------------------

--
-- Структура таблицы `country`
--

CREATE TABLE `country` (
  `id` int(11) NOT NULL,
  `name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `flag` varchar(9) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL COMMENT 'ISO Code (2 letters)',
  `img` varchar(12) CHARACTER SET utf32 COLLATE utf32_bin DEFAULT NULL,
  `mok3code` varchar(3) DEFAULT NULL COMMENT 'International Olympic Code MOC  (3 letters)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

--
-- Дамп данных таблицы `country`
--

INSERT INTO `country` (`id`, `name`, `flag`, `img`, `mok3code`) VALUES
(1, 'Россия', 'RU', '🇷🇺', 'RUS'),
(2, 'Украина', 'UA', '🇺🇦', 'UKR'),
(6, 'Азербайджан', 'AZ', '🇦🇿', 'AZB'),
(15, 'Армения', 'AM', '🇦🇲', 'ARM'),
(17, 'Афганистан', 'AF', '🇦🇫', 'AFG'),
(22, 'Беларусь', 'BY', '🇧🇾', 'BLR'),
(61, 'Грузия', 'GE', '🇬🇪', 'GEO'),
(71, 'Индия', 'IN', '🇮🇳', 'IND'),
(74, 'Ирак', 'IQ', '🇮🇶', 'IRQ'),
(75, 'Иран', 'IR', '🇮🇷', 'IRI'),
(82, 'Казахстан', 'KZ', '🇰🇿', 'KAZ'),
(88, 'Кипр', 'CY', '🇨🇾', 'CYP'),
(90, 'Китай', 'CN', '🇨🇳', 'CHN'),
(97, 'Куба', 'CU', '🇨🇺', 'CUB'),
(100, 'Кыргызстан', 'KG', '🇰🇬', 'KGS'),
(141, 'Пакистан', 'PK', '🇵🇰', 'PAK'),
(170, 'Сирия', 'SY', '🇸🇾', 'SYR'),
(188, 'Туркменистан', 'TM', '🇹🇲', 'TKM'),
(190, 'Турция', 'TR', '🇹🇷', 'TUR'),
(192, 'Узбекистан', 'UZ', '🇺🇿', 'UZB'),
(218, 'Япония', 'JP', '🇯🇵', 'JPN'),
(219, 'Таиланд', 'TY', '🇹🇭', 'THA'),
(220, 'Малайзия', 'MY', '🇲🇾', 'MAS'),
(221, 'Вьетнам', 'VY', '🇻🇳', 'VIE'),
(222, 'Сингапур', 'SR', '🇸🇬', 'SGP'),
(223, 'Франция', 'FR', '🇫🇷', NULL),
(224, 'USA', 'US', '🇺🇸', NULL),
(225, 'Англия', 'GB', '🇬🇧', NULL),
(227, 'РСФСР', 'USSR', NULL, NULL);

-- --------------------------------------------------------

--
-- Структура таблицы `info`
--

CREATE TABLE `info` (
  `id` int(11) NOT NULL,
  `att_id` int(11) NOT NULL,
  `world_record` int(11) NOT NULL,
  `own_record` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `opt`
--

CREATE TABLE `opt` (
  `id` int(11) NOT NULL,
  `name` varchar(29) NOT NULL,
  `value` varchar(48) NOT NULL,
  `descript` varchar(48) NOT NULL,
  `descript_off` varchar(48) NOT NULL DEFAULT 'собственный вес  [ СКРЫТ ]',
  `param` varchar(9) NOT NULL,
  `changed_time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `opt`
--

INSERT INTO `opt` (`id`, `name`, `value`, `descript`, `descript_off`, `param`, `changed_time`) VALUES
(1, 'ui_language', '0', '', 'собственный вес  [ СКРЫТ ]', 'rus', '2022-08-07 22:06:02'),
(2, 'ui_language', 'ru', '', 'собственный вес  [ СКРЫТ ]', 'eng', '2022-08-07 22:07:40'),
(3, 'app_core_ip', '10.0.0.108', '', 'собственный вес  [ СКРЫТ ]', '10.0.0.1', '2022-08-07 22:09:12'),
(4, 'app_core_port', '5000', '', 'собственный вес  [ СКРЫТ ]', '5678', '2022-08-07 22:09:16'),
(5, 'app_core_version', '7.16.1128', '', 'собственный вес  [ СКРЫТ ]', '7.1.1659', '2022-08-07 22:09:18'),
(6, 'flow_show_rank_table', '1', '', 'собственный вес  [ СКРЫТ ]', '', '2022-08-07 22:09:20'),
(7, 'flow_mode_auto', '1', '', 'собственный вес  [ СКРЫТ ]', '', '2022-08-07 22:09:23'),
(8, 'dbl_show_flag', '1', 'флаг  [ ОТОБРАЖАЕТСЯ ]', 'флаг  [ СКРЫТ ]', '', '2022-08-07 22:09:23'),
(9, 'dbl_show_number', '1', 'номер №  [ ОТОБРАЖАЕТСЯ ]', 'номер №  [ СКРЫТ ]', '', '2022-08-07 22:09:23'),
(10, 'dbl_show_wcat', '1', 'весовая категория  [ ОТОБРАЖАЕТСЯ ]', 'весовая категория  [ СКРЫТА ]', '', '2022-08-07 22:09:23'),
(11, 'dbl_show_ow_city', '0', 'собственный вес  [ ОТОБРАЖАЕТСЯ ]', 'собственный вес   [ СКРЫТ ]', '', '2022-08-07 22:09:23'),
(12, 'dbl_background_color', '1', 'цвет заднего фона  [ ]', 'цвет заднего фона  [ ]', '', '2022-08-07 22:09:23'),
(13, 'dbl_show_2ccode', '1', 'страна ( 2 символа)  [ ОТОБРАЖАЕТСЯ ]', 'страна ( 2 символа)  [ СКРЫТА ]', '', '2022-08-07 22:09:23'),
(14, 'dbl_background_color', '03ff04', 'локация / город  [ ОТОБРАЖАЕТСЯ ]', 'локация / город  [ СКРЫТ ]', '', '2022-08-07 22:09:23'),
(15, 'dbl_background_color_isset', '0', 'локация / город  [ ОТОБРАЖАЕТСЯ ]', 'локация / город  [ СКРЫТ ]', '', '2022-08-07 22:09:23');

-- --------------------------------------------------------

--
-- Структура таблицы `ranks`
--

CREATE TABLE `ranks` (
  `id` int(11) NOT NULL,
  `sex` int(11) NOT NULL,
  `wcat` varchar(7) NOT NULL,
  `wcat_id` int(11) NOT NULL DEFAULT 7,
  `msmk` int(11) DEFAULT NULL,
  `ms` int(11) DEFAULT NULL,
  `kms` int(11) DEFAULT NULL,
  `rank1` int(11) DEFAULT NULL,
  `rank2` int(11) DEFAULT NULL,
  `rank3` int(11) DEFAULT NULL,
  `rank1jun` int(11) DEFAULT NULL,
  `rank2jun` int(11) DEFAULT NULL,
  `rank3jun` int(11) DEFAULT NULL,
  `value` int(11) DEFAULT NULL,
  `worldrecord` int(11) DEFAULT NULL,
  `also02` int(11) DEFAULT NULL,
  `wr_who` varchar(19) NOT NULL,
  `wr_where` varchar(29) NOT NULL,
  `wr_when` varchar(12) NOT NULL,
  `wr_snatch` int(11) DEFAULT NULL,
  `wr_cj` int(11) DEFAULT NULL,
  `wr_total` int(11) DEFAULT NULL,
  `wr_year` varchar(55) NOT NULL DEFAULT 'Действующие рекорды (с 2018 года)'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci COMMENT='att ranks table 2022';

--
-- Дамп данных таблицы `ranks`
--

INSERT INTO `ranks` (`id`, `sex`, `wcat`, `wcat_id`, `msmk`, `ms`, `kms`, `rank1`, `rank2`, `rank3`, `rank1jun`, `rank2jun`, `rank3jun`, `value`, `worldrecord`, `also02`, `wr_who`, `wr_where`, `wr_when`, `wr_snatch`, `wr_cj`, `wr_total`, `wr_year`) VALUES
(33, 1, '+109', 34, NULL, 325, 275, 150, 138, 126, NULL, NULL, NULL, 109109, NULL, NULL, 'Лаша Талахадзе', 'Ташкент  UZ', '17.12.2021', NULL, NULL, 492, 'Действующие рекорды (с 2018 года)'),
(34, 1, '+109', 34, NULL, 325, 275, 155, 143, 131, NULL, NULL, NULL, 109109, NULL, NULL, 'Лаша Талахадзе', 'Ташкент  UZ', '17.12.2021', NULL, 267, NULL, 'Действующие рекорды (с 2018 года)'),
(35, 1, '+109', 34, NULL, 325, 275, 155, 143, 131, NULL, NULL, NULL, 109109, NULL, NULL, 'Лаша Талахадзе', 'Ташкент  UZ', '17.12.2021', 225, NULL, NULL, 'Действующие рекорды (с 2018 года)'),
(36, 1, '109', 33, NULL, 320, 270, 246, 221, 196, NULL, NULL, NULL, 109, NULL, NULL, 'Ян Чжэ', 'Ташкент  UZ', '24.04.2021', 200, NULL, NULL, 'Действующие рекорды (с 2018 года)'),
(37, 1, '109', 33, NULL, 320, 270, 246, 221, 196, NULL, NULL, NULL, 109, NULL, NULL, 'Нурудинов Руслан', 'Ташкент  UZ', '24.04.2021', NULL, 241, NULL, 'Действующие рекорды (с 2018 года)'),
(38, 1, '109', 33, NULL, 320, 270, 246, 221, 196, NULL, NULL, NULL, 109, NULL, NULL, 'Симон Мартиросян', 'Ашхабад TM', '09.11.2018', NULL, NULL, 437, 'Действующие рекорды (с 2018 года)'),
(39, 1, '96', 30, NULL, 310, 255, 148, 136, 124, 112, 100, 88, 96, NULL, NULL, 'Лесман Паредес', 'Ташкент  UZ', '14.12.2021', 187, NULL, NULL, 'Действующие рекорды (с 2018 года)'),
(40, 1, '96', 30, NULL, 310, 255, 148, 136, 124, 112, 100, 88, 96, NULL, NULL, 'Тянь Тао', 'Токио  JP', '07.07.2019', NULL, 231, NULL, 'Действующие рекорды (с 2018 года)'),
(41, 1, '96', 30, NULL, 310, 255, 148, 136, 124, 112, 100, 88, 96, NULL, NULL, 'Сохраб Моради', 'Ашхабад TM', '07.11.2018', NULL, NULL, 416, 'Действующие рекорды (с 2018 года)'),
(42, 1, '89', 29, NULL, 295, 245, 148, 136, 124, 112, 100, 88, 96, NULL, NULL, 'Карлос Насар', 'Богота CL', '11.12.2022', NULL, 220, NULL, 'Действующие рекорды (с 2018 года)'),
(43, 1, '89', 29, NULL, 295, 245, 148, 136, 124, 112, 100, 88, 89, NULL, NULL, 'Антонио Пиццолато', 'Тирана CO', '02.06.2022', NULL, NULL, 392, 'Действующие рекорды (с 2018 года)'),
(44, 1, '81', 28, NULL, 280, 240, 148, 136, 124, 112, 100, 88, 81, NULL, NULL, 'Ли Даинь', 'Тирана CO', '01.01.2020', 175, NULL, NULL, 'Действующие рекорды (с 2018 года)'),
(45, 1, '81', 28, NULL, 280, 240, 148, 136, 124, 112, 100, 88, 81, NULL, NULL, 'Карлос Насар', 'Ташкент  UZ', '12.12.2021', NULL, 208, NULL, 'Действующие рекорды (с 2018 года)'),
(46, 1, '81', 28, NULL, 280, 240, 148, 136, 124, 112, 100, 88, 81, NULL, NULL, 'Люй Сяоцзюнь', 'Паттайя TH', '22.09.2019', NULL, NULL, 378, 'Действующие рекорды (с 2018 года)'),
(47, 1, '73', 27, NULL, 265, 220, 148, 136, 124, 112, 100, 88, 73, NULL, NULL, 'Ши Чжиюн', 'Нибно CN', '22.09.2019', 170, NULL, NULL, 'Действующие рекорды (с 2018 года)'),
(48, 1, '73', 27, NULL, 265, 220, 148, 136, 124, 112, 100, 88, 73, NULL, 2018, 'Ши Чжиюн', 'Паттайя TH', '21.09.2019', NULL, 199, NULL, 'Действующие рекорды (с 2018 года)'),
(49, 1, '73', 27, NULL, 265, 220, 148, 136, 124, 112, 100, 88, 73, NULL, 2018, 'Ши Чжиюн', 'Паттайя TH', '21.09.2019', NULL, NULL, 365, 'Действующие рекорды (с 2018 года)'),
(50, 1, '67', 26, NULL, 250, 200, 148, 136, 124, 112, 100, 88, 67, NULL, 2018, 'Хуан Миньхао', 'Токио  JP', '06.07.2019', 155, NULL, NULL, 'Действующие рекорды (с 2018 года)'),
(51, 1, '67', 26, NULL, 250, 200, 148, 136, 124, 112, 100, 88, 67, NULL, 2018, 'Пак Чон Джу', 'Паттайя TH', '18.09.2019', NULL, 188, NULL, 'Действующие рекорды (с 2018 года)'),
(52, 1, '67', 26, NULL, 250, 200, 148, 136, 124, 112, 100, 88, 67, NULL, 2018, 'Чэнь Лицзюнь', 'Нинбо CN', '21.04.2019', NULL, NULL, 339, 'Действующие рекорды (с 2018 года)'),
(53, 1, '61', 25, NULL, 225, 185, 148, 136, 124, 112, 100, 88, 61, NULL, 2018, 'Ли Фабинь', 'Паттайя TH', '19.09.2019', NULL, NULL, 318, 'Действующие рекорды (с 2018 года)'),
(54, 1, '61', 25, NULL, 225, 185, 148, 136, 124, 112, 100, 88, 61, NULL, 2018, 'Ли Фабинь', 'Паттайя TH', '19.09.2019', 145, NULL, NULL, 'Действующие рекорды (с 2018 года)'),
(55, 1, '61', 25, NULL, 225, 185, 148, 136, 124, 112, 100, 88, 61, NULL, 2018, 'Ли Фабинь', 'Богота CL', '07.12.2022', NULL, 175, NULL, 'Действующие рекорды (с 2018 года)'),
(56, 1, '55', 24, NULL, 200, 165, 148, 136, 124, 112, 100, 88, 55, NULL, 2018, 'Ом Юн Чхоль', 'Паттайя TH', '19.09.2019', NULL, NULL, 294, 'Действующие рекорды (с 2018 года)'),
(57, 1, '55', 24, NULL, 200, 165, 148, 136, 124, 112, 100, 88, 55, NULL, 2018, 'Ом Юн Чхоль', 'Паттайя TH', '19.09.2019', NULL, 166, NULL, 'Действующие рекорды (с 2018 года)'),
(59, 1, '49', 23, NULL, 175, 145, 148, 136, 124, 112, 100, 88, 49, NULL, 2018, '', '', '', NULL, NULL, NULL, 'Действующие рекорды (с 2018 года)');

-- --------------------------------------------------------

--
-- Структура таблицы `region`
--

CREATE TABLE `region` (
  `id` int(10) UNSIGNED NOT NULL,
  `country_id` mediumint(8) UNSIGNED NOT NULL,
  `name` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `region`
--

INSERT INTO `region` (`id`, `country_id`, `name`) VALUES
(1, 1, 'Москва и Московская обл.'),
(2, 1, 'Санкт-Петербург и область'),
(3, 1, 'Адыгея'),
(4, 1, 'Алтайский край'),
(5, 1, 'Амурская обл.'),
(6, 1, 'Архангельская обл.'),
(7, 1, 'Астраханская обл.'),
(8, 1, 'Башкортостан(Башкирия)'),
(9, 1, 'Белгородская обл.'),
(10, 1, 'Брянская обл.'),
(11, 1, 'Бурятия'),
(12, 1, 'Владимирская обл.'),
(13, 1, 'Волгоградская обл.'),
(14, 1, 'Вологодская обл.'),
(15, 1, 'Воронежская обл.'),
(16, 1, 'Дагестан'),
(17, 1, 'Еврейская обл.'),
(18, 1, 'Ивановская обл.'),
(19, 1, 'Иркутская обл.'),
(20, 1, 'Кабардино-Балкария'),
(21, 1, 'Калининградская обл.'),
(22, 1, 'Калмыкия'),
(23, 1, 'Калужская обл.'),
(24, 1, 'Камчатская обл.'),
(25, 1, 'Карелия'),
(26, 1, 'Кемеровская обл.'),
(27, 1, 'Кировская обл.'),
(28, 1, 'Коми'),
(29, 1, 'Костромская обл.'),
(30, 1, 'Краснодарский край'),
(31, 1, 'Красноярский край'),
(32, 1, 'Курганская обл.'),
(33, 1, 'Курская обл.'),
(34, 1, 'Липецкая обл.'),
(35, 1, 'Магаданская обл.'),
(36, 1, 'Марий Эл'),
(37, 1, 'Мордовия'),
(38, 1, 'Мурманская обл.'),
(39, 1, 'Нижегородская (Горьковская)'),
(40, 1, 'Новгородская обл.'),
(41, 1, 'Новосибирская обл.'),
(42, 1, 'Омская обл.'),
(43, 1, 'Оренбургская обл.'),
(44, 1, 'Орловская обл.'),
(45, 1, 'Пензенская обл.'),
(46, 1, 'Пермский край'),
(47, 1, 'Приморский край'),
(48, 1, 'Псковская обл.'),
(49, 1, 'Ростовская обл.'),
(50, 1, 'Рязанская обл.'),
(51, 1, 'Самарская обл.'),
(52, 1, 'Саратовская обл.'),
(53, 1, 'Саха (Якутия)'),
(54, 1, 'Сахалин'),
(55, 1, 'Свердловская обл.'),
(56, 1, 'Северная Осетия'),
(57, 1, 'Смоленская обл.'),
(58, 1, 'Ставропольский край'),
(59, 1, 'Тамбовская обл.'),
(60, 1, 'Татарстан'),
(61, 1, 'Тверская обл.'),
(62, 1, 'Томская обл.'),
(63, 1, 'Тува (Тувинская Респ.)'),
(64, 1, 'Тульская обл.'),
(65, 1, 'Тюменская обл. и Ханты-Мансийский АО'),
(66, 1, 'Удмуртия'),
(67, 1, 'Ульяновская обл.'),
(68, 1, 'Уральская обл.'),
(69, 1, 'Хабаровский край'),
(70, 1, 'Хакасия'),
(71, 1, 'Челябинская обл.'),
(72, 1, 'Чечено-Ингушетия'),
(73, 1, 'Читинская обл.'),
(74, 1, 'Чувашия'),
(75, 1, 'Чукотский АО'),
(76, 1, 'Ямало-Ненецкий АО'),
(77, 1, 'Ярославская обл.'),
(78, 1, 'Карачаево-Черкесская Республика'),
(79, 1, 'Ханты-Мансийский АО');

-- --------------------------------------------------------

--
-- Структура таблицы `v7now`
--

CREATE TABLE `v7now` (
  `id` int(11) NOT NULL,
  `op` int(11) NOT NULL DEFAULT 0,
  `nextop` int(11) NOT NULL DEFAULT 0,
  `prevop` int(11) NOT NULL DEFAULT 0,
  `weightnow` int(11) NOT NULL DEFAULT 0,
  `exnow` enum('s1','s2','s3','j1','j2','j3','finished') NOT NULL DEFAULT 's1',
  `trynow` int(11) DEFAULT 0,
  `serialnumber` int(11) DEFAULT NULL,
  `sex` int(11) NOT NULL DEFAULT 1,
  `ownweight` float(10,1) NOT NULL DEFAULT 72.8,
  `wcat_id` int(5) DEFAULT 1,
  `rank_id` int(11) DEFAULT 0,
  `info_id` int(11) DEFAULT 1,
  `newrank` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `sincler` varchar(15) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `position` int(11) DEFAULT NULL,
  `snatch1` int(11) NOT NULL DEFAULT 44,
  `snatch1isget` tinyint(3) DEFAULT NULL,
  `s1d` int(11) DEFAULT NULL,
  `s1ch1` int(11) DEFAULT NULL,
  `s1ch2` int(11) DEFAULT NULL,
  `s1ch3` int(11) DEFAULT NULL,
  `snatch2` int(11) DEFAULT NULL,
  `snatch2isget` tinyint(3) DEFAULT NULL,
  `s2d` int(11) DEFAULT NULL,
  `s2ai` int(11) DEFAULT NULL,
  `s2ch1` int(11) DEFAULT NULL,
  `s2ch2` int(11) DEFAULT NULL,
  `snatch3` int(11) DEFAULT NULL,
  `snatch3isget` tinyint(3) DEFAULT NULL,
  `s3d` int(11) DEFAULT NULL,
  `s3ai` int(11) DEFAULT NULL,
  `s3ch1` int(11) DEFAULT NULL,
  `s3ch2` int(11) DEFAULT NULL,
  `snatchresult` int(11) DEFAULT 0,
  `snatch_place` int(3) DEFAULT NULL COMMENT 'snatch place',
  `cleanjerk1` int(11) NOT NULL DEFAULT 55,
  `cleanjerk1isget` tinyint(3) DEFAULT NULL,
  `cleanjerk1d` int(11) DEFAULT NULL,
  `cleanjerk1ch1` int(11) DEFAULT NULL,
  `cleanjerk1ch2` int(11) DEFAULT NULL,
  `cleanjerk1ch3` int(11) DEFAULT NULL,
  `cleanjerk2` int(11) DEFAULT NULL,
  `cleanjerk2isget` tinyint(3) DEFAULT NULL,
  `cleanjerk2d` int(11) DEFAULT NULL,
  `cleanjerk2ai` int(11) DEFAULT NULL,
  `cleanjerk2ch1` int(11) DEFAULT NULL,
  `cleanjerk2ch2` int(11) DEFAULT NULL,
  `cleanjerk3` int(11) DEFAULT NULL,
  `cleanjerk3isget` tinyint(3) DEFAULT NULL,
  `cleanjerk3d` int(11) DEFAULT NULL,
  `cleanjerk3ai` int(11) DEFAULT NULL,
  `cleanjerk3ch1` int(11) DEFAULT NULL,
  `cleanjerk3ch2` int(11) DEFAULT NULL,
  `cleanjerkresult` int(11) DEFAULT 0,
  `cleanjerk_place` int(3) DEFAULT NULL COMMENT 'clean&jerk place',
  `doublesum` int(11) DEFAULT 0,
  `firstname` varchar(15) NOT NULL DEFAULT 'Нимай',
  `secondname` varchar(15) NOT NULL DEFAULT 'Махапрабху',
  `birth` varchar(10) NOT NULL DEFAULT '07.08.1983',
  `country_id` int(11) DEFAULT 1,
  `city_id` varchar(27) DEFAULT '1',
  `city` varchar(39) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL DEFAULT '1',
  `avatar` varchar(50) NOT NULL DEFAULT '/img/avatars/defava0.png',
  `changets` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `guru1name` varchar(20) NOT NULL DEFAULT 'Палько С.А.',
  `guru2name` varchar(20) NOT NULL DEFAULT 'Палько А.Г.',
  `ishideordel` int(11) NOT NULL DEFAULT 0,
  `actionend` int(11) NOT NULL DEFAULT 0,
  `place` int(3) DEFAULT NULL COMMENT 'flow att place',
  `flow_` tinyint(3) DEFAULT NULL COMMENT 'null - новый Атлет \r\n         1 - Выступает (сейчас Атлет в потоке выступления)\r\n         2 - Выступил ( Атлет уже выступил, скрыт)',
  `country_` enum('rus','ukr','kaz','uzb','usa','arm','grg') NOT NULL DEFAULT 'rus',
  `wcat_` varchar(5) NOT NULL DEFAULT '102+',
  `bkp_creation` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `v7now`
--

INSERT INTO `v7now` (`id`, `op`, `nextop`, `prevop`, `weightnow`, `exnow`, `trynow`, `serialnumber`, `sex`, `ownweight`, `wcat_id`, `rank_id`, `info_id`, `newrank`, `score`, `sincler`, `position`, `snatch1`, `snatch1isget`, `s1d`, `s1ch1`, `s1ch2`, `s1ch3`, `snatch2`, `snatch2isget`, `s2d`, `s2ai`, `s2ch1`, `s2ch2`, `snatch3`, `snatch3isget`, `s3d`, `s3ai`, `s3ch1`, `s3ch2`, `snatchresult`, `snatch_place`, `cleanjerk1`, `cleanjerk1isget`, `cleanjerk1d`, `cleanjerk1ch1`, `cleanjerk1ch2`, `cleanjerk1ch3`, `cleanjerk2`, `cleanjerk2isget`, `cleanjerk2d`, `cleanjerk2ai`, `cleanjerk2ch1`, `cleanjerk2ch2`, `cleanjerk3`, `cleanjerk3isget`, `cleanjerk3d`, `cleanjerk3ai`, `cleanjerk3ch1`, `cleanjerk3ch2`, `cleanjerkresult`, `cleanjerk_place`, `doublesum`, `firstname`, `secondname`, `birth`, `country_id`, `city_id`, `city`, `avatar`, `changets`, `guru1name`, `guru2name`, `ishideordel`, `actionend`, `place`, `flow_`, `country_`, `wcat_`, `bkp_creation`) VALUES
(1, 0, 0, 0, 35, 's1', 0, NULL, 1, 72.8, 34, 34, 1, NULL, NULL, '', NULL, 35, NULL, 35, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 1, 155, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 1, 0, 'Гаура́нга', 'Нитьяна́нда', '07.03.1486', 1, '1', '1', '/img/avatars/defava11.png', '2023-04-04 23:59:39', 'Палькодзян С.А.', 'Палько А.Г.', 0, 1, 1, 2, 'rus', '102+', ''),
(2, 0, 0, 0, 34, 's1', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 34, NULL, 34, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 2, 155, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 2, 0, 'ṬHĀKURA', 'Haridāsa', '', 1, '1', ' Лангепас  ', '/img/avatars/defava0.png', '2023-04-04 23:59:39', 'Палько С.А.', 'Палько А.Г.', 0, 1, 2, 2, 'rus', '102+', ''),
(3, 0, 0, 0, 67, 's1', 0, NULL, 1, 69.7, 34, 34, 1, NULL, NULL, '', NULL, 67, NULL, 67, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 3, 190, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 3, 0, 'Прабху', 'Иванов', '', 1, '1', ' Лангепас  ', '/img/avatars/defava0.png', '2023-04-04 23:59:39', 'Палько С.А.', 'Палько А.Г.', 0, 1, 3, 2, 'rus', '102+', ''),
(4, 1, 0, 0, 32, 's1', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 32, NULL, 32, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 189, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 0, 'Банинадзе', 'Алаваш', '', 1, '1', ' Лангепас  ', '/img/avatars/defava0.png', '2023-04-04 23:59:39', 'Палько С.А.', 'Палько А.Г.', 0, 1, 4, 2, 'rus', '102+', ''),
(5, 0, 0, 0, 66, 's1', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 66, NULL, 66, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 5, 154, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 5, 0, 'Турхмалов', 'Алабаса', '', 1, '1', ' Лангепас  ', '/img/avatars/defava0.png', '2023-04-04 23:59:39', 'Палько С.А.', 'Палько А.Г.', 0, 1, 5, 2, 'rus', '102+', '');

--
-- Триггеры `v7now`
--
DELIMITER $$
CREATE TRIGGER `set_double_sum` BEFORE UPDATE ON `v7now` FOR EACH ROW SET NEW.doublesum = NEW.snatchresult + NEW.cleanjerkresult
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `set_jerk_res` BEFORE UPDATE ON `v7now` FOR EACH ROW SET NEW.cleanjerkresult=(
SELECT GREATEST(IF(NEW.cleanjerk1isget=1,IFNULL(NEW.cleanjerk1, 0),0), IF(NEW.cleanjerk2isget=1,IFNULL(NEW.cleanjerk2, 0),0),
IF(NEW.cleanjerk3isget=1,IFNULL(NEW.cleanjerk3, 0),0))
)
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `set_snatch_res` BEFORE UPDATE ON `v7now` FOR EACH ROW SET NEW.snatchresult=(
SELECT GREATEST(IF(NEW.snatch1isget=1,IFNULL(NEW.snatch1, 0),0), IF(NEW.snatch2isget=1,IFNULL(NEW.snatch2, 0),0),
IF(NEW.snatch3isget=1,IFNULL(NEW.snatch3, 0),0))
)
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Структура таблицы `v7staff`
--

CREATE TABLE `v7staff` (
  `id` int(11) NOT NULL,
  `flow_gpoup` int(11) NOT NULL DEFAULT 1,
  `name` varchar(25) NOT NULL DEFAULT 'Иванов И.В.',
  `post` varchar(31) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `post_ru` varchar(31) NOT NULL DEFAULT 'Судья',
  `city` varchar(29) NOT NULL DEFAULT 'Лангепас',
  `category` varchar(5) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL DEFAULT 'ВК'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `v7staff`
--

INSERT INTO `v7staff` (`id`, `flow_gpoup`, `name`, `post`, `post_ru`, `city`, `category`) VALUES
(1, 1, 'Палько А.Г.', 'HeadOfJuri', 'Руководитель жюриИии', 'Ялта', 'ВК'),
(2, 1, 'Палько С.А.', 'MemberOfJury', 'Член жюри', 'Лангепас', 'ВК'),
(3, 1, 'Иванов И.В.', 'MemberOfJury2', 'Член жюри', 'Лангепас', '1К'),
(4, 1, 'Курбанов Ш.К.', 'JudgeChief', 'Главный судья', 'Солнечный', 'ВК'),
(5, 1, 'Госвами Ш.П.', 'SecretaryChief', 'Главный секретарь\n', 'Шадринск', 'ВК'),
(6, 1, 'Лизунов Р.В.', 'CentralJudge', 'Центральный судья', 'Солнечный', 'ВК'),
(7, 1, 'Чубатый И.О.', 'Doctor', 'Доктор', 'Тарко-Сале', 'ВК'),
(8, 1, 'Джубака А.А.', 'Judge', 'Судья', 'Минск', '1К'),
(9, 1, 'Боркин А.А.', 'Judge2', 'Судья', 'Омск', 'ВК'),
(10, 1, 'Сиклый А.Э.', 'TechController', 'Технический контролер', 'Лангепас', 'ВК'),
(11, 1, 'Горов Ж.Б.', 'LeadSecretary', 'Ведущий секретарь', 'Москва', 'ВК'),
(12, 1, 'Иванов И.В.', 'LeadSecretaryAssistant', 'Пом. вед. секретаря', 'Пенза', 'ВК'),
(13, 2, 'Палько С.А.', 'HeadOfJuri', 'Руководитель жюри', 'Лангепас', 'ВК'),
(14, 2, 'Палько А.Г.', 'MemberOfJury', 'Член жюри', 'Лангепас', 'ВК'),
(15, 2, 'Иванов И.В.', 'MemberOfJury2', 'Член жюри', 'Лангепас', '1К'),
(16, 2, 'Одуван Б.К.', 'JudgeChief', 'Главный судья', 'Солнечный', 'ВК'),
(17, 2, 'Смирнов Д.В.', 'SecretaryChief', 'Главный секретарь\n', 'Шадринск', 'ВК'),
(18, 2, 'Зеленченков Р.В.', 'CentralJudge', 'Центральный судья', 'Солнечный', 'ВК'),
(19, 2, 'Попачкин С.А.', 'Doctor', 'Доктор', 'Тарко-Сале', 'ВК'),
(20, 2, 'Сорокин Ю.А.', 'Judge', 'Судья', 'Сургут', 'ВК'),
(21, 2, 'Банкин П.И.', 'Judge2', 'Судья', 'Саратов', 'ВК'),
(22, 2, 'Петров И.В.', 'TechController', 'Технический контролер', 'Лангепас', '1К'),
(23, 2, 'ИСидоров И.В.', 'LeadSecretary', 'Ведущий секретарь', 'Лангепас', 'ВК'),
(24, 2, 'Цой И.В.', 'LeadSecretaryAssistant', 'Пом. вед. секретаря', 'Лангепас', 'ВК'),
(25, 3, 'Ручьев А.А.', 'HeadOfJuri', 'Руководитель жюри', 'Коряжма', 'ВК'),
(26, 3, 'Тушер Ю.Л.', 'MemberOfJury', 'Член жюри', 'Москва', 'ВК'),
(27, 3, 'Юткин А.А.', 'MemberOfJury2', 'Член жюри', 'Приозерск', '1К'),
(28, 3, 'Спицина О.И.', 'JudgeChief', 'Главный судья', 'Приозерск', '1К'),
(29, 3, 'Василенко Н.Н.', 'SecretaryChief', 'Главный секретарь', 'Сыктывкар', 'ВК'),
(30, 3, 'Лилейко А.С.', 'CentralJudge', 'Центральный судья', 'Выборг', 'ВК'),
(31, 3, 'Дмитриев А.В.', 'Doctor', 'Доктор', 'Москва', 'ВК'),
(32, 3, 'Нескородов Ю.В.', 'Judge', 'Судья', 'Курск', 'ВК'),
(33, 3, 'Федяев О.С.', 'Judge2', 'Судья', 'Курск', 'ВК'),
(34, 3, 'Борыгина А.А.', 'TechController', 'Технический контролер', 'Санкт-Петербург', 'ВК'),
(35, 3, 'Гонке Е.С.', 'LeadSecretary', 'Ведущий секретарь', 'Коряжма', 'ВК'),
(36, 3, 'Бабушкин Е.А.', 'LeadSecretaryAssistant', 'Пом. вед. секретаря', 'Новосибирск', '1К'),
(37, 4, 'Дешев А.А.', 'HeadOfJuri', 'Руководитель жюри', 'с. Алхуд', 'ВК'),
(38, 4, 'Ивочкин С.Н.', 'MemberOfJury', 'Член жюри', 'Дятьково', '1К'),
(39, 4, 'Лустина И.Н.', 'MemberOfJury2', 'Член жюри', 'пгт. Мостовской', '1К'),
(40, 4, 'Одуван Б.К.', 'JudgeChief', 'Главный судья', 'Солнечный', 'ВК'),
(41, 4, 'Колосов И.Г.', 'SecretaryChief', 'Главный секретарь', 'Ессентуки', 'ВК'),
(42, 4, 'Коблев А.М.', 'CentralJudge', 'Центральный судья', 'Майкоп', '1К'),
(43, 4, 'Чембохов А.М.', 'Doctor', 'Доктор', 'а. Джамбичи', '1К'),
(44, 4, 'Любимов В.А.', 'Judge', 'Судья', 'Саянск', '1К'),
(45, 4, 'Эврюков А.П.', 'Judge2', 'Судья', 'Саратов', 'ВК'),
(46, 4, 'Петров И.В.', 'TechController', 'Технический контролер', 'Димитровград', 'ВК'),
(47, 4, 'Эврюкова О.Н.', 'LeadSecretary', 'Ведущий секретарь', 'Димитровград', 'ВК'),
(48, 4, 'Чехин В.В.', 'LeadSecretaryAssistant', 'Пом. вед. секретаря', 'Старый Оскол', 'ВК'),
(49, 5, 'Слободян С.Б.', 'HeadOfJuri', 'Руководитель жюри', 'Сыктывкар', '1К'),
(50, 5, 'Разинькова А.А.', 'MemberOfJury', 'Член жюри', 'Курск', 'ВК'),
(51, 5, 'Кондрашова Я.В.', 'MemberOfJury2', 'Член жюри', 'Москва', 'ВК'),
(52, 5, 'Карагачан С.М.', 'JudgeChief', 'Главный судья', 'Лангепас', '1К'),
(53, 5, 'Мктрчян М.Л.', 'SecretaryChief', 'Главный секретарь', 'Карлино', '1К'),
(54, 5, 'Посохин П.Н.', 'CentralJudge', 'Центральный судья', 'Уфа', 'ВК'),
(55, 5, 'Яруллин А.Ф.', 'Doctor', 'Доктор', 'а. Джамбичи', '1К'),
(56, 5, 'Тё С.Ю.', 'Judge', 'Судья', 'Омск', 'ВК'),
(57, 5, 'Лаптев О.Ю.', 'Judge2', 'Судья', 'Ульяновск', '1К'),
(58, 5, 'Бергун А.А.', 'TechController', 'Технический контролер', 'Краснодар', 'ВК'),
(59, 5, 'Шуваев М.В.', 'LeadSecretary', 'Ведущий секретарь', 'Барнаул', 'ВК'),
(60, 5, 'Кучин В.А.', 'LeadSecretaryAssistant', 'Пом. вед. секретаря', 'Нефтекамск', 'ВК');

-- --------------------------------------------------------

--
-- Структура таблицы `v7stat`
--

CREATE TABLE `v7stat` (
  `id` int(9) NOT NULL,
  `yes_vote` int(8) NOT NULL DEFAULT 0,
  `not_vote` int(8) NOT NULL DEFAULT 0,
  `w_max` int(8) DEFAULT NULL,
  `w_min` int(9) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `v7timer`
--

CREATE TABLE `v7timer` (
  `id` int(5) NOT NULL COMMENT 'id',
  `start_timestamp` timestamp(6) NOT NULL DEFAULT current_timestamp(6),
  `status` int(7) NOT NULL DEFAULT 0 COMMENT '0-stop; 1-run;2-pause',
  `one_two_min` int(11) NOT NULL DEFAULT 1 COMMENT '1 min:60 sec OR 2 min:120 sec',
  `curr_timestamp` timestamp(6) NOT NULL DEFAULT current_timestamp(6) ON UPDATE current_timestamp(6),
  `until_end` varchar(19) DEFAULT '60',
  `paused_seconds` int(2) DEFAULT NULL,
  `time2display` varchar(19) NOT NULL DEFAULT '60'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin COMMENT='v7 timer the';

--
-- Дамп данных таблицы `v7timer`
--

INSERT INTO `v7timer` (`id`, `start_timestamp`, `status`, `one_two_min`, `curr_timestamp`, `until_end`, `paused_seconds`, `time2display`) VALUES
(1, '2023-03-27 16:32:09.550540', 0, 1, '2023-03-27 16:34:07.649973', '0', NULL, '60');

--
-- Триггеры `v7timer`
--
DELIMITER $$
CREATE TRIGGER `odd_seconds` BEFORE UPDATE ON `v7timer` FOR EACH ROW SET NEW.until_end = NEW.until_end
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Структура таблицы `wcat`
--

CREATE TABLE `wcat` (
  `id` int(11) NOT NULL,
  `sex` tinyint(4) NOT NULL DEFAULT 1,
  `wcat` varchar(5) NOT NULL,
  `label` varchar(7) NOT NULL,
  `label_ru` varchar(9) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL DEFAULT '22 кг'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `wcat`
--

INSERT INTO `wcat` (`id`, `sex`, `wcat`, `label`, `label_ru`) VALUES
(1, 0, '40', '40 kG', '40 кг'),
(2, 0, '45', '45 kG', '45 кг'),
(3, 0, '49', '49 kG', '49 кг'),
(4, 0, '55', '55 kG', '55 кг'),
(5, 0, '59', '59 kG', '59 кг'),
(6, 0, '64', '64 kG', '64 кг'),
(7, 0, '71', '71 kG', '71 кг'),
(8, 0, '76', '76 kG', '76 кг'),
(9, 0, '81', '81 kG', '81 кг'),
(10, 0, '81+', '81+ kG', '81+ кг'),
(11, 0, '87', '87 kG', '87 кг'),
(12, 0, '87+', '87+ kG', '87+ кг'),
(23, 1, '49', '49 kG', '49 кг'),
(24, 1, '55', '55 kG', '55 кг'),
(25, 1, '61', '61 kG', '61 кг'),
(26, 1, '67', '67 kG', '67 кг'),
(27, 1, '73', '73 kG', '73 кг'),
(28, 1, '81', '81 kG', '81 кг'),
(29, 1, '89', '89 kG', '89 кг'),
(30, 1, '96', '96 kG', '96 кг'),
(31, 1, '102', '102 kG', '102 кг'),
(32, 1, '102+', '102+ kG', '102+ кг'),
(33, 1, '109', '109 kG', '109 кг'),
(34, 1, '109+', '109+ kG', '109+ кг');

-- --------------------------------------------------------

--
-- Структура таблицы `_v7athlete`
--

CREATE TABLE `_v7athlete` (
  `id` int(11) NOT NULL,
  `op` int(11) NOT NULL DEFAULT 0,
  `nextop` int(11) NOT NULL DEFAULT 0,
  `prevop` int(11) NOT NULL DEFAULT 0,
  `weightnow` int(11) NOT NULL DEFAULT 0,
  `exnow` enum('s1','s2','s3','j1','j2','j3','finished') NOT NULL DEFAULT 's1',
  `trynow` int(11) DEFAULT 0,
  `serialnumber` int(11) DEFAULT NULL,
  `sex` int(11) NOT NULL DEFAULT 1,
  `ownweight` float(10,1) NOT NULL DEFAULT 72.8,
  `wcat_id` int(5) DEFAULT 1,
  `rank_id` int(11) DEFAULT 0,
  `info_id` int(11) DEFAULT 1,
  `newrank` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `sincler` varchar(15) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `position` int(11) DEFAULT NULL,
  `snatch1` int(11) NOT NULL DEFAULT 44,
  `snatch1isget` tinyint(3) DEFAULT NULL,
  `s1d` int(11) DEFAULT NULL,
  `s1ch1` int(11) DEFAULT NULL,
  `s1ch2` int(11) DEFAULT NULL,
  `s1ch3` int(11) DEFAULT NULL,
  `snatch2` int(11) DEFAULT NULL,
  `snatch2isget` tinyint(3) DEFAULT NULL,
  `s2d` int(11) DEFAULT NULL,
  `s2ai` int(11) DEFAULT NULL,
  `s2ch1` int(11) DEFAULT NULL,
  `s2ch2` int(11) DEFAULT NULL,
  `snatch3` int(11) DEFAULT NULL,
  `snatch3isget` tinyint(3) DEFAULT NULL,
  `s3d` int(11) DEFAULT NULL,
  `s3ai` int(11) DEFAULT NULL,
  `s3ch1` int(11) DEFAULT NULL,
  `s3ch2` int(11) DEFAULT NULL,
  `snatchresult` int(11) DEFAULT 0,
  `snatch_place` int(3) DEFAULT NULL COMMENT 'snatch place',
  `cleanjerk1` int(11) NOT NULL DEFAULT 55,
  `cleanjerk1isget` tinyint(3) DEFAULT NULL,
  `cleanjerk1d` int(11) DEFAULT NULL,
  `cleanjerk1ch1` int(11) DEFAULT NULL,
  `cleanjerk1ch2` int(11) DEFAULT NULL,
  `cleanjerk1ch3` int(11) DEFAULT NULL,
  `cleanjerk2` int(11) DEFAULT NULL,
  `cleanjerk2isget` tinyint(3) DEFAULT NULL,
  `cleanjerk2d` int(11) DEFAULT NULL,
  `cleanjerk2ai` int(11) DEFAULT NULL,
  `cleanjerk2ch1` int(11) DEFAULT NULL,
  `cleanjerk2ch2` int(11) DEFAULT NULL,
  `cleanjerk3` int(11) DEFAULT NULL,
  `cleanjerk3isget` tinyint(3) DEFAULT NULL,
  `cleanjerk3d` int(11) DEFAULT NULL,
  `cleanjerk3ai` int(11) DEFAULT NULL,
  `cleanjerk3ch1` int(11) DEFAULT NULL,
  `cleanjerk3ch2` int(11) DEFAULT NULL,
  `cleanjerkresult` int(11) DEFAULT 0,
  `cleanjerk_place` int(3) DEFAULT NULL COMMENT 'clean&jerk place',
  `doublesum` int(11) DEFAULT 0,
  `firstname` varchar(15) NOT NULL DEFAULT 'Нимай',
  `secondname` varchar(15) NOT NULL DEFAULT 'Махапрабху',
  `birth` varchar(10) NOT NULL DEFAULT '07.08.1983',
  `country_id` int(11) DEFAULT 1,
  `city_id` varchar(27) DEFAULT '1',
  `city` varchar(39) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL DEFAULT '1',
  `avatar` varchar(50) NOT NULL DEFAULT '/img/avatars/defava0.png',
  `changets` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `guru1name` varchar(20) NOT NULL DEFAULT 'Палько С.А.',
  `guru2name` varchar(20) NOT NULL DEFAULT 'Палько А.Г.',
  `ishideordel` int(11) NOT NULL DEFAULT 0,
  `actionend` int(11) NOT NULL DEFAULT 0,
  `place` int(3) DEFAULT NULL COMMENT 'flow att place',
  `flow_` tinyint(3) DEFAULT NULL COMMENT 'null - новый Атлет \r\n         1 - Выступает (сейчас Атлет в потоке выступления)\r\n         2 - Выступил ( Атлет уже выступил, скрыт)',
  `country_` enum('rus','ukr','kaz','uzb','usa','arm','grg') NOT NULL DEFAULT 'rus',
  `wcat_` varchar(5) NOT NULL DEFAULT '102+',
  `bkp_creation` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `_v7athlete`
--

INSERT INTO `_v7athlete` (`id`, `op`, `nextop`, `prevop`, `weightnow`, `exnow`, `trynow`, `serialnumber`, `sex`, `ownweight`, `wcat_id`, `rank_id`, `info_id`, `newrank`, `score`, `sincler`, `position`, `snatch1`, `snatch1isget`, `s1d`, `s1ch1`, `s1ch2`, `s1ch3`, `snatch2`, `snatch2isget`, `s2d`, `s2ai`, `s2ch1`, `s2ch2`, `snatch3`, `snatch3isget`, `s3d`, `s3ai`, `s3ch1`, `s3ch2`, `snatchresult`, `snatch_place`, `cleanjerk1`, `cleanjerk1isget`, `cleanjerk1d`, `cleanjerk1ch1`, `cleanjerk1ch2`, `cleanjerk1ch3`, `cleanjerk2`, `cleanjerk2isget`, `cleanjerk2d`, `cleanjerk2ai`, `cleanjerk2ch1`, `cleanjerk2ch2`, `cleanjerk3`, `cleanjerk3isget`, `cleanjerk3d`, `cleanjerk3ai`, `cleanjerk3ch1`, `cleanjerk3ch2`, `cleanjerkresult`, `cleanjerk_place`, `doublesum`, `firstname`, `secondname`, `birth`, `country_id`, `city_id`, `city`, `avatar`, `changets`, `guru1name`, `guru2name`, `ishideordel`, `actionend`, `place`, `flow_`, `country_`, `wcat_`, `bkp_creation`) VALUES
(1, 0, 0, 0, 44, 's1', 0, NULL, 1, 72.8, 34, 34, 1, NULL, NULL, '', NULL, 44, NULL, 44, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 2, 235, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 1, 0, 'Гаура́нга', 'Нитьяна́нда', '07.03.1486', 1, '1', 'Сургут', '/img/avatars/defava11.png', '2023-03-15 17:28:44', 'Палькодзян С.А.', 'Палько А.Г.', 0, 1, 2, 2, 'rus', '102+', ''),
(2, 0, 0, 0, 68, 's1', 0, NULL, 1, 69.7, 34, 34, 1, NULL, NULL, '', NULL, 68, NULL, 68, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 3, 103, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 2, 0, 'Сержиоу', 'Чанчик', '', 1, '1', 'Вриндаван', '/img/avatars/defava0.png', '2023-03-15 17:28:44', 'Палько С.А.', 'Палько А.Г.', 0, 1, 3, 2, 'rus', '102+', ''),
(3, 0, 0, 0, 88, 's1', 0, NULL, 1, 69.7, 34, 34, 1, NULL, NULL, '', NULL, 88, NULL, 88, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 191, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 3, 0, 'Николя́', 'Шпаку́', '', 1, '1', 'Вриндаван', '/img/avatars/defava0.png', '2023-03-15 17:28:44', 'Палько С.А.', 'Палько А.Г.', 0, 1, 4, 2, 'rus', '102+', ''),
(4, 0, 0, 0, 0, 'j2', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 50, 1, 50, NULL, NULL, NULL, 51, 0, 51, NULL, NULL, NULL, 51, 1, 51, NULL, NULL, NULL, 51, 1, 66, 0, 66, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 51, 'Олег', 'Альфреди', '', 1, '1', 'Сургут', '/img/avatars/defava0.png', '2023-03-15 17:28:44', 'Палько С.А.', 'Палько А.Г.', 0, 1, 1, 2, 'rus', '102+', ''),
(5, 1, 0, 0, 64, 's2', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 55, 0, 55, NULL, NULL, NULL, 64, NULL, 55, NULL, 56, 64, NULL, NULL, NULL, NULL, NULL, NULL, 0, 5, 66, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 5, 0, 'ghfgh', 'hgfh', '', 1, '1', 'ОМСК', '/img/avatars/defava0.png', '2023-03-15 17:28:44', 'Палько С.А.', 'Палько А.Г.', 0, 1, 5, 2, 'rus', '102+', ''),
(6, 0, 1, 0, 58, 's1', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 58, NULL, 55, 58, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 6, 66, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 6, 0, 'Санечка', 'Попов', '', 1, '1', 'Солнечный', '/img/avatars/defava0.png', '2023-03-15 17:28:44', 'Палько С.А.', 'Палько А.Г.', 0, 1, 6, 2, 'rus', '102+', ''),
(7, 0, 0, 0, 48, 's1', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 48, NULL, 48, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 7, 66, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 7, 0, 'Ябударов', 'Ильсун', '', 100, '1', 'Вартовск', '/img/avatars/defava0.png', '2023-03-15 17:28:44', 'Палько С.А.', 'Палько А.Г.', 0, 1, 7, 2, 'rus', '102+', ''),
(8, 0, 0, 0, 45, 's1', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 45, NULL, 45, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 8, 78, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 8, 0, 'Яфаров', 'Гюзбар', '', 1, '1', 'Покачи', '/img/avatars/defava0.png', '2023-03-15 17:28:44', 'Палько С.А.', 'Палько А.Г.', 0, 1, 8, 2, 'rus', '102+', ''),
(9, 0, 0, 0, 33, 's1', 0, NULL, 1, 69.7, 34, 34, 1, NULL, NULL, '', NULL, 33, NULL, 33, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 9, 72, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 9, 0, 'Шьям', 'Чандра', '', 1, '1', 'Лангепас', '/img/avatars/defava0.png', '2023-03-15 17:28:44', 'Палько С.А.', 'Палько А.Г.', 0, 1, 9, 2, 'rus', '102+', ''),
(10, 0, 0, 0, 55, 's1', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 55, NULL, 55, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 10, 67, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 10, 0, 'Питюнидзе', 'Фамилий', '', 1, '1', ' Лангепас  ', '/img/avatars/defava0.png', '2023-03-15 17:28:44', 'Палько С.А.', 'Палько А.Г.', 0, 1, 10, 2, 'rus', '102+', '');

-- --------------------------------------------------------

--
-- Структура таблицы `__v7bkp_2023020119434501`
--

CREATE TABLE `__v7bkp_2023020119434501` (
  `id` int(11) NOT NULL,
  `op` int(11) NOT NULL DEFAULT 0,
  `nextop` int(11) NOT NULL DEFAULT 0,
  `prevop` int(11) NOT NULL DEFAULT 0,
  `weightnow` int(11) NOT NULL DEFAULT 0,
  `exnow` enum('s1','s2','s3','j1','j2','j3','finished') NOT NULL DEFAULT 's1',
  `trynow` int(11) DEFAULT 0,
  `serialnumber` int(11) DEFAULT NULL,
  `sex` int(11) NOT NULL DEFAULT 1,
  `ownweight` float(10,1) NOT NULL DEFAULT 72.8,
  `wcat_id` int(5) DEFAULT 1,
  `rank_id` int(11) DEFAULT 0,
  `info_id` int(11) DEFAULT 1,
  `newrank` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `sincler` varchar(15) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `position` int(11) DEFAULT NULL,
  `snatch1` int(11) NOT NULL DEFAULT 44,
  `snatch1isget` tinyint(3) DEFAULT NULL,
  `s1d` int(11) DEFAULT NULL,
  `s1ch1` int(11) DEFAULT NULL,
  `s1ch2` int(11) DEFAULT NULL,
  `s1ch3` int(11) DEFAULT NULL,
  `snatch2` int(11) DEFAULT NULL,
  `snatch2isget` tinyint(3) DEFAULT NULL,
  `s2d` int(11) DEFAULT NULL,
  `s2ai` int(11) DEFAULT NULL,
  `s2ch1` int(11) DEFAULT NULL,
  `s2ch2` int(11) DEFAULT NULL,
  `snatch3` int(11) DEFAULT NULL,
  `snatch3isget` tinyint(3) DEFAULT NULL,
  `s3d` int(11) DEFAULT NULL,
  `s3ai` int(11) DEFAULT NULL,
  `s3ch1` int(11) DEFAULT NULL,
  `s3ch2` int(11) DEFAULT NULL,
  `snatchresult` int(11) DEFAULT 0,
  `snatch_place` int(3) DEFAULT NULL COMMENT 'snatch place',
  `cleanjerk1` int(11) NOT NULL DEFAULT 55,
  `cleanjerk1isget` tinyint(3) DEFAULT NULL,
  `cleanjerk1d` int(11) DEFAULT NULL,
  `cleanjerk1ch1` int(11) DEFAULT NULL,
  `cleanjerk1ch2` int(11) DEFAULT NULL,
  `cleanjerk1ch3` int(11) DEFAULT NULL,
  `cleanjerk2` int(11) DEFAULT NULL,
  `cleanjerk2isget` tinyint(3) DEFAULT NULL,
  `cleanjerk2d` int(11) DEFAULT NULL,
  `cleanjerk2ai` int(11) DEFAULT NULL,
  `cleanjerk2ch1` int(11) DEFAULT NULL,
  `cleanjerk2ch2` int(11) DEFAULT NULL,
  `cleanjerk3` int(11) DEFAULT NULL,
  `cleanjerk3isget` tinyint(3) DEFAULT NULL,
  `cleanjerk3d` int(11) DEFAULT NULL,
  `cleanjerk3ai` int(11) DEFAULT NULL,
  `cleanjerk3ch1` int(11) DEFAULT NULL,
  `cleanjerk3ch2` int(11) DEFAULT NULL,
  `cleanjerkresult` int(11) DEFAULT 0,
  `cleanjerk_place` int(3) DEFAULT NULL COMMENT 'clean&jerk place',
  `doublesum` int(11) DEFAULT 0,
  `firstname` varchar(15) NOT NULL DEFAULT 'Нимай',
  `secondname` varchar(15) NOT NULL DEFAULT 'Махапрабху',
  `birth` varchar(10) NOT NULL DEFAULT '07.08.1983',
  `country_id` int(11) DEFAULT 1,
  `city_id` varchar(27) DEFAULT '1',
  `city` varchar(39) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL DEFAULT '1',
  `avatar` varchar(50) NOT NULL DEFAULT '/img/avatars/defava0.png',
  `changets` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `guru1name` varchar(20) NOT NULL DEFAULT 'Палько С.А.',
  `guru2name` varchar(20) NOT NULL DEFAULT 'Палько А.Г.',
  `ishideordel` int(11) NOT NULL DEFAULT 0,
  `actionend` int(11) NOT NULL DEFAULT 0,
  `place` int(3) DEFAULT NULL COMMENT 'flow att place',
  `flow_` tinyint(3) DEFAULT NULL COMMENT 'null - новый Атлет \r\n         1 - Выступает (сейчас Атлет в потоке выступления)\r\n         2 - Выступил ( Атлет уже выступил, скрыт)',
  `country_` enum('rus','ukr','kaz','uzb','usa','arm','grg') NOT NULL DEFAULT 'rus',
  `wcat_` varchar(5) NOT NULL DEFAULT '102+',
  `bkp_creation` timestamp(6) NOT NULL DEFAULT current_timestamp(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `__v7bkp_2023020119434501`
--

INSERT INTO `__v7bkp_2023020119434501` (`id`, `op`, `nextop`, `prevop`, `weightnow`, `exnow`, `trynow`, `serialnumber`, `sex`, `ownweight`, `wcat_id`, `rank_id`, `info_id`, `newrank`, `score`, `sincler`, `position`, `snatch1`, `snatch1isget`, `s1d`, `s1ch1`, `s1ch2`, `s1ch3`, `snatch2`, `snatch2isget`, `s2d`, `s2ai`, `s2ch1`, `s2ch2`, `snatch3`, `snatch3isget`, `s3d`, `s3ai`, `s3ch1`, `s3ch2`, `snatchresult`, `snatch_place`, `cleanjerk1`, `cleanjerk1isget`, `cleanjerk1d`, `cleanjerk1ch1`, `cleanjerk1ch2`, `cleanjerk1ch3`, `cleanjerk2`, `cleanjerk2isget`, `cleanjerk2d`, `cleanjerk2ai`, `cleanjerk2ch1`, `cleanjerk2ch2`, `cleanjerk3`, `cleanjerk3isget`, `cleanjerk3d`, `cleanjerk3ai`, `cleanjerk3ch1`, `cleanjerk3ch2`, `cleanjerkresult`, `cleanjerk_place`, `doublesum`, `firstname`, `secondname`, `birth`, `country_id`, `city_id`, `city`, `avatar`, `changets`, `guru1name`, `guru2name`, `ishideordel`, `actionend`, `place`, `flow_`, `country_`, `wcat_`, `bkp_creation`) VALUES
(1, 1, 0, 0, 44, 's1', 0, NULL, 1, 72.8, 1, 0, 1, NULL, NULL, '', NULL, 44, NULL, 44, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 55, NULL, 55, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 0, 'Гаура́нга', 'Нитьяна́нда', '07.03.1486', 1, '1', '1', '/img/avatars/defava11.png', '2023-02-01 14:43:15', 'Палькодзян С.А.', 'Палько А.Г.', 0, 0, 0, 1, 'rus', '102+', '2023-02-01 14:43:45.407953'),
(5, 0, 0, 0, 108, 's2', 0, NULL, 1, 69.5, 33, 0, 1, NULL, 108, '', 1, 77, 1, 44, 77, 77, NULL, 108, NULL, 78, NULL, 99, 108, NULL, NULL, NULL, NULL, NULL, NULL, 77, 4, 55, 1, 55, NULL, NULL, NULL, 59, NULL, 59, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 55, 1, 132, 'Ш́рӣла дас', 'Прабхупа̄да', '07.08.1983', 71, '8', 'Вриндаван', '/img/avatars/defava5.png', '2023-02-01 14:43:14', 'fdsfds', 'Палько А.Г.', 0, 0, 1, 1, 'rus', '102+', '2023-02-01 14:43:45.407953'),
(6, 0, 0, 0, 72, 's2', 0, NULL, 1, 72.8, 25, 0, 1, NULL, NULL, '', NULL, 70, 0, 44, 54, 70, NULL, 72, NULL, 70, NULL, 72, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 55, NULL, 55, NULL, NULL, NULL, 64, NULL, 64, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 0, 'Вриндаван дас', 'Тхакур', '05.02.1983', 15, '1', 'Лангепас', '/img/avatars/defava7.png', '2023-02-01 14:43:15', 'Палько С.А.', 'Палько А.Г.', 0, 0, 0, 1, 'rus', '102+', '2023-02-01 14:43:45.407953'),
(12, 0, 0, 0, 89, 's1', 0, NULL, 1, 72.8, 26, 0, 1, NULL, NULL, '', NULL, 89, NULL, 44, 89, 89, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 53, 1, 53, NULL, NULL, NULL, 62, NULL, 62, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 53, 2, 53, 'Рупа дас', 'Госвами', '07.08.1983', 2, '1', 'Лангепас', '/img/avatars/defava.png', '2023-02-01 14:43:14', 'Палько С.А.', 'Палько А.Г.', 0, 0, 7, 1, 'rus', '102+', '2023-02-01 14:43:45.407953'),
(16, 0, 0, 0, 28, 'j1', 0, NULL, 1, 108.0, 23, 0, 1, NULL, NULL, '', NULL, 28, 1, 44, 28, NULL, NULL, 29, 1, 29, NULL, NULL, NULL, 30, 0, 30, NULL, NULL, NULL, 29, 0, 55, NULL, 55, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 29, 'Санатана дас', 'Госвами', '07.08.1983', 71, '1', 'Джессор', '/img/avatars/defava.png', '2023-02-01 14:43:14', 'Палько С.А.', 'Палько А.Г.', 0, 0, 0, 1, 'rus', '102+', '2023-02-01 14:43:45.407953'),
(17, 0, 1, 0, 51, 's3', 0, NULL, 1, 72.8, 30, 0, 1, NULL, NULL, '', NULL, 44, 1, 44, NULL, NULL, NULL, 55, 1, 51, NULL, 55, NULL, 51, NULL, 46, NULL, 51, 51, 55, 5, 99, NULL, 99, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 55, 'Рагхунатха дас', 'Бхатта', '07.08.1983', 2, '1', 'Лангепас', '/img/avatars/defava.png', '2023-02-01 14:43:15', 'Палько С.А.', 'Палько А.Г.', 0, 0, 6, 1, 'rus', '102+', '2023-02-01 14:43:45.407953'),
(19, 0, 0, 0, 23, 'j1', 0, NULL, 1, 72.8, 7, 0, 1, NULL, NULL, '', NULL, 23, 1, 44, 53, 23, NULL, 24, 1, 24, NULL, NULL, NULL, 25, 1, 25, NULL, NULL, NULL, 25, 0, 55, NULL, 55, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 25, 'Джива дас', 'Госвами', '07.08.1983', 1, '1', 'Лангепас', '/img/avatars/defava.png', '2023-02-01 14:43:14', 'Палько С.А.', 'Палько А.Г.', 0, 0, 0, 1, 'rus', '102+', '2023-02-01 14:43:45.407953'),
(20, 0, 0, 0, 22, 'j1', 0, NULL, 1, 72.8, 32, 0, 1, NULL, NULL, '', NULL, 22, 1, 44, 53, 22, NULL, 23, 1, 23, NULL, NULL, NULL, 24, 1, 24, NULL, NULL, NULL, 24, 0, 55, NULL, 55, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 24, 'Шьямананда дас', 'Госвами', '07.08.1983', 1, '1', 'Лангепас', '/img/avatars/defava.png', '2023-02-01 14:43:14', 'Палько С.А.', 'Палько А.Г.', 0, 0, 0, 1, 'rus', '102+', '2023-02-01 14:43:45.407953'),
(21, 0, 0, 0, 23, 'j1', 0, NULL, 1, 72.8, 26, 0, 1, NULL, NULL, '', NULL, 44, 1, 44, NULL, NULL, NULL, 23, 0, 47, NULL, 53, 23, 31, 1, 31, NULL, NULL, NULL, 44, 7, 55, NULL, 55, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 44, 'Нароттама дас', 'Тхакур', '07.08.1983', 1, '10', 'Бангладеш', '/img/avatars/defava.png', '2023-02-01 14:43:14', 'Палько С.А.', 'Палько А.Г.', 0, 0, 0, 1, 'rus', '102+', '2023-02-01 14:43:45.407953'),
(22, 0, 0, 0, 113, 's2', 0, NULL, 1, 72.8, 23, 0, 1, NULL, NULL, '', NULL, 48, 1, 44, 31, 48, NULL, 113, NULL, 49, NULL, 113, 113, NULL, NULL, NULL, NULL, NULL, NULL, 48, 6, 55, NULL, 55, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 48, 'Бхактивинода да', 'Тхакур', '07.08.1983', 1, '9', 'Бирнагар', '/img/avatars/defava.png', '2023-02-01 14:43:15', 'Палько С.А.', 'Палько А.Г.', 0, 0, 0, 1, 'rus', '102+', '2023-02-01 14:43:45.407953'),
(24, 0, 0, 0, 89, 's2', 0, NULL, 1, 72.8, 29, 0, 1, NULL, NULL, '', NULL, 48, 1, 44, 36, 48, NULL, 89, NULL, 49, NULL, 89, 89, NULL, NULL, NULL, NULL, NULL, NULL, 48, 6, 55, NULL, 55, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 48, 'Бхактисиддханта', 'Сарасвати', '07.08.1983', 1, '8', 'Маяпур', '/img/avatars/defava7.png', '2023-02-01 14:43:15', 'Палько С.А.', 'Палько А.Г.', 0, 0, 0, 1, 'rus', '102+', '2023-02-01 14:43:45.407953'),
(34, 0, 0, 0, 45, 's2', 0, NULL, 1, 72.8, 20, 0, 1, NULL, NULL, '', NULL, 44, 1, 44, NULL, NULL, NULL, 108, NULL, 108, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 44, 7, 55, NULL, 55, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 44, 'Чандра Чаран', 'Чайтанья', '07.08.1983', 1, '7', 'Георгиевка', '/img/avatars/defava9.png', '2023-02-01 14:43:15', 'Палько С.А.', 'Палько А.Г.', 0, 0, 0, 1, 'rus', '102+', '2023-02-01 14:43:45.407953'),
(35, 0, 0, 0, 36, 'j2', 0, NULL, 1, 99.9, 34, 0, 1, NULL, NULL, '', NULL, 35, 1, 44, 35, 35, NULL, 35, 1, 35, NULL, 35, 35, 36, 1, 36, NULL, 36, 36, 36, 0, 41, 1, 55, 41, 41, NULL, 42, NULL, 42, NULL, 42, 42, NULL, NULL, NULL, NULL, NULL, NULL, 41, 3, 77, 'Раса дас', 'Расика', '02.01.2023', 17, '3', 'ОМск', '/img/avatars/defava8.png', '2023-02-01 14:43:15', 'Палько С.А.', 'Палько А.Г.', 0, 1, 5, 2, 'rus', '102+', '2023-02-01 14:43:45.407953'),
(42, 0, 0, 0, 121, 's2', 0, NULL, 1, 69.7, 25, 0, 1, NULL, 100, '', NULL, 121, 1, 222, 121, 121, NULL, 121, NULL, 108, NULL, 121, 121, 121, NULL, 121, NULL, 121, 121, 121, 2, 255, NULL, 255, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 121, 'Индрадьюмна дас', 'Свами', '', 1, '6', 'Пало-Алто', '/img/avatars/defava.png', '2023-02-01 14:43:15', 'Палько С.А.', 'Палько А.Г.', 0, 0, 3, 1, 'rus', '102+', '2023-02-01 14:43:45.407953'),
(54, 0, 0, 0, 141, 'finished', 0, NULL, 1, 69.7, 30, 0, 1, NULL, NULL, '', NULL, 141, -1, 141, NULL, NULL, NULL, 141, -1, 141, NULL, NULL, NULL, 141, -1, 141, NULL, 141, 141, 0, 0, 123, -1, 123, NULL, NULL, NULL, 124, -1, 124, NULL, 124, 124, 124, -1, 124, NULL, 124, 124, 0, 4, 0, 'Никитос', 'Гелюшонок', '', 1, '1', ' Локация:  ', '/img/avatars/defava0.png', '2023-02-01 14:43:14', 'Палько С.А.', 'Палько А.Г.', 0, 1, 0, 2, 'rus', '102+', '2023-02-01 14:43:45.407953'),
(55, 0, 0, 0, 234, 'j1', 0, NULL, 1, 69.7, 27, 0, 1, NULL, NULL, '', NULL, 190, -1, 190, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 234, NULL, 234, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 0, 'Иванов', 'Иван', '', 1, '1', ' Локация:  ', '/img/avatars/defava8.png', '2023-02-01 14:43:14', 'Палько С.А.', 'Палько А.Г.', 0, 0, 0, 2, 'rus', '102+', '2023-02-01 14:43:45.407953'),
(57, 0, 0, 0, 57, 'j1', 0, NULL, 1, 69.7, 25, 0, 1, NULL, NULL, '', NULL, 57, -1, 44, 57, NULL, NULL, 58, -1, 58, NULL, NULL, NULL, NULL, -1, NULL, NULL, NULL, NULL, 0, 0, 66, -1, 66, NULL, NULL, NULL, NULL, -1, NULL, NULL, NULL, NULL, NULL, -1, NULL, NULL, NULL, NULL, 0, 4, 0, 'Пипачкин', 'Буба', '', 1, '1', ' Локация:  ', '/img/avatars/defava.png', '2023-02-01 14:43:14', 'Палько С.А.', 'Палько А.Г.', 0, 0, 0, 2, 'rus', '102+', '2023-02-01 14:43:45.407953'),
(59, 0, 0, 0, 146, 's3', 0, NULL, 1, 69.7, 28, 0, 1, NULL, NULL, '', NULL, 74, 1, 88, 74, 74, NULL, 124, 1, 110, NULL, 124, 124, 146, NULL, 111, NULL, 146, 146, 124, 1, 102, NULL, 99, 102, 102, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 124, 'Нада', 'Вавада', '', 1, '1', ' Локация:  ', '/img/avatars/defava.png', '2023-02-01 14:43:15', 'Палько С.А.', 'Палько А.Г.', 0, 0, 2, 2, 'rus', '102+', '2023-02-01 14:43:45.407953'),
(61, 0, 0, 0, 124, 's2', 0, NULL, 1, 69.7, 1, 0, 1, NULL, NULL, '', NULL, 79, 0, 77, 78, 79, NULL, 124, NULL, 79, NULL, 124, 124, NULL, NULL, NULL, NULL, NULL, NULL, 0, 0, 88, NULL, 88, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 0, 'яфяфяфяф', 'фыфыыфы', '', 1, '1', ' Локация:  ', '/img/avatars/defava.png', '2023-02-01 14:43:15', 'Палько С.А.', 'Палько А.Г.', 0, 0, 0, 2, 'rus', '102+', '2023-02-01 14:43:45.407953'),
(62, 0, 0, 0, 109, 's2', 0, NULL, 1, 69.7, 1, 0, 1, NULL, NULL, '', NULL, 108, 1, 108, NULL, NULL, NULL, 109, NULL, 109, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 108, 3, 208, NULL, 208, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 108, 'Лаптев', 'Дмитрий', '', 1, '1', ' Локация:  ', '/img/avatars/defava0.png', '2023-02-01 14:43:14', 'Палько С.А.', 'Палько А.Г.', 0, 0, 4, 2, 'rus', '102+', '2023-02-01 14:43:45.407953');

-- --------------------------------------------------------

--
-- Структура таблицы `__v7bkp_2023030405202704`
--

CREATE TABLE `__v7bkp_2023030405202704` (
  `id` int(11) NOT NULL,
  `op` int(11) NOT NULL DEFAULT 0,
  `nextop` int(11) NOT NULL DEFAULT 0,
  `prevop` int(11) NOT NULL DEFAULT 0,
  `weightnow` int(11) NOT NULL DEFAULT 0,
  `exnow` enum('s1','s2','s3','j1','j2','j3','finished') NOT NULL DEFAULT 's1',
  `trynow` int(11) DEFAULT 0,
  `serialnumber` int(11) DEFAULT NULL,
  `sex` int(11) NOT NULL DEFAULT 1,
  `ownweight` float(10,1) NOT NULL DEFAULT 72.8,
  `wcat_id` int(5) DEFAULT 1,
  `rank_id` int(11) DEFAULT 0,
  `info_id` int(11) DEFAULT 1,
  `newrank` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `sincler` varchar(15) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `position` int(11) DEFAULT NULL,
  `snatch1` int(11) NOT NULL DEFAULT 44,
  `snatch1isget` tinyint(3) DEFAULT NULL,
  `s1d` int(11) DEFAULT NULL,
  `s1ch1` int(11) DEFAULT NULL,
  `s1ch2` int(11) DEFAULT NULL,
  `s1ch3` int(11) DEFAULT NULL,
  `snatch2` int(11) DEFAULT NULL,
  `snatch2isget` tinyint(3) DEFAULT NULL,
  `s2d` int(11) DEFAULT NULL,
  `s2ai` int(11) DEFAULT NULL,
  `s2ch1` int(11) DEFAULT NULL,
  `s2ch2` int(11) DEFAULT NULL,
  `snatch3` int(11) DEFAULT NULL,
  `snatch3isget` tinyint(3) DEFAULT NULL,
  `s3d` int(11) DEFAULT NULL,
  `s3ai` int(11) DEFAULT NULL,
  `s3ch1` int(11) DEFAULT NULL,
  `s3ch2` int(11) DEFAULT NULL,
  `snatchresult` int(11) DEFAULT 0,
  `snatch_place` int(3) DEFAULT NULL COMMENT 'snatch place',
  `cleanjerk1` int(11) NOT NULL DEFAULT 55,
  `cleanjerk1isget` tinyint(3) DEFAULT NULL,
  `cleanjerk1d` int(11) DEFAULT NULL,
  `cleanjerk1ch1` int(11) DEFAULT NULL,
  `cleanjerk1ch2` int(11) DEFAULT NULL,
  `cleanjerk1ch3` int(11) DEFAULT NULL,
  `cleanjerk2` int(11) DEFAULT NULL,
  `cleanjerk2isget` tinyint(3) DEFAULT NULL,
  `cleanjerk2d` int(11) DEFAULT NULL,
  `cleanjerk2ai` int(11) DEFAULT NULL,
  `cleanjerk2ch1` int(11) DEFAULT NULL,
  `cleanjerk2ch2` int(11) DEFAULT NULL,
  `cleanjerk3` int(11) DEFAULT NULL,
  `cleanjerk3isget` tinyint(3) DEFAULT NULL,
  `cleanjerk3d` int(11) DEFAULT NULL,
  `cleanjerk3ai` int(11) DEFAULT NULL,
  `cleanjerk3ch1` int(11) DEFAULT NULL,
  `cleanjerk3ch2` int(11) DEFAULT NULL,
  `cleanjerkresult` int(11) DEFAULT 0,
  `cleanjerk_place` int(3) DEFAULT NULL COMMENT 'clean&jerk place',
  `doublesum` int(11) DEFAULT 0,
  `firstname` varchar(15) NOT NULL DEFAULT 'Нимай',
  `secondname` varchar(15) NOT NULL DEFAULT 'Махапрабху',
  `birth` varchar(10) NOT NULL DEFAULT '07.08.1983',
  `country_id` int(11) DEFAULT 1,
  `city_id` varchar(27) DEFAULT '1',
  `city` varchar(39) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL DEFAULT '1',
  `avatar` varchar(50) NOT NULL DEFAULT '/img/avatars/defava0.png',
  `changets` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `guru1name` varchar(20) NOT NULL DEFAULT 'Палько С.А.',
  `guru2name` varchar(20) NOT NULL DEFAULT 'Палько А.Г.',
  `ishideordel` int(11) NOT NULL DEFAULT 0,
  `actionend` int(11) NOT NULL DEFAULT 0,
  `place` int(3) DEFAULT NULL COMMENT 'flow att place',
  `flow_` tinyint(3) DEFAULT NULL COMMENT 'null - новый Атлет \r\n         1 - Выступает (сейчас Атлет в потоке выступления)\r\n         2 - Выступил ( Атлет уже выступил, скрыт)',
  `country_` enum('rus','ukr','kaz','uzb','usa','arm','grg') NOT NULL DEFAULT 'rus',
  `wcat_` varchar(5) NOT NULL DEFAULT '102+',
  `bkp_creation` timestamp(6) NOT NULL DEFAULT current_timestamp(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `__v7bkp_2023030405202704`
--

INSERT INTO `__v7bkp_2023030405202704` (`id`, `op`, `nextop`, `prevop`, `weightnow`, `exnow`, `trynow`, `serialnumber`, `sex`, `ownweight`, `wcat_id`, `rank_id`, `info_id`, `newrank`, `score`, `sincler`, `position`, `snatch1`, `snatch1isget`, `s1d`, `s1ch1`, `s1ch2`, `s1ch3`, `snatch2`, `snatch2isget`, `s2d`, `s2ai`, `s2ch1`, `s2ch2`, `snatch3`, `snatch3isget`, `s3d`, `s3ai`, `s3ch1`, `s3ch2`, `snatchresult`, `snatch_place`, `cleanjerk1`, `cleanjerk1isget`, `cleanjerk1d`, `cleanjerk1ch1`, `cleanjerk1ch2`, `cleanjerk1ch3`, `cleanjerk2`, `cleanjerk2isget`, `cleanjerk2d`, `cleanjerk2ai`, `cleanjerk2ch1`, `cleanjerk2ch2`, `cleanjerk3`, `cleanjerk3isget`, `cleanjerk3d`, `cleanjerk3ai`, `cleanjerk3ch1`, `cleanjerk3ch2`, `cleanjerkresult`, `cleanjerk_place`, `doublesum`, `firstname`, `secondname`, `birth`, `country_id`, `city_id`, `city`, `avatar`, `changets`, `guru1name`, `guru2name`, `ishideordel`, `actionend`, `place`, `flow_`, `country_`, `wcat_`, `bkp_creation`) VALUES
(1, 0, 0, 0, 55, 'j1', 0, NULL, 1, 72.8, 34, 34, 1, NULL, NULL, '', NULL, 44, 0, 44, NULL, NULL, NULL, 45, 0, NULL, NULL, 45, 45, 46, 0, NULL, NULL, 46, 46, 0, 6, 55, NULL, 55, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 1, 0, 'Гаура́нга', 'Нитьяна́нда', '07.03.1486', 1, '1', 'Вриндаван', '/img/avatars/defava11.png', '2023-03-04 00:20:14', 'Палькодзян С.А.', 'Палько А.Г.', 0, 0, 6, 1, 'rus', '102+', '2023-03-04 00:20:27.752255'),
(2, 0, 1, 0, 40, 'j1', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 39, 1, 30, 36, 39, NULL, 41, 0, NULL, NULL, 41, 41, 40, 1, NULL, NULL, 40, 40, 40, 4, 40, NULL, 40, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 2, 40, 'Лаптев', 'Евгений', '', 71, '1', ' Локация:  ', '/img/avatars/defava0.png', '2023-03-04 00:20:14', 'Палько С.А.', 'Палько А.Г.', 0, 0, 4, 1, 'rus', '102+', '2023-03-04 00:20:27.752255'),
(3, 0, 0, 0, 40, 'j1', 0, NULL, 1, 99.7, 34, 34, 1, NULL, NULL, '', NULL, 48, 1, 30, 48, NULL, NULL, 50, 0, NULL, NULL, 50, 50, 51, 1, NULL, NULL, 51, 51, 51, 2, 40, NULL, 40, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 3, 51, 'Рябов', 'Дмитрий', '', 71, '1', 'OMck', '/img/avatars/defava0.png', '2023-03-04 00:20:14', 'Палько С.А.', 'Палько А.Г.', 0, 0, 2, 1, 'rus', '102+', '2023-03-04 00:20:27.752255'),
(4, 0, 0, 0, 40, 'j1', 0, NULL, 1, 69.7, 34, 34, 1, NULL, NULL, '', NULL, 35, 0, 30, 35, 35, NULL, 36, 1, NULL, NULL, 36, 36, 38, 0, NULL, NULL, 38, 38, 36, 5, 40, NULL, 40, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 36, 'Осипов', 'Константин', '', 2, '1', 'Hhcghff', '/img/avatars/defava0.png', '2023-03-04 00:20:14', 'Палько С.А.', 'Палько А.Г.', 0, 0, 5, 1, 'rus', '102+', '2023-03-04 00:20:27.752255'),
(5, 0, 0, 0, 43, 'j1', 0, NULL, 1, 103.7, 32, 32, 1, NULL, NULL, '', NULL, 45, 1, 45, NULL, NULL, NULL, 47, 1, NULL, NULL, 47, 47, 49, 1, NULL, NULL, 49, 49, 49, 3, 43, NULL, 43, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 5, 49, 'Карагачан', 'Сергей', '', 1, '1', 'Славянск', '/img/avatars/defava0.png', '2023-03-04 00:20:14', 'Палько С.А.', 'Палько А.Г.', 0, 0, 3, 1, 'rus', '102+', '2023-03-04 00:20:27.752255'),
(6, 0, 0, 0, 148, 'j1', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 122, 0, 122, NULL, NULL, NULL, 123, 0, NULL, NULL, 123, 123, 124, 0, NULL, NULL, 124, 124, 0, 7, 148, NULL, 148, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 6, 0, 'Кроса́учэг', 'Романюга', '', 1, '1', 'Самара', '/img/avatars/defava0.png', '2023-03-04 00:20:14', 'Палько С.А.', 'Палько А.Г.', 0, 0, 7, 1, 'rus', '102+', '2023-03-04 00:20:27.752255'),
(7, 0, 0, 0, 188, 'j1', 0, NULL, 1, 69.7, 34, 34, 1, NULL, NULL, '', NULL, 108, 1, 108, NULL, NULL, NULL, 110, 0, NULL, NULL, 110, 110, 111, 0, NULL, NULL, 111, 111, 108, 1, 188, NULL, 188, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 7, 108, 'Давлетгареев', 'Альберт', '', 1, '1', 'Babu', '/img/avatars/defava0.png', '2023-03-04 00:20:14', 'Палько С.А.', 'Палько А.Г.', 0, 0, 1, 1, 'rus', '102+', '2023-03-04 00:20:27.752255'),
(8, 1, 0, 0, 34, 'j1', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 48, 0, 48, NULL, NULL, NULL, 46, 0, NULL, NULL, 46, 46, 48, 0, NULL, NULL, 48, 48, 0, 8, 34, NULL, 34, 34, 34, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 8, 0, 'Бубарин', 'Бибуля', '', 1, '1', 'Иволга', '/img/avatars/defava0.png', '2023-03-04 00:20:14', 'Палько С.А.', 'Палько А.Г.', 0, 1, 8, 2, 'rus', '102+', '2023-03-04 00:20:27.752255');

-- --------------------------------------------------------

--
-- Структура таблицы `__v7bkp_2023030407085304`
--

CREATE TABLE `__v7bkp_2023030407085304` (
  `id` int(11) NOT NULL,
  `op` int(11) NOT NULL DEFAULT 0,
  `nextop` int(11) NOT NULL DEFAULT 0,
  `prevop` int(11) NOT NULL DEFAULT 0,
  `weightnow` int(11) NOT NULL DEFAULT 0,
  `exnow` enum('s1','s2','s3','j1','j2','j3','finished') NOT NULL DEFAULT 's1',
  `trynow` int(11) DEFAULT 0,
  `serialnumber` int(11) DEFAULT NULL,
  `sex` int(11) NOT NULL DEFAULT 1,
  `ownweight` float(10,1) NOT NULL DEFAULT 72.8,
  `wcat_id` int(5) DEFAULT 1,
  `rank_id` int(11) DEFAULT 0,
  `info_id` int(11) DEFAULT 1,
  `newrank` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `sincler` varchar(15) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `position` int(11) DEFAULT NULL,
  `snatch1` int(11) NOT NULL DEFAULT 44,
  `snatch1isget` tinyint(3) DEFAULT NULL,
  `s1d` int(11) DEFAULT NULL,
  `s1ch1` int(11) DEFAULT NULL,
  `s1ch2` int(11) DEFAULT NULL,
  `s1ch3` int(11) DEFAULT NULL,
  `snatch2` int(11) DEFAULT NULL,
  `snatch2isget` tinyint(3) DEFAULT NULL,
  `s2d` int(11) DEFAULT NULL,
  `s2ai` int(11) DEFAULT NULL,
  `s2ch1` int(11) DEFAULT NULL,
  `s2ch2` int(11) DEFAULT NULL,
  `snatch3` int(11) DEFAULT NULL,
  `snatch3isget` tinyint(3) DEFAULT NULL,
  `s3d` int(11) DEFAULT NULL,
  `s3ai` int(11) DEFAULT NULL,
  `s3ch1` int(11) DEFAULT NULL,
  `s3ch2` int(11) DEFAULT NULL,
  `snatchresult` int(11) DEFAULT 0,
  `snatch_place` int(3) DEFAULT NULL COMMENT 'snatch place',
  `cleanjerk1` int(11) NOT NULL DEFAULT 55,
  `cleanjerk1isget` tinyint(3) DEFAULT NULL,
  `cleanjerk1d` int(11) DEFAULT NULL,
  `cleanjerk1ch1` int(11) DEFAULT NULL,
  `cleanjerk1ch2` int(11) DEFAULT NULL,
  `cleanjerk1ch3` int(11) DEFAULT NULL,
  `cleanjerk2` int(11) DEFAULT NULL,
  `cleanjerk2isget` tinyint(3) DEFAULT NULL,
  `cleanjerk2d` int(11) DEFAULT NULL,
  `cleanjerk2ai` int(11) DEFAULT NULL,
  `cleanjerk2ch1` int(11) DEFAULT NULL,
  `cleanjerk2ch2` int(11) DEFAULT NULL,
  `cleanjerk3` int(11) DEFAULT NULL,
  `cleanjerk3isget` tinyint(3) DEFAULT NULL,
  `cleanjerk3d` int(11) DEFAULT NULL,
  `cleanjerk3ai` int(11) DEFAULT NULL,
  `cleanjerk3ch1` int(11) DEFAULT NULL,
  `cleanjerk3ch2` int(11) DEFAULT NULL,
  `cleanjerkresult` int(11) DEFAULT 0,
  `cleanjerk_place` int(3) DEFAULT NULL COMMENT 'clean&jerk place',
  `doublesum` int(11) DEFAULT 0,
  `firstname` varchar(15) NOT NULL DEFAULT 'Нимай',
  `secondname` varchar(15) NOT NULL DEFAULT 'Махапрабху',
  `birth` varchar(10) NOT NULL DEFAULT '07.08.1983',
  `country_id` int(11) DEFAULT 1,
  `city_id` varchar(27) DEFAULT '1',
  `city` varchar(39) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL DEFAULT '1',
  `avatar` varchar(50) NOT NULL DEFAULT '/img/avatars/defava0.png',
  `changets` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `guru1name` varchar(20) NOT NULL DEFAULT 'Палько С.А.',
  `guru2name` varchar(20) NOT NULL DEFAULT 'Палько А.Г.',
  `ishideordel` int(11) NOT NULL DEFAULT 0,
  `actionend` int(11) NOT NULL DEFAULT 0,
  `place` int(3) DEFAULT NULL COMMENT 'flow att place',
  `flow_` tinyint(3) DEFAULT NULL COMMENT 'null - новый Атлет \r\n         1 - Выступает (сейчас Атлет в потоке выступления)\r\n         2 - Выступил ( Атлет уже выступил, скрыт)',
  `country_` enum('rus','ukr','kaz','uzb','usa','arm','grg') NOT NULL DEFAULT 'rus',
  `wcat_` varchar(5) NOT NULL DEFAULT '102+',
  `bkp_creation` timestamp(6) NOT NULL DEFAULT current_timestamp(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `__v7bkp_2023030407085304`
--

INSERT INTO `__v7bkp_2023030407085304` (`id`, `op`, `nextop`, `prevop`, `weightnow`, `exnow`, `trynow`, `serialnumber`, `sex`, `ownweight`, `wcat_id`, `rank_id`, `info_id`, `newrank`, `score`, `sincler`, `position`, `snatch1`, `snatch1isget`, `s1d`, `s1ch1`, `s1ch2`, `s1ch3`, `snatch2`, `snatch2isget`, `s2d`, `s2ai`, `s2ch1`, `s2ch2`, `snatch3`, `snatch3isget`, `s3d`, `s3ai`, `s3ch1`, `s3ch2`, `snatchresult`, `snatch_place`, `cleanjerk1`, `cleanjerk1isget`, `cleanjerk1d`, `cleanjerk1ch1`, `cleanjerk1ch2`, `cleanjerk1ch3`, `cleanjerk2`, `cleanjerk2isget`, `cleanjerk2d`, `cleanjerk2ai`, `cleanjerk2ch1`, `cleanjerk2ch2`, `cleanjerk3`, `cleanjerk3isget`, `cleanjerk3d`, `cleanjerk3ai`, `cleanjerk3ch1`, `cleanjerk3ch2`, `cleanjerkresult`, `cleanjerk_place`, `doublesum`, `firstname`, `secondname`, `birth`, `country_id`, `city_id`, `city`, `avatar`, `changets`, `guru1name`, `guru2name`, `ishideordel`, `actionend`, `place`, `flow_`, `country_`, `wcat_`, `bkp_creation`) VALUES
(1, 0, 0, 0, 97, 's1', 0, NULL, 1, 72.8, 1, 1, 1, NULL, NULL, '', NULL, 97, NULL, 44, 97, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 1, 55, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 1, 0, 'Гаура́нга', 'Нитьяна́нда', '07.03.1486', 1, '1', '1', '/img/avatars/defava11.png', '2023-03-04 02:08:50', 'Палькодзян С.А.', 'Палько А.Г.', 0, 0, 1, 1, 'rus', '102+', '2023-03-04 02:08:53.156266'),
(2, 0, 0, 0, 77, 's1', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 77, NULL, 77, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 2, 88, NULL, 88, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 2, 0, 'Журкин', 'Дмитрий', '', 1, '1', ' Локация:  ', '/img/avatars/defava0.png', '2023-03-04 02:08:50', 'Палько С.А.', 'Палько А.Г.', 0, 0, 2, 1, 'rus', '102+', '2023-03-04 02:08:53.156266'),
(3, 0, 0, 0, 123, 's1', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 123, NULL, 123, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 3, 155, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 3, 0, 'Карагачан', 'Сергей', '', 1, '1', ' Локация:  ', '/img/avatars/defava0.png', '2023-03-04 02:08:50', 'Палько С.А.', 'Палько А.Г.', 0, 0, 3, 1, 'rus', '102+', '2023-03-04 02:08:53.156266'),
(4, 0, 0, 0, 177, 's1', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 177, NULL, 177, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 199, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 0, 'Шпак', 'Сергей', '', 1, '1', ' Локация:  ', '/img/avatars/defava0.png', '2023-03-04 02:08:50', 'Палько С.А.', 'Палько А.Г.', 0, 0, 4, 1, 'rus', '102+', '2023-03-04 02:08:53.156266'),
(5, 1, 0, 0, 55, 's1', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 55, NULL, 55, NULL, NULL, NULL, 55, NULL, 55, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 5, 77, NULL, 77, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 5, 0, 'Орликовский', 'Олег', '', 1, '1', ' Локация:  ', '/img/avatars/defava0.png', '2023-03-04 02:08:50', 'Палько С.А.', 'Палько А.Г.', 0, 0, 5, 1, 'rus', '102+', '2023-03-04 02:08:53.156266');

-- --------------------------------------------------------

--
-- Структура таблицы `__v7bkp_2023030409263104`
--

CREATE TABLE `__v7bkp_2023030409263104` (
  `id` int(11) NOT NULL,
  `op` int(11) NOT NULL DEFAULT 0,
  `nextop` int(11) NOT NULL DEFAULT 0,
  `prevop` int(11) NOT NULL DEFAULT 0,
  `weightnow` int(11) NOT NULL DEFAULT 0,
  `exnow` enum('s1','s2','s3','j1','j2','j3','finished') NOT NULL DEFAULT 's1',
  `trynow` int(11) DEFAULT 0,
  `serialnumber` int(11) DEFAULT NULL,
  `sex` int(11) NOT NULL DEFAULT 1,
  `ownweight` float(10,1) NOT NULL DEFAULT 72.8,
  `wcat_id` int(5) DEFAULT 1,
  `rank_id` int(11) DEFAULT 0,
  `info_id` int(11) DEFAULT 1,
  `newrank` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `sincler` varchar(15) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `position` int(11) DEFAULT NULL,
  `snatch1` int(11) NOT NULL DEFAULT 44,
  `snatch1isget` tinyint(3) DEFAULT NULL,
  `s1d` int(11) DEFAULT NULL,
  `s1ch1` int(11) DEFAULT NULL,
  `s1ch2` int(11) DEFAULT NULL,
  `s1ch3` int(11) DEFAULT NULL,
  `snatch2` int(11) DEFAULT NULL,
  `snatch2isget` tinyint(3) DEFAULT NULL,
  `s2d` int(11) DEFAULT NULL,
  `s2ai` int(11) DEFAULT NULL,
  `s2ch1` int(11) DEFAULT NULL,
  `s2ch2` int(11) DEFAULT NULL,
  `snatch3` int(11) DEFAULT NULL,
  `snatch3isget` tinyint(3) DEFAULT NULL,
  `s3d` int(11) DEFAULT NULL,
  `s3ai` int(11) DEFAULT NULL,
  `s3ch1` int(11) DEFAULT NULL,
  `s3ch2` int(11) DEFAULT NULL,
  `snatchresult` int(11) DEFAULT 0,
  `snatch_place` int(3) DEFAULT NULL COMMENT 'snatch place',
  `cleanjerk1` int(11) NOT NULL DEFAULT 55,
  `cleanjerk1isget` tinyint(3) DEFAULT NULL,
  `cleanjerk1d` int(11) DEFAULT NULL,
  `cleanjerk1ch1` int(11) DEFAULT NULL,
  `cleanjerk1ch2` int(11) DEFAULT NULL,
  `cleanjerk1ch3` int(11) DEFAULT NULL,
  `cleanjerk2` int(11) DEFAULT NULL,
  `cleanjerk2isget` tinyint(3) DEFAULT NULL,
  `cleanjerk2d` int(11) DEFAULT NULL,
  `cleanjerk2ai` int(11) DEFAULT NULL,
  `cleanjerk2ch1` int(11) DEFAULT NULL,
  `cleanjerk2ch2` int(11) DEFAULT NULL,
  `cleanjerk3` int(11) DEFAULT NULL,
  `cleanjerk3isget` tinyint(3) DEFAULT NULL,
  `cleanjerk3d` int(11) DEFAULT NULL,
  `cleanjerk3ai` int(11) DEFAULT NULL,
  `cleanjerk3ch1` int(11) DEFAULT NULL,
  `cleanjerk3ch2` int(11) DEFAULT NULL,
  `cleanjerkresult` int(11) DEFAULT 0,
  `cleanjerk_place` int(3) DEFAULT NULL COMMENT 'clean&jerk place',
  `doublesum` int(11) DEFAULT 0,
  `firstname` varchar(15) NOT NULL DEFAULT 'Нимай',
  `secondname` varchar(15) NOT NULL DEFAULT 'Махапрабху',
  `birth` varchar(10) NOT NULL DEFAULT '07.08.1983',
  `country_id` int(11) DEFAULT 1,
  `city_id` varchar(27) DEFAULT '1',
  `city` varchar(39) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL DEFAULT '1',
  `avatar` varchar(50) NOT NULL DEFAULT '/img/avatars/defava0.png',
  `changets` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `guru1name` varchar(20) NOT NULL DEFAULT 'Палько С.А.',
  `guru2name` varchar(20) NOT NULL DEFAULT 'Палько А.Г.',
  `ishideordel` int(11) NOT NULL DEFAULT 0,
  `actionend` int(11) NOT NULL DEFAULT 0,
  `place` int(3) DEFAULT NULL COMMENT 'flow att place',
  `flow_` tinyint(3) DEFAULT NULL COMMENT 'null - новый Атлет \r\n         1 - Выступает (сейчас Атлет в потоке выступления)\r\n         2 - Выступил ( Атлет уже выступил, скрыт)',
  `country_` enum('rus','ukr','kaz','uzb','usa','arm','grg') NOT NULL DEFAULT 'rus',
  `wcat_` varchar(5) NOT NULL DEFAULT '102+',
  `bkp_creation` timestamp(6) NOT NULL DEFAULT current_timestamp(6)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `__v7bkp_2023030409263104`
--

INSERT INTO `__v7bkp_2023030409263104` (`id`, `op`, `nextop`, `prevop`, `weightnow`, `exnow`, `trynow`, `serialnumber`, `sex`, `ownweight`, `wcat_id`, `rank_id`, `info_id`, `newrank`, `score`, `sincler`, `position`, `snatch1`, `snatch1isget`, `s1d`, `s1ch1`, `s1ch2`, `s1ch3`, `snatch2`, `snatch2isget`, `s2d`, `s2ai`, `s2ch1`, `s2ch2`, `snatch3`, `snatch3isget`, `s3d`, `s3ai`, `s3ch1`, `s3ch2`, `snatchresult`, `snatch_place`, `cleanjerk1`, `cleanjerk1isget`, `cleanjerk1d`, `cleanjerk1ch1`, `cleanjerk1ch2`, `cleanjerk1ch3`, `cleanjerk2`, `cleanjerk2isget`, `cleanjerk2d`, `cleanjerk2ai`, `cleanjerk2ch1`, `cleanjerk2ch2`, `cleanjerk3`, `cleanjerk3isget`, `cleanjerk3d`, `cleanjerk3ai`, `cleanjerk3ch1`, `cleanjerk3ch2`, `cleanjerkresult`, `cleanjerk_place`, `doublesum`, `firstname`, `secondname`, `birth`, `country_id`, `city_id`, `city`, `avatar`, `changets`, `guru1name`, `guru2name`, `ishideordel`, `actionend`, `place`, `flow_`, `country_`, `wcat_`, `bkp_creation`) VALUES
(1, 0, 0, 0, 55, 'j1', 0, NULL, 1, 72.8, 1, 1, 1, NULL, NULL, '', NULL, 44, 0, 44, NULL, NULL, NULL, 44, 1, 44, NULL, NULL, NULL, 45, 1, 45, NULL, NULL, NULL, 45, 2, 55, NULL, 55, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 1, 45, 'Гаура́нга', 'Нитьяна́нда', '07.03.1486', 1, '1', '1', '/img/avatars/defava11.png', '2023-03-04 04:26:31', 'Палькодзян С.А.', 'Палько А.Г.', 0, 0, 2, 1, 'rus', '102+', '2023-03-04 04:26:31.521732'),
(2, 1, 0, 0, 55, 's1', 0, NULL, 1, 69.7, 30, 30, 1, NULL, NULL, '', NULL, 55, NULL, 55, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 3, 77, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 2, 0, 'fdsf', 'fsdf', '', 1, '1', ' Локация:  ', '/img/avatars/defava0.png', '2023-03-04 04:26:31', 'Палько С.А.', 'Палько А.Г.', 0, 0, 3, 1, 'rus', '102+', '2023-03-04 04:26:31.521732'),
(3, 0, 0, 0, 88, 's1', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 88, NULL, 88, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 99, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 3, 0, 'dsfsdf', 'fdsf', '', 1, '1', ' Локация:  ', '/img/avatars/defava0.png', '2023-03-04 04:26:31', 'Палько С.А.', 'Палько А.Г.', 0, 0, 4, 1, 'rus', '102+', '2023-03-04 04:26:31.521732'),
(4, 0, 0, 0, 67, 's1', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 67, NULL, 67, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 5, 76, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 0, 'sdsf', 'fdsfsdf', '', 1, '1', ' Локация:  ', '/img/avatars/defava0.png', '2023-03-04 04:26:31', 'Палько С.А.', 'Палько А.Г.', 0, 0, 5, 1, 'rus', '102+', '2023-03-04 04:26:31.521732'),
(5, 0, 0, 0, 55, 'j1', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 53, 0, 55, 53, NULL, NULL, 53, 1, 53, NULL, NULL, NULL, 54, 1, 54, NULL, NULL, NULL, 54, 1, 55, NULL, 55, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 5, 54, 'fyfgbv', 'cccccc', '', 1, '1', ' Локация:  ', '/img/avatars/defava0.png', '2023-03-04 04:26:31', 'Палько С.А.', 'Палько А.Г.', 0, 0, 1, 1, 'rus', '102+', '2023-03-04 04:26:31.521732');

-- --------------------------------------------------------

--
-- Структура таблицы `__v7bkp_2023030412383904`
--

CREATE TABLE `__v7bkp_2023030412383904` (
  `id` int(11) NOT NULL,
  `op` int(11) NOT NULL DEFAULT 0,
  `nextop` int(11) NOT NULL DEFAULT 0,
  `prevop` int(11) NOT NULL DEFAULT 0,
  `weightnow` int(11) NOT NULL DEFAULT 0,
  `exnow` enum('s1','s2','s3','j1','j2','j3','finished') NOT NULL DEFAULT 's1',
  `trynow` int(11) DEFAULT 0,
  `serialnumber` int(11) DEFAULT NULL,
  `sex` int(11) NOT NULL DEFAULT 1,
  `ownweight` float(10,1) NOT NULL DEFAULT 72.8,
  `wcat_id` int(5) DEFAULT 1,
  `rank_id` int(11) DEFAULT 0,
  `info_id` int(11) DEFAULT 1,
  `newrank` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `sincler` varchar(15) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `position` int(11) DEFAULT NULL,
  `snatch1` int(11) NOT NULL DEFAULT 44,
  `snatch1isget` tinyint(3) DEFAULT NULL,
  `s1d` int(11) DEFAULT NULL,
  `s1ch1` int(11) DEFAULT NULL,
  `s1ch2` int(11) DEFAULT NULL,
  `s1ch3` int(11) DEFAULT NULL,
  `snatch2` int(11) DEFAULT NULL,
  `snatch2isget` tinyint(3) DEFAULT NULL,
  `s2d` int(11) DEFAULT NULL,
  `s2ai` int(11) DEFAULT NULL,
  `s2ch1` int(11) DEFAULT NULL,
  `s2ch2` int(11) DEFAULT NULL,
  `snatch3` int(11) DEFAULT NULL,
  `snatch3isget` tinyint(3) DEFAULT NULL,
  `s3d` int(11) DEFAULT NULL,
  `s3ai` int(11) DEFAULT NULL,
  `s3ch1` int(11) DEFAULT NULL,
  `s3ch2` int(11) DEFAULT NULL,
  `snatchresult` int(11) DEFAULT 0,
  `snatch_place` int(3) DEFAULT NULL COMMENT 'snatch place',
  `cleanjerk1` int(11) NOT NULL DEFAULT 55,
  `cleanjerk1isget` tinyint(3) DEFAULT NULL,
  `cleanjerk1d` int(11) DEFAULT NULL,
  `cleanjerk1ch1` int(11) DEFAULT NULL,
  `cleanjerk1ch2` int(11) DEFAULT NULL,
  `cleanjerk1ch3` int(11) DEFAULT NULL,
  `cleanjerk2` int(11) DEFAULT NULL,
  `cleanjerk2isget` tinyint(3) DEFAULT NULL,
  `cleanjerk2d` int(11) DEFAULT NULL,
  `cleanjerk2ai` int(11) DEFAULT NULL,
  `cleanjerk2ch1` int(11) DEFAULT NULL,
  `cleanjerk2ch2` int(11) DEFAULT NULL,
  `cleanjerk3` int(11) DEFAULT NULL,
  `cleanjerk3isget` tinyint(3) DEFAULT NULL,
  `cleanjerk3d` int(11) DEFAULT NULL,
  `cleanjerk3ai` int(11) DEFAULT NULL,
  `cleanjerk3ch1` int(11) DEFAULT NULL,
  `cleanjerk3ch2` int(11) DEFAULT NULL,
  `cleanjerkresult` int(11) DEFAULT 0,
  `cleanjerk_place` int(3) DEFAULT NULL COMMENT 'clean&jerk place',
  `doublesum` int(11) DEFAULT 0,
  `firstname` varchar(15) NOT NULL DEFAULT 'Нимай',
  `secondname` varchar(15) NOT NULL DEFAULT 'Махапрабху',
  `birth` varchar(10) NOT NULL DEFAULT '07.08.1983',
  `country_id` int(11) DEFAULT 1,
  `city_id` varchar(27) DEFAULT '1',
  `city` varchar(39) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL DEFAULT '1',
  `avatar` varchar(50) NOT NULL DEFAULT '/img/avatars/defava0.png',
  `changets` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `guru1name` varchar(20) NOT NULL DEFAULT 'Палько С.А.',
  `guru2name` varchar(20) NOT NULL DEFAULT 'Палько А.Г.',
  `ishideordel` int(11) NOT NULL DEFAULT 0,
  `actionend` int(11) NOT NULL DEFAULT 0,
  `place` int(3) DEFAULT NULL COMMENT 'flow att place',
  `flow_` tinyint(3) DEFAULT NULL COMMENT 'null - новый Атлет \r\n         1 - Выступает (сейчас Атлет в потоке выступления)\r\n         2 - Выступил ( Атлет уже выступил, скрыт)',
  `country_` enum('rus','ukr','kaz','uzb','usa','arm','grg') NOT NULL DEFAULT 'rus',
  `wcat_` varchar(5) NOT NULL DEFAULT '102+',
  `bkp_creation` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `__v7bkp_2023030412383904`
--

INSERT INTO `__v7bkp_2023030412383904` (`id`, `op`, `nextop`, `prevop`, `weightnow`, `exnow`, `trynow`, `serialnumber`, `sex`, `ownweight`, `wcat_id`, `rank_id`, `info_id`, `newrank`, `score`, `sincler`, `position`, `snatch1`, `snatch1isget`, `s1d`, `s1ch1`, `s1ch2`, `s1ch3`, `snatch2`, `snatch2isget`, `s2d`, `s2ai`, `s2ch1`, `s2ch2`, `snatch3`, `snatch3isget`, `s3d`, `s3ai`, `s3ch1`, `s3ch2`, `snatchresult`, `snatch_place`, `cleanjerk1`, `cleanjerk1isget`, `cleanjerk1d`, `cleanjerk1ch1`, `cleanjerk1ch2`, `cleanjerk1ch3`, `cleanjerk2`, `cleanjerk2isget`, `cleanjerk2d`, `cleanjerk2ai`, `cleanjerk2ch1`, `cleanjerk2ch2`, `cleanjerk3`, `cleanjerk3isget`, `cleanjerk3d`, `cleanjerk3ai`, `cleanjerk3ch1`, `cleanjerk3ch2`, `cleanjerkresult`, `cleanjerk_place`, `doublesum`, `firstname`, `secondname`, `birth`, `country_id`, `city_id`, `city`, `avatar`, `changets`, `guru1name`, `guru2name`, `ishideordel`, `actionend`, `place`, `flow_`, `country_`, `wcat_`, `bkp_creation`) VALUES
(25, 0, 0, 0, 104, 's1', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 104, NULL, 44, 104, 104, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 1, 55, NULL, 55, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 1, 0, 'Голова', 'Браманы', '', 1, '1', ' Локация:  ', '/img/avatars/defava0.png', '2023-03-04 07:38:37', 'Палько С.А.', 'Палько А.Г.', 0, 0, 1, 1, 'rus', '102+', ''),
(26, 1, 0, 0, 66, 's1', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 66, NULL, 66, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 2, 77, NULL, 77, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 2, 0, 'Руки', 'Кшатрии', '', 1, '1', ' Локация:  ', '/img/avatars/defava0.png', '2023-03-04 07:38:39', 'Палько С.А.', 'Палько А.Г.', 0, 0, 2, 1, 'rus', '102+', ''),
(27, 0, 0, 0, 75, 's1', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 75, NULL, 67, 70, 75, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 3, 89, NULL, 89, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 3, 0, 'Живот', 'Вайшьи', '', 1, '1', ' Локация:  ', '/img/avatars/defava0.png', '2023-03-04 07:38:37', 'Палько С.А.', 'Палько А.Г.', 0, 0, 3, 1, 'rus', '102+', ''),
(28, 0, 1, 0, 74, 's1', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 74, NULL, 74, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 59, NULL, 59, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 0, 'Ноги', 'Шудры', '', 1, '1', ' Локация:  ', '/img/avatars/defava0.png', '2023-03-04 07:38:39', 'Палько С.А.', 'Палько А.Г.', 0, 0, 4, 1, 'rus', '102+', '');

-- --------------------------------------------------------

--
-- Структура таблицы `__v7bkp_2023030416292904`
--

CREATE TABLE `__v7bkp_2023030416292904` (
  `id` int(11) NOT NULL,
  `op` int(11) NOT NULL DEFAULT 0,
  `nextop` int(11) NOT NULL DEFAULT 0,
  `prevop` int(11) NOT NULL DEFAULT 0,
  `weightnow` int(11) NOT NULL DEFAULT 0,
  `exnow` enum('s1','s2','s3','j1','j2','j3','finished') NOT NULL DEFAULT 's1',
  `trynow` int(11) DEFAULT 0,
  `serialnumber` int(11) DEFAULT NULL,
  `sex` int(11) NOT NULL DEFAULT 1,
  `ownweight` float(10,1) NOT NULL DEFAULT 72.8,
  `wcat_id` int(5) DEFAULT 1,
  `rank_id` int(11) DEFAULT 0,
  `info_id` int(11) DEFAULT 1,
  `newrank` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `sincler` varchar(15) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `position` int(11) DEFAULT NULL,
  `snatch1` int(11) NOT NULL DEFAULT 44,
  `snatch1isget` tinyint(3) DEFAULT NULL,
  `s1d` int(11) DEFAULT NULL,
  `s1ch1` int(11) DEFAULT NULL,
  `s1ch2` int(11) DEFAULT NULL,
  `s1ch3` int(11) DEFAULT NULL,
  `snatch2` int(11) DEFAULT NULL,
  `snatch2isget` tinyint(3) DEFAULT NULL,
  `s2d` int(11) DEFAULT NULL,
  `s2ai` int(11) DEFAULT NULL,
  `s2ch1` int(11) DEFAULT NULL,
  `s2ch2` int(11) DEFAULT NULL,
  `snatch3` int(11) DEFAULT NULL,
  `snatch3isget` tinyint(3) DEFAULT NULL,
  `s3d` int(11) DEFAULT NULL,
  `s3ai` int(11) DEFAULT NULL,
  `s3ch1` int(11) DEFAULT NULL,
  `s3ch2` int(11) DEFAULT NULL,
  `snatchresult` int(11) DEFAULT 0,
  `snatch_place` int(3) DEFAULT NULL COMMENT 'snatch place',
  `cleanjerk1` int(11) NOT NULL DEFAULT 55,
  `cleanjerk1isget` tinyint(3) DEFAULT NULL,
  `cleanjerk1d` int(11) DEFAULT NULL,
  `cleanjerk1ch1` int(11) DEFAULT NULL,
  `cleanjerk1ch2` int(11) DEFAULT NULL,
  `cleanjerk1ch3` int(11) DEFAULT NULL,
  `cleanjerk2` int(11) DEFAULT NULL,
  `cleanjerk2isget` tinyint(3) DEFAULT NULL,
  `cleanjerk2d` int(11) DEFAULT NULL,
  `cleanjerk2ai` int(11) DEFAULT NULL,
  `cleanjerk2ch1` int(11) DEFAULT NULL,
  `cleanjerk2ch2` int(11) DEFAULT NULL,
  `cleanjerk3` int(11) DEFAULT NULL,
  `cleanjerk3isget` tinyint(3) DEFAULT NULL,
  `cleanjerk3d` int(11) DEFAULT NULL,
  `cleanjerk3ai` int(11) DEFAULT NULL,
  `cleanjerk3ch1` int(11) DEFAULT NULL,
  `cleanjerk3ch2` int(11) DEFAULT NULL,
  `cleanjerkresult` int(11) DEFAULT 0,
  `cleanjerk_place` int(3) DEFAULT NULL COMMENT 'clean&jerk place',
  `doublesum` int(11) DEFAULT 0,
  `firstname` varchar(15) NOT NULL DEFAULT 'Нимай',
  `secondname` varchar(15) NOT NULL DEFAULT 'Махапрабху',
  `birth` varchar(10) NOT NULL DEFAULT '07.08.1983',
  `country_id` int(11) DEFAULT 1,
  `city_id` varchar(27) DEFAULT '1',
  `city` varchar(39) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL DEFAULT '1',
  `avatar` varchar(50) NOT NULL DEFAULT '/img/avatars/defava0.png',
  `changets` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `guru1name` varchar(20) NOT NULL DEFAULT 'Палько С.А.',
  `guru2name` varchar(20) NOT NULL DEFAULT 'Палько А.Г.',
  `ishideordel` int(11) NOT NULL DEFAULT 0,
  `actionend` int(11) NOT NULL DEFAULT 0,
  `place` int(3) DEFAULT NULL COMMENT 'flow att place',
  `flow_` tinyint(3) DEFAULT NULL COMMENT 'null - новый Атлет \r\n         1 - Выступает (сейчас Атлет в потоке выступления)\r\n         2 - Выступил ( Атлет уже выступил, скрыт)',
  `country_` enum('rus','ukr','kaz','uzb','usa','arm','grg') NOT NULL DEFAULT 'rus',
  `wcat_` varchar(5) NOT NULL DEFAULT '102+',
  `bkp_creation` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `__v7bkp_2023030416292904`
--

INSERT INTO `__v7bkp_2023030416292904` (`id`, `op`, `nextop`, `prevop`, `weightnow`, `exnow`, `trynow`, `serialnumber`, `sex`, `ownweight`, `wcat_id`, `rank_id`, `info_id`, `newrank`, `score`, `sincler`, `position`, `snatch1`, `snatch1isget`, `s1d`, `s1ch1`, `s1ch2`, `s1ch3`, `snatch2`, `snatch2isget`, `s2d`, `s2ai`, `s2ch1`, `s2ch2`, `snatch3`, `snatch3isget`, `s3d`, `s3ai`, `s3ch1`, `s3ch2`, `snatchresult`, `snatch_place`, `cleanjerk1`, `cleanjerk1isget`, `cleanjerk1d`, `cleanjerk1ch1`, `cleanjerk1ch2`, `cleanjerk1ch3`, `cleanjerk2`, `cleanjerk2isget`, `cleanjerk2d`, `cleanjerk2ai`, `cleanjerk2ch1`, `cleanjerk2ch2`, `cleanjerk3`, `cleanjerk3isget`, `cleanjerk3d`, `cleanjerk3ai`, `cleanjerk3ch1`, `cleanjerk3ch2`, `cleanjerkresult`, `cleanjerk_place`, `doublesum`, `firstname`, `secondname`, `birth`, `country_id`, `city_id`, `city`, `avatar`, `changets`, `guru1name`, `guru2name`, `ishideordel`, `actionend`, `place`, `flow_`, `country_`, `wcat_`, `bkp_creation`) VALUES
(1, 0, 0, 0, 63, 'finished', 0, NULL, 1, 72.8, 1, 1, 1, NULL, NULL, '', NULL, 44, 0, 44, NULL, NULL, NULL, 44, 1, 44, NULL, NULL, NULL, 45, 1, 45, NULL, NULL, NULL, 45, 3, 55, 0, 55, NULL, NULL, NULL, 62, 1, 62, NULL, 62, 62, 63, 0, 63, NULL, NULL, NULL, 62, 2, 107, 'Махапрабху', 'Нитьяна́нда', '07.03.1486', 1, '1', 'Омск', '/img/avatars/defava11.png', '2023-03-04 11:16:37', 'Палькодзян С.А.', 'Палько А.Г.', 0, 1, 2, 2, 'rus', '102+', ''),
(2, 0, 0, 0, 69, 'finished', 0, NULL, 1, 69.7, 34, 34, 1, NULL, NULL, '', NULL, 55, 1, 55, NULL, NULL, NULL, 56, 0, 56, NULL, NULL, NULL, 56, 1, 56, NULL, NULL, NULL, 56, 2, 66, 0, 66, NULL, NULL, NULL, 69, 0, 69, NULL, 69, 69, 69, 1, 69, NULL, NULL, NULL, 69, 1, 125, 'Адвайта', 'Шри', '', 1, '1', ' Локация:  ', '/img/avatars/defava0.png', '2023-03-04 11:16:37', 'Палько С.А.', 'Палько А.Г.', 0, 1, 1, 2, 'rus', '102+', ''),
(3, 0, 0, 0, 0, 'j2', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 77, 0, 77, NULL, NULL, NULL, 77, 0, 77, NULL, NULL, NULL, 77, 1, 77, NULL, NULL, NULL, 77, 1, 88, 0, 88, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 3, 77, 'Гадагхара', 'Шри', '', 1, '1', ' Локация:  ', '/img/avatars/defava0.png', '2023-03-04 11:16:37', 'Палько С.А.', 'Палько А.Г.', 0, 1, 3, 2, 'rus', '102+', '');

-- --------------------------------------------------------

--
-- Структура таблицы `__v7bkp_2023031522291115`
--

CREATE TABLE `__v7bkp_2023031522291115` (
  `id` int(11) NOT NULL,
  `op` int(11) NOT NULL DEFAULT 0,
  `nextop` int(11) NOT NULL DEFAULT 0,
  `prevop` int(11) NOT NULL DEFAULT 0,
  `weightnow` int(11) NOT NULL DEFAULT 0,
  `exnow` enum('s1','s2','s3','j1','j2','j3','finished') NOT NULL DEFAULT 's1',
  `trynow` int(11) DEFAULT 0,
  `serialnumber` int(11) DEFAULT NULL,
  `sex` int(11) NOT NULL DEFAULT 1,
  `ownweight` float(10,1) NOT NULL DEFAULT 72.8,
  `wcat_id` int(5) DEFAULT 1,
  `rank_id` int(11) DEFAULT 0,
  `info_id` int(11) DEFAULT 1,
  `newrank` int(11) DEFAULT NULL,
  `score` int(11) DEFAULT NULL,
  `sincler` varchar(15) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `position` int(11) DEFAULT NULL,
  `snatch1` int(11) NOT NULL DEFAULT 44,
  `snatch1isget` tinyint(3) DEFAULT NULL,
  `s1d` int(11) DEFAULT NULL,
  `s1ch1` int(11) DEFAULT NULL,
  `s1ch2` int(11) DEFAULT NULL,
  `s1ch3` int(11) DEFAULT NULL,
  `snatch2` int(11) DEFAULT NULL,
  `snatch2isget` tinyint(3) DEFAULT NULL,
  `s2d` int(11) DEFAULT NULL,
  `s2ai` int(11) DEFAULT NULL,
  `s2ch1` int(11) DEFAULT NULL,
  `s2ch2` int(11) DEFAULT NULL,
  `snatch3` int(11) DEFAULT NULL,
  `snatch3isget` tinyint(3) DEFAULT NULL,
  `s3d` int(11) DEFAULT NULL,
  `s3ai` int(11) DEFAULT NULL,
  `s3ch1` int(11) DEFAULT NULL,
  `s3ch2` int(11) DEFAULT NULL,
  `snatchresult` int(11) DEFAULT 0,
  `snatch_place` int(3) DEFAULT NULL COMMENT 'snatch place',
  `cleanjerk1` int(11) NOT NULL DEFAULT 55,
  `cleanjerk1isget` tinyint(3) DEFAULT NULL,
  `cleanjerk1d` int(11) DEFAULT NULL,
  `cleanjerk1ch1` int(11) DEFAULT NULL,
  `cleanjerk1ch2` int(11) DEFAULT NULL,
  `cleanjerk1ch3` int(11) DEFAULT NULL,
  `cleanjerk2` int(11) DEFAULT NULL,
  `cleanjerk2isget` tinyint(3) DEFAULT NULL,
  `cleanjerk2d` int(11) DEFAULT NULL,
  `cleanjerk2ai` int(11) DEFAULT NULL,
  `cleanjerk2ch1` int(11) DEFAULT NULL,
  `cleanjerk2ch2` int(11) DEFAULT NULL,
  `cleanjerk3` int(11) DEFAULT NULL,
  `cleanjerk3isget` tinyint(3) DEFAULT NULL,
  `cleanjerk3d` int(11) DEFAULT NULL,
  `cleanjerk3ai` int(11) DEFAULT NULL,
  `cleanjerk3ch1` int(11) DEFAULT NULL,
  `cleanjerk3ch2` int(11) DEFAULT NULL,
  `cleanjerkresult` int(11) DEFAULT 0,
  `cleanjerk_place` int(3) DEFAULT NULL COMMENT 'clean&jerk place',
  `doublesum` int(11) DEFAULT 0,
  `firstname` varchar(15) NOT NULL DEFAULT 'Нимай',
  `secondname` varchar(15) NOT NULL DEFAULT 'Махапрабху',
  `birth` varchar(10) NOT NULL DEFAULT '07.08.1983',
  `country_id` int(11) DEFAULT 1,
  `city_id` varchar(27) DEFAULT '1',
  `city` varchar(39) CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL DEFAULT '1',
  `avatar` varchar(50) NOT NULL DEFAULT '/img/avatars/defava0.png',
  `changets` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `guru1name` varchar(20) NOT NULL DEFAULT 'Палько С.А.',
  `guru2name` varchar(20) NOT NULL DEFAULT 'Палько А.Г.',
  `ishideordel` int(11) NOT NULL DEFAULT 0,
  `actionend` int(11) NOT NULL DEFAULT 0,
  `place` int(3) DEFAULT NULL COMMENT 'flow att place',
  `flow_` tinyint(3) DEFAULT NULL COMMENT 'null - новый Атлет \r\n         1 - Выступает (сейчас Атлет в потоке выступления)\r\n         2 - Выступил ( Атлет уже выступил, скрыт)',
  `country_` enum('rus','ukr','kaz','uzb','usa','arm','grg') NOT NULL DEFAULT 'rus',
  `wcat_` varchar(5) NOT NULL DEFAULT '102+',
  `bkp_creation` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Дамп данных таблицы `__v7bkp_2023031522291115`
--

INSERT INTO `__v7bkp_2023031522291115` (`id`, `op`, `nextop`, `prevop`, `weightnow`, `exnow`, `trynow`, `serialnumber`, `sex`, `ownweight`, `wcat_id`, `rank_id`, `info_id`, `newrank`, `score`, `sincler`, `position`, `snatch1`, `snatch1isget`, `s1d`, `s1ch1`, `s1ch2`, `s1ch3`, `snatch2`, `snatch2isget`, `s2d`, `s2ai`, `s2ch1`, `s2ch2`, `snatch3`, `snatch3isget`, `s3d`, `s3ai`, `s3ch1`, `s3ch2`, `snatchresult`, `snatch_place`, `cleanjerk1`, `cleanjerk1isget`, `cleanjerk1d`, `cleanjerk1ch1`, `cleanjerk1ch2`, `cleanjerk1ch3`, `cleanjerk2`, `cleanjerk2isget`, `cleanjerk2d`, `cleanjerk2ai`, `cleanjerk2ch1`, `cleanjerk2ch2`, `cleanjerk3`, `cleanjerk3isget`, `cleanjerk3d`, `cleanjerk3ai`, `cleanjerk3ch1`, `cleanjerk3ch2`, `cleanjerkresult`, `cleanjerk_place`, `doublesum`, `firstname`, `secondname`, `birth`, `country_id`, `city_id`, `city`, `avatar`, `changets`, `guru1name`, `guru2name`, `ishideordel`, `actionend`, `place`, `flow_`, `country_`, `wcat_`, `bkp_creation`) VALUES
(1, 0, 0, 0, 44, 's1', 0, NULL, 1, 72.8, 34, 34, 1, NULL, NULL, '', NULL, 44, NULL, 44, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 2, 235, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 1, 0, 'Гаура́нга', 'Нитьяна́нда', '07.03.1486', 1, '1', 'Сургут', '/img/avatars/defava11.png', '2023-03-15 17:28:44', 'Палькодзян С.А.', 'Палько А.Г.', 0, 1, 2, 2, 'rus', '102+', ''),
(2, 0, 0, 0, 68, 's1', 0, NULL, 1, 69.7, 34, 34, 1, NULL, NULL, '', NULL, 68, NULL, 68, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 3, 103, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 2, 0, 'Сержиоу', 'Чанчик', '', 1, '1', 'Вриндаван', '/img/avatars/defava0.png', '2023-03-15 17:28:44', 'Палько С.А.', 'Палько А.Г.', 0, 1, 3, 2, 'rus', '102+', ''),
(3, 0, 0, 0, 88, 's1', 0, NULL, 1, 69.7, 34, 34, 1, NULL, NULL, '', NULL, 88, NULL, 88, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 191, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 3, 0, 'Николя́', 'Шпаку́', '', 1, '1', 'Вриндаван', '/img/avatars/defava0.png', '2023-03-15 17:28:44', 'Палько С.А.', 'Палько А.Г.', 0, 1, 4, 2, 'rus', '102+', ''),
(4, 0, 0, 0, 0, 'j2', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 50, 1, 50, NULL, NULL, NULL, 51, 0, 51, NULL, NULL, NULL, 51, 1, 51, NULL, NULL, NULL, 51, 1, 66, 0, 66, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 4, 51, 'Олег', 'Альфреди', '', 1, '1', 'Сургут', '/img/avatars/defava0.png', '2023-03-15 17:28:44', 'Палько С.А.', 'Палько А.Г.', 0, 1, 1, 2, 'rus', '102+', ''),
(5, 1, 0, 0, 64, 's2', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 55, 0, 55, NULL, NULL, NULL, 64, NULL, 55, NULL, 56, 64, NULL, NULL, NULL, NULL, NULL, NULL, 0, 5, 66, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 5, 0, 'ghfgh', 'hgfh', '', 1, '1', 'ОМСК', '/img/avatars/defava0.png', '2023-03-15 17:28:44', 'Палько С.А.', 'Палько А.Г.', 0, 1, 5, 2, 'rus', '102+', ''),
(6, 0, 1, 0, 58, 's1', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 58, NULL, 55, 58, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 6, 66, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 6, 0, 'Санечка', 'Попов', '', 1, '1', 'Солнечный', '/img/avatars/defava0.png', '2023-03-15 17:28:44', 'Палько С.А.', 'Палько А.Г.', 0, 1, 6, 2, 'rus', '102+', ''),
(7, 0, 0, 0, 48, 's1', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 48, NULL, 48, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 7, 66, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 7, 0, 'Ябударов', 'Ильсун', '', 100, '1', 'Вартовск', '/img/avatars/defava0.png', '2023-03-15 17:28:44', 'Палько С.А.', 'Палько А.Г.', 0, 1, 7, 2, 'rus', '102+', ''),
(8, 0, 0, 0, 45, 's1', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 45, NULL, 45, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 8, 78, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 8, 0, 'Яфаров', 'Гюзбар', '', 1, '1', 'Покачи', '/img/avatars/defava0.png', '2023-03-15 17:28:44', 'Палько С.А.', 'Палько А.Г.', 0, 1, 8, 2, 'rus', '102+', ''),
(9, 0, 0, 0, 33, 's1', 0, NULL, 1, 69.7, 34, 34, 1, NULL, NULL, '', NULL, 33, NULL, 33, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 9, 72, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 9, 0, 'Шьям', 'Чандра', '', 1, '1', 'Лангепас', '/img/avatars/defava0.png', '2023-03-15 17:28:44', 'Палько С.А.', 'Палько А.Г.', 0, 1, 9, 2, 'rus', '102+', ''),
(10, 0, 0, 0, 55, 's1', 0, NULL, 1, 69.7, 1, 1, 1, NULL, NULL, '', NULL, 55, NULL, 55, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 10, 67, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, 0, 10, 0, 'Питюнидзе', 'Фамилий', '', 1, '1', ' Лангепас  ', '/img/avatars/defava0.png', '2023-03-15 17:28:44', 'Палько С.А.', 'Палько А.Г.', 0, 1, 10, 2, 'rus', '102+', '');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `cities`
--
ALTER TABLE `cities`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `country`
--
ALTER TABLE `country`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `info`
--
ALTER TABLE `info`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `opt`
--
ALTER TABLE `opt`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `ranks`
--
ALTER TABLE `ranks`
  ADD PRIMARY KEY (`id`),
  ADD KEY `wcat_id` (`wcat_id`);

--
-- Индексы таблицы `region`
--
ALTER TABLE `region`
  ADD PRIMARY KEY (`id`),
  ADD KEY `country_id` (`country_id`);

--
-- Индексы таблицы `v7now`
--
ALTER TABLE `v7now`
  ADD PRIMARY KEY (`id`) USING BTREE,
  ADD UNIQUE KEY `op_index` (`id`),
  ADD UNIQUE KEY `nop_index` (`id`),
  ADD KEY `country_id` (`country_id`),
  ADD KEY `rank_id` (`rank_id`),
  ADD KEY `wcat_id` (`wcat_id`),
  ADD KEY `info_id` (`info_id`);

--
-- Индексы таблицы `v7staff`
--
ALTER TABLE `v7staff`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `v7stat`
--
ALTER TABLE `v7stat`
  ADD KEY `id` (`id`);

--
-- Индексы таблицы `v7timer`
--
ALTER TABLE `v7timer`
  ADD PRIMARY KEY (`id`) USING BTREE;

--
-- Индексы таблицы `wcat`
--
ALTER TABLE `wcat`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `_v7athlete`
--
ALTER TABLE `_v7athlete`
  ADD PRIMARY KEY (`id`) USING BTREE,
  ADD UNIQUE KEY `op_index` (`id`),
  ADD UNIQUE KEY `nop_index` (`id`),
  ADD KEY `country_id` (`country_id`),
  ADD KEY `rank_id` (`rank_id`),
  ADD KEY `wcat_id` (`wcat_id`),
  ADD KEY `info_id` (`info_id`);

--
-- Индексы таблицы `__v7bkp_2023020119434501`
--
ALTER TABLE `__v7bkp_2023020119434501`
  ADD PRIMARY KEY (`id`) USING BTREE,
  ADD KEY `country_id` (`country_id`),
  ADD KEY `rank_id` (`rank_id`),
  ADD KEY `wcat_id` (`wcat_id`),
  ADD KEY `info_id` (`info_id`);

--
-- Индексы таблицы `__v7bkp_2023030405202704`
--
ALTER TABLE `__v7bkp_2023030405202704`
  ADD PRIMARY KEY (`id`) USING BTREE,
  ADD KEY `country_id` (`country_id`),
  ADD KEY `rank_id` (`rank_id`),
  ADD KEY `wcat_id` (`wcat_id`),
  ADD KEY `info_id` (`info_id`);

--
-- Индексы таблицы `__v7bkp_2023030407085304`
--
ALTER TABLE `__v7bkp_2023030407085304`
  ADD PRIMARY KEY (`id`) USING BTREE,
  ADD UNIQUE KEY `op_index` (`id`),
  ADD UNIQUE KEY `nop_index` (`id`),
  ADD KEY `country_id` (`country_id`),
  ADD KEY `rank_id` (`rank_id`),
  ADD KEY `wcat_id` (`wcat_id`),
  ADD KEY `info_id` (`info_id`);

--
-- Индексы таблицы `__v7bkp_2023030409263104`
--
ALTER TABLE `__v7bkp_2023030409263104`
  ADD PRIMARY KEY (`id`) USING BTREE,
  ADD UNIQUE KEY `op_index` (`id`),
  ADD UNIQUE KEY `nop_index` (`id`),
  ADD KEY `country_id` (`country_id`),
  ADD KEY `rank_id` (`rank_id`),
  ADD KEY `wcat_id` (`wcat_id`),
  ADD KEY `info_id` (`info_id`);

--
-- Индексы таблицы `__v7bkp_2023030412383904`
--
ALTER TABLE `__v7bkp_2023030412383904`
  ADD PRIMARY KEY (`id`) USING BTREE,
  ADD UNIQUE KEY `op_index` (`id`),
  ADD UNIQUE KEY `nop_index` (`id`),
  ADD KEY `country_id` (`country_id`),
  ADD KEY `rank_id` (`rank_id`),
  ADD KEY `wcat_id` (`wcat_id`),
  ADD KEY `info_id` (`info_id`);

--
-- Индексы таблицы `__v7bkp_2023030416292904`
--
ALTER TABLE `__v7bkp_2023030416292904`
  ADD PRIMARY KEY (`id`) USING BTREE,
  ADD UNIQUE KEY `op_index` (`id`),
  ADD UNIQUE KEY `nop_index` (`id`),
  ADD KEY `country_id` (`country_id`),
  ADD KEY `rank_id` (`rank_id`),
  ADD KEY `wcat_id` (`wcat_id`),
  ADD KEY `info_id` (`info_id`);

--
-- Индексы таблицы `__v7bkp_2023031522291115`
--
ALTER TABLE `__v7bkp_2023031522291115`
  ADD PRIMARY KEY (`id`) USING BTREE,
  ADD UNIQUE KEY `op_index` (`id`),
  ADD UNIQUE KEY `nop_index` (`id`),
  ADD KEY `country_id` (`country_id`),
  ADD KEY `rank_id` (`rank_id`),
  ADD KEY `wcat_id` (`wcat_id`),
  ADD KEY `info_id` (`info_id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `cities`
--
ALTER TABLE `cities`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT для таблицы `country`
--
ALTER TABLE `country`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=228;

--
-- AUTO_INCREMENT для таблицы `info`
--
ALTER TABLE `info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `opt`
--
ALTER TABLE `opt`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT для таблицы `ranks`
--
ALTER TABLE `ranks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=60;

--
-- AUTO_INCREMENT для таблицы `region`
--
ALTER TABLE `region`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1613;

--
-- AUTO_INCREMENT для таблицы `v7now`
--
ALTER TABLE `v7now`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `v7staff`
--
ALTER TABLE `v7staff`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=273;

--
-- AUTO_INCREMENT для таблицы `v7stat`
--
ALTER TABLE `v7stat`
  MODIFY `id` int(9) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `v7timer`
--
ALTER TABLE `v7timer`
  MODIFY `id` int(5) NOT NULL AUTO_INCREMENT COMMENT 'id', AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT для таблицы `wcat`
--
ALTER TABLE `wcat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT для таблицы `_v7athlete`
--
ALTER TABLE `_v7athlete`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT для таблицы `__v7bkp_2023020119434501`
--
ALTER TABLE `__v7bkp_2023020119434501`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;

--
-- AUTO_INCREMENT для таблицы `__v7bkp_2023030405202704`
--
ALTER TABLE `__v7bkp_2023030405202704`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT для таблицы `__v7bkp_2023030407085304`
--
ALTER TABLE `__v7bkp_2023030407085304`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `__v7bkp_2023030409263104`
--
ALTER TABLE `__v7bkp_2023030409263104`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `__v7bkp_2023030412383904`
--
ALTER TABLE `__v7bkp_2023030412383904`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- AUTO_INCREMENT для таблицы `__v7bkp_2023030416292904`
--
ALTER TABLE `__v7bkp_2023030416292904`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `__v7bkp_2023031522291115`
--
ALTER TABLE `__v7bkp_2023031522291115`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `v7now`
--
ALTER TABLE `v7now`
  ADD CONSTRAINT `att_country_fk1` FOREIGN KEY (`country_id`) REFERENCES `country` (`id`),
  ADD CONSTRAINT `att_weight_cat_fk1` FOREIGN KEY (`wcat_id`) REFERENCES `wcat` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
