CREATE DATABASE IF NOT EXISTS TalkHive;

USE TalkHive;
 
CREATE TABLE IF NOT EXISTS Usuarios (
  Id_usuario INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
  nombre VARCHAR(200) DEFAULT NULL,
  correo_electronico VARCHAR (200) DEFAULT NULL,
  cantrasenia VARCHAR (200) DEFAULT NULL,
  fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  ultima_vez DATETIME
  );
  
  CREATE TABLE IF NOT EXISTS Servidores (
  Id_servidor INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
  nombre VARCHAR(200) DEFAULT NULL,
  descripción TEXT,
  fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  );
  
  CREATE TABLE IF NOT EXISTS Usuario_servidor (
  Id_usuario_servidor INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
  Id_usuario INT,
  Id_servidor INT,
  FOREIGN KEY (Id_usuario) REFERENCES Usuarios(Id_usuario),
  FOREIGN KEY (Id_servidor) REFERENCES Servidores(Id_servidor)
  );
 
  CREATE TABLE IF NOT EXISTS Canales (
  Id_canal INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
  nombre VARCHAR(200) DEFAULT NULL,
  tipo VARCHAR(200) DEFAULT NULL, -- (texto, voz, etc.) -- 
  Id_servidor INT,
  fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (Id_servidor) REFERENCES Servidores(Id_servidor)
  );
  
  CREATE TABLE IF NOT EXISTS Chats (
  Id_mensaje INT AUTO_INCREMENT UNIQUE PRIMARY KEY,
  contenido TEXT,
  fecha_hora DATETIME,
  Id_UsuarioEnvia INT,
  Id_CanalEnviado INT,
  FOREIGN KEY (Id_UsuarioEnvia) REFERENCES Usuarios(Id_usuario),
  FOREIGN KEY (Id_CanalEnviado) REFERENCES Canales(Id_canal)
  );
