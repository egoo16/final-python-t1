DDL_QUERY =  '''
-- Eliminar tabla si existe y luego crear tabla categoria
DROP TABLE IF EXISTS categoria;
CREATE TABLE categoria (
    idcategoria SERIAL PRIMARY KEY,
    nombre varchar(50),
    descripcion varchar(255),
    estado boolean
);

-- Eliminar tabla si existe y luego crear tabla articulo
DROP TABLE IF EXISTS articulo;
CREATE TABLE articulo (
    idarticulo SERIAL PRIMARY KEY,
    idcategoria int,
    codigo varchar(50),
    nombre varchar(100),
    precio_venta decimal(11, 2),
    stock int,
    descripcion varchar(255),
    imagen varchar(20),
    estado boolean,
    FOREIGN KEY (idcategoria) REFERENCES categoria (idcategoria)
);

-- Eliminar tabla si existe y luego crear tabla persona
DROP TABLE IF EXISTS persona;
CREATE TABLE persona (
    idpersona SERIAL PRIMARY KEY,
    tipo_persona varchar(20),
    nombre varchar(100),
    tipo_documento varchar(20),
    num_documento varchar(20),
    direccion varchar(70),
    telefono varchar(20),
    email varchar(50)
);

-- Eliminar tabla si existe y luego crear tabla usuario
DROP TABLE IF EXISTS usuario;
CREATE TABLE usuario (
    idusuario SERIAL PRIMARY KEY,
    idrol int,
    nombre varchar(100),
    tipo_documento varchar(20),
    num_documento varchar(20),
    direccion varchar(70),
    telefono varchar(20),
    email varchar(50),
    clave varchar(250),
    estado boolean,
    FOREIGN KEY (idrol) REFERENCES rol (idrol)
);

-- Eliminar tabla si existe y luego crear tabla rol
DROP TABLE IF EXISTS rol;
CREATE TABLE rol (
    idrol SERIAL PRIMARY KEY,
    nombre varchar(30),
    descripcion varchar(255)
);

-- Eliminar tabla si existe y luego crear tabla ingreso
DROP TABLE IF EXISTS ingreso;
CREATE TABLE ingreso (
    idingreso SERIAL PRIMARY KEY,
    idproveedor int,
    idusuario int,
    tipo_comprobante varchar(20),
    serie_comprobante varchar(7),
    num_comprobante varchar(10),
    fecha timestamp,
    impuesto decimal(4, 2),
    total decimal(11, 2),
    estado boolean,
    FOREIGN KEY (idproveedor) REFERENCES persona (idpersona),
    FOREIGN KEY (idusuario) REFERENCES usuario (idusuario)
);

-- Eliminar tabla si existe y luego crear tabla detalle_ingreso
DROP TABLE IF EXISTS detalle_ingreso;
CREATE TABLE detalle_ingreso (
    iddetalle_ingreso SERIAL PRIMARY KEY,
    idingreso int,
    idarticulo int,
    cantidad int,
    precio decimal(11, 2),
    FOREIGN KEY (idingreso) REFERENCES ingreso (idingreso),
    FOREIGN KEY (idarticulo) REFERENCES articulo (idarticulo)
);

-- Eliminar tabla si existe y luego crear tabla venta
DROP TABLE IF EXISTS venta;
CREATE TABLE venta (
    idventa SERIAL PRIMARY KEY,
    idcliente int,
    idusuario int,
    tipo_comprobante varchar(20),
    serie_comprobante varchar(7),
    num_comprobante varchar(10),
    fecha timestamp,
    impuesto decimal(4, 2),
    total decimal(11, 2),
    estado boolean,
    FOREIGN KEY (idcliente) REFERENCES persona (idpersona),
    FOREIGN KEY (idusuario) REFERENCES usuario (idusuario)
);

-- Eliminar tabla si existe y luego crear tabla detalle_venta
DROP TABLE IF EXISTS detalle_venta;
CREATE TABLE detalle_venta (
    iddetalle_venta SERIAL PRIMARY KEY,
    idventa int,
    idarticulo int,
    cantidad int,
    precio decimal(11, 2),
    descuento decimal(11, 2),
    FOREIGN KEY (idventa) REFERENCES venta (idventa),
    FOREIGN KEY (idarticulo) REFERENCES articulo (idarticulo)
);

'''