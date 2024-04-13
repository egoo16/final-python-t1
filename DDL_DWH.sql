CREATE DATABASE Tienda;
USE Tienda;
CREATE TABLE h_ventas_ingresos
(
	id_venta int not null primary key,
    id_cliente int not null references d_clientes(id_cliente),
    id_usuario int not null references d_usuarios(id_usuario),
    id_articulo int not null references d_articulos(id_articulo),
    id_fecha int not null references d_fechas(id_fecha),
    tipo_movimiento varchar(7) not null,
    tipo_comprobante varchar(20) not null,
    serie_comprobante varchar(7) not null,
    num_comprobante varchar(10) not null,
    impuesto decimal(4,2) default 0,
    total decimal(11,2) default 0,
    cantidad int default 0,
    precio decimal(11,2) default 0,
    descuento decimal(11,2) default 0
);

CREATE TABLE d_personas
(
	id_persona int not null primary key,
    tipo_persona varchar(20) not null,
    nombre varchar(100) not null,
    tipo_documento varchar(20) not null,
    num_documento varchar(20) not null,
    direccion varchar(70),
    telefono varchar(20),
    email varchar(50)
);

CREATE TABLE d_articulos
(
	id_articulo int not null primary key,
    categoria varchar(50) not null,
    codigo_articulo varchar(50) not null,
    nombre varchar(100) not null,
    precio_venta decimal(11,2) default 0
);

CREATE TABLE d_usuarios
(
	id_usuario int not null primary key,
    rol_usuario varchar(30) not null,
    nombre varchar(100) not null,
    tipo_documento varchar(20) not null,
    num_documento varchar(20) not null,
    direccion varchar(70),
    telefono varchar(20),
    email varchar(50)
);

create table d_fechas(
	id_fecha int not null primary key,
	full_date date not null,
	day_of_week int not null,
	day_num_in_month int not null,
	day_name varchar(15) not null,
	day_abbrev varchar(10) not null,
	month tinyint,
	month_name varchar(10) not null,
	month_abbrev varchar(10) not null,
	quarter tinyint not null,
	year int not null,
	yearmo int not null,
	fiscal_month tinyint not null,
	fiscal_quarter tinyint not null,
	fiscal_year int not null
);
