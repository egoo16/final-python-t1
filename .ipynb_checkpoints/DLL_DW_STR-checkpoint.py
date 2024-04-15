DDL_QUERY =  '''
CREATE TABLE IF NOT EXISTS d_personas (
    id_persona INT AUTO_INCREMENT PRIMARY KEY,
    tipo_persona VARCHAR(20) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    tipo_documento VARCHAR(20) NOT NULL,
    num_documento VARCHAR(20) NOT NULL,
    direccion VARCHAR(70),
    telefono VARCHAR(20),
    email VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS d_articulos (
    id_articulo INT AUTO_INCREMENT PRIMARY KEY,
    categoria VARCHAR(50) NOT NULL,
    codigo_articulo VARCHAR(50) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    precio_venta DECIMAL(11,2) DEFAULT 0
);

CREATE TABLE IF NOT EXISTS d_usuarios (
    id_usuario INT AUTO_INCREMENT PRIMARY KEY,
    rol_usuario VARCHAR(30) NOT NULL,
    nombre VARCHAR(100) NOT NULL,
    tipo_documento VARCHAR(20) NOT NULL,
    num_documento VARCHAR(20) NOT NULL,
    direccion VARCHAR(70),
    telefono VARCHAR(20),
    email VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS d_fechas (
  `id_fecha` int NOT NULL AUTO_INCREMENT,
  `full_date` date NOT NULL,
  `day_of_week` int NOT NULL,
  `month` tinyint DEFAULT NULL,
  `quarter` tinyint NOT NULL,
  `year` int NOT NULL,
  `day` int DEFAULT NULL,
  PRIMARY KEY (`id_fecha`)
);

CREATE TABLE IF NOT EXISTS h_ventas_ingresos (
    id_venta INT AUTO_INCREMENT PRIMARY KEY,
    id_cliente INT NOT NULL,
    id_usuario INT NOT NULL,
    id_articulo INT NOT NULL,
    id_fecha INT NOT NULL,
    tipo_movimiento VARCHAR(7) NOT NULL,
    tipo_comprobante VARCHAR(20) NOT NULL,
    serie_comprobante VARCHAR(7) NOT NULL,
    num_comprobante VARCHAR(10) NOT NULL,
    impuesto DECIMAL(4,2) DEFAULT 0,
    total DECIMAL(11,2) DEFAULT 0,
    cantidad INT DEFAULT 0,
    precio DECIMAL(11,2) DEFAULT 0,
    descuento DECIMAL(11,2) DEFAULT 0,
    FOREIGN KEY (id_cliente) REFERENCES d_personas(id_persona),
    FOREIGN KEY (id_usuario) REFERENCES d_usuarios(id_usuario),
    FOREIGN KEY (id_articulo) REFERENCES d_articulos(id_articulo),
    FOREIGN KEY (id_fecha) REFERENCES d_fechas(id_fecha)
);

'''