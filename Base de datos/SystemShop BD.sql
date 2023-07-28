-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-07-2023 a las 23:10:25
-- Versión del servidor: 10.4.27-MariaDB
-- Versión de PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `systemshop`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `ObtenerProductosPorEstudiante` (IN `Matricula` VARCHAR(50))   BEGIN
    SELECT p.* FROM dbo_producto p
    INNER JOIN dbo_estudiantes_producto ep ON p.id_Producto = ep.id_Producto
    WHERE ep.Matricula = Matricula;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dbo_estudiantes`
--

CREATE TABLE `dbo_estudiantes` (
  `Matricula` int(11) NOT NULL,
  `Carrera` varchar(50) NOT NULL,
  `Grupo` varchar(5) NOT NULL,
  `Nombre` varchar(50) NOT NULL,
  `ApPaterno` varchar(50) NOT NULL,
  `ApMaterno` varchar(50) NOT NULL,
  `Correo` varchar(50) NOT NULL,
  `Contra` varchar(50) NOT NULL,
  `Activo` varchar(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `dbo_estudiantes`
--

INSERT INTO `dbo_estudiantes` (`Matricula`, `Carrera`, `Grupo`, `Nombre`, `ApPaterno`, `ApMaterno`, `Correo`, `Contra`, `Activo`) VALUES
(1, 'Sistemas', 'S185', 'Prueba', 'Solano', 'Sanchez', '119033915@upq.edu.mx', '123', 'SI'),
(12, 'Sistemas', 's123', 'a', 'v', 'c', '12@upq.com', '1234', 'NO'),
(13, 'Sistemas', 'S185', 'Luis', 'Garcia', 'Estrada', '13@upq.com', '2468', 'NO'),
(1234, 'Sistemas', 'S172', 'Usuario', 'de', 'Prueba', '1234@gmail.com', '1234', 'SI'),
(123456, 'Sistemas', 'S173', 'Luis', 'Suarez', '', '123456@upq.mx', '1234', 'SI'),
(246810, 'Sistemas', 'S198', 'Jose', 'Contreras', '', '246810@upq.com', '1234', 'SI'),
(1234567, 'Sistemas', 'S167', 'Usuario', 'Gonzalez', '', '1234567@upq.com', '1234', 'NO'),
(12345678, 'Sistemas', 'S182', 'PRUEBA', 'ERW', 'REWREW', '1234567890@UPQ.COM', '12345', 'NO'),
(112023002, 'Sistemas', 'S188', 'Eduardo', 'Ortiz', 'Reyes', '112023002@upq.com', '1234', 'NO'),
(119033914, 'Sistemas', 'S185', 'Joaquin', 'Solano', 'Sanchez', '119033914@upq.edu.mx', '1234', 'SI'),
(120039493, 'Sistemas', 'S173', 'Alma', 'Franco', 'Ramirez', '120039493@upq.com', '7412', 'SI'),
(121039717, 'Sistemas', 'S185', 'Jesus', 'Gutierrez', 'Hernandez', '121039717@upq.edu.mx', 'EligibleIowa86', 'SI'),
(121039836, 'Sistemas', 'S185', 'Jose', 'Martinez', 'Gomez', '121039836@upq.com', '9632', 'NO'),
(121040187, 'Sistemas', 'S183', 'Edain', 'Hernandez', 'Garcia', '121040187@upq.com', '8523', 'NO'),
(121040701, 'Sistemas', 'S185', 'Kevin', 'Gonzalez', 'Camacho', '121040701@upq.mx', '09876', 'SI'),
(123341213, 'Sistemas', 'S172', 'Alan', 'Lopez', 'Arzola', '123341213@upq.com', '9874', 'SI'),
(123452333, 'Sistemas', 'S180', 'Diego', 'Cruz', 'Alvares', '123452333', '9512', 'SI');

--
-- Disparadores `dbo_estudiantes`
--
DELIMITER $$
CREATE TRIGGER `tr_ActualizarEstudianteActivo` AFTER INSERT ON `dbo_estudiantes` FOR EACH ROW BEGIN
    UPDATE dbo_estudiantes
    SET Activo = 'SI'
    WHERE Matricula = NEW.Matricula;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dbo_estudiantes_producto`
--

CREATE TABLE `dbo_estudiantes_producto` (
  `Matricula` int(11) NOT NULL,
  `Id_Producto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `dbo_estudiantes_producto`
--

INSERT INTO `dbo_estudiantes_producto` (`Matricula`, `Id_Producto`) VALUES
(119033914, 102),
(120039493, 103),
(121039836, 104),
(121040187, 105),
(123341213, 106),
(123452333, 100);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dbo_estudiantes_servicios`
--

CREATE TABLE `dbo_estudiantes_servicios` (
  `Matricula` int(11) NOT NULL,
  `Id_Servicios` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `dbo_estudiantes_servicios`
--

INSERT INTO `dbo_estudiantes_servicios` (`Matricula`, `Id_Servicios`) VALUES
(119033914, 2),
(119033914, 5),
(120039493, 3),
(121039836, 4),
(123341213, 6),
(123452333, 7);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dbo_producto`
--

CREATE TABLE `dbo_producto` (
  `Id_Producto` int(11) NOT NULL,
  `NombreProducto` varchar(80) NOT NULL,
  `Detalles` varchar(500) NOT NULL,
  `Precio` bigint(20) NOT NULL,
  `Marca` varchar(50) NOT NULL,
  `Imagen` varchar(100) DEFAULT 'C:xampp2htdocsSYSTEMSHOPimgProductosDefault_ISC.png',
  `Estado` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `dbo_producto`
--

INSERT INTO `dbo_producto` (`Id_Producto`, `NombreProducto`, `Detalles`, `Precio`, `Marca`, `Imagen`, `Estado`) VALUES
(100, 'Memoria RAM Kingston', 'Ram 8GB', 500, 'Kingston', 'C:\\xampp2\\htdocs\\SYSTEMSHOP\\imgProductos\\Default_ISC.png', 'DISPONIBLE'),
(101, 'Mouse HP', 'Ranton inalambrico', 80, 'HP', 'C:\\xampp2\\htdocs\\SYSTEMSHOP\\imgProductos\\Default_ISC.png', 'DISPONIBLE'),
(102, 'Teclado Ghia', 'Teclado', 200, 'Ghia', 'C:\\xampp2\\htdocs\\SYSTEMSHOP\\imgProductos\\Default_ISC.png', 'DISPONIBLE'),
(103, 'Protoboard', 'Protoboard usada en buen estado', 300, 'Steren', 'C:\\xampp2\\htdocs\\SYSTEMSHOP\\imgProductos\\Default_ISC.png', 'DISPONIBLE'),
(104, 'Memoria USB 16 GB', 'USB', 80, 'Kingston', 'C:\\xampp2\\htdocs\\SYSTEMSHOP\\imgProductos\\Default_ISC.png', 'DISPONIBLE'),
(105, 'Lata de aire comprimido', 'Aire comprimido', 300, 'Steren', 'C:\\xampp2\\htdocs\\SYSTEMSHOP\\imgProductos\\Default_ISC.png', 'DISPONIBLE'),
(106, 'Adaptador HDMI', 'Adaptadores', 400, 'Steren', 'C:\\xampp2\\htdocs\\SYSTEMSHOP\\imgProductos\\Default_ISC.png', 'DISPONIBLE');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dbo_servicios`
--

CREATE TABLE `dbo_servicios` (
  `Id_servicios` int(11) NOT NULL,
  `NombreServicio` varchar(80) DEFAULT NULL,
  `Descripcion` varchar(500) NOT NULL,
  `Fecha_inicio` date NOT NULL,
  `Fecha_Final` date NOT NULL,
  `Imagen` varchar(100) DEFAULT 'C:xampp2htdocsSYSTEMSHOPimgServiciosDefault_ISC.png',
  `Estado` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `dbo_servicios`
--

INSERT INTO `dbo_servicios` (`Id_servicios`, `NombreServicio`, `Descripcion`, `Fecha_inicio`, `Fecha_Final`, `Imagen`, `Estado`) VALUES
(1, 'Mantenimiento a PCs', 'Reparacion de computadoras', '2023-05-02', '2023-05-10', 'C:\\xampp2\\htdocs\\SYSTEMSHOP\\imgServicios\\Default_ISC.png', 'VENCIDO'),
(2, 'Asesorias php', 'Seccion de preguntas php', '2023-05-16', '2023-05-30', 'C:\\xampp2\\htdocs\\SYSTEMSHOP\\imgServicios\\Default_ISC.png', 'VENCIDO'),
(3, 'Mnatenimiento celulares', 'Reparacion de celulares', '2023-06-01', '2023-06-15', 'C:\\xampp2\\htdocs\\SYSTEMSHOP\\imgServicios\\Default_ISC.png', 'VENCIDO'),
(4, 'Creacion de software', 'Desarrollo de software', '2023-06-01', '2023-06-05', 'C:\\xampp2\\htdocs\\SYSTEMSHOP\\imgServicios\\Default_ISC.png', 'VENCIDO'),
(5, 'Asesorias Java', 'Consultoria sobre lenguaje de programacion Java', '2023-06-03', '2023-06-16', 'C:\\xampp2\\htdocs\\SYSTEMSHOP\\imgServicios\\Default_ISC.png', 'VENCIDO'),
(6, 'Creacion de paginas web', 'Diseño y desarrollo de sitios web', '2023-06-08', '2023-06-19', 'C:\\xampp2\\htdocs\\SYSTEMSHOP\\imgServicios\\Default_ISC.png', 'VENCIDO'),
(7, 'Creacion de apps', 'Desarrollo de aplicaciones moviles', '2023-07-09', '2023-07-20', 'C:\\xampp2\\htdocs\\SYSTEMSHOP\\imgServicios\\Default_ISC.png', 'DISPONIBLE'),
(12, 'Prueba', 'Prueba', '2023-07-07', '2023-07-08', 'ruta/prueba', NULL),
(13, 'Prueba', 'Prueba', '2023-07-07', '2023-07-08', 'ruta/prueba', 'DISPONIBLE');

--
-- Disparadores `dbo_servicios`
--
DELIMITER $$
CREATE TRIGGER `tr_Establecer_Estatus_Servicio` AFTER INSERT ON `dbo_servicios` FOR EACH ROW BEGIN
    IF NEW.Fecha_Final > NOW() THEN
        UPDATE dbo_servicios
        SET Estado = 'DISPONIBLE'
        WHERE Id_servicios = NEW.Id_servicios;
    END IF;
END
$$
DELIMITER ;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `dbo_estudiantes`
--
ALTER TABLE `dbo_estudiantes`
  ADD PRIMARY KEY (`Matricula`);

--
-- Indices de la tabla `dbo_estudiantes_producto`
--
ALTER TABLE `dbo_estudiantes_producto`
  ADD PRIMARY KEY (`Matricula`,`Id_Producto`),
  ADD KEY `FK_Estudiantes_Producto_Producto` (`Id_Producto`);

--
-- Indices de la tabla `dbo_estudiantes_servicios`
--
ALTER TABLE `dbo_estudiantes_servicios`
  ADD PRIMARY KEY (`Matricula`,`Id_Servicios`),
  ADD KEY `FK_Estudiantes_Servicios_Servicios` (`Id_Servicios`);

--
-- Indices de la tabla `dbo_producto`
--
ALTER TABLE `dbo_producto`
  ADD PRIMARY KEY (`Id_Producto`);

--
-- Indices de la tabla `dbo_servicios`
--
ALTER TABLE `dbo_servicios`
  ADD PRIMARY KEY (`Id_servicios`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `dbo_estudiantes_producto`
--
ALTER TABLE `dbo_estudiantes_producto`
  ADD CONSTRAINT `FK_Estudiantes_Producto_Estudiantes` FOREIGN KEY (`Matricula`) REFERENCES `dbo_estudiantes` (`Matricula`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `FK_Estudiantes_Producto_Producto` FOREIGN KEY (`Id_Producto`) REFERENCES `dbo_producto` (`Id_Producto`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `dbo_estudiantes_servicios`
--
ALTER TABLE `dbo_estudiantes_servicios`
  ADD CONSTRAINT `FK_Estudiantes_Servicios_Estudiantes` FOREIGN KEY (`Matricula`) REFERENCES `dbo_estudiantes` (`Matricula`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  ADD CONSTRAINT `FK_Estudiantes_Servicios_Servicios` FOREIGN KEY (`Id_Servicios`) REFERENCES `dbo_servicios` (`Id_servicios`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
