## *GIT:*

#### *Qué es?*

Es un sistema de control de versiones que se utiliza para controlar los diferentes archivos usados por diferentes personas, las cuales pueden trabajar en paralelo usando programas o herramientas específicas.

Es una especie de “nube”, pero lleva un registro de los cambios.

Unha vez instalamos git, debemos establecer nuestro usuario y correo electrónico con dos comandos:

`git config --global user.name`

`git config --global user.email`

Después de esto, es necesario crear un cartafol (directorio), donde irá el repositorio.

### *CICLO DE TRABALLO GIT:*

1.	**Repositorio:**
Aquí tenemos acumulados los cambios. Para pasar a la siguiente etapa debemos hacer un “pull” del sitio donde la información fue cambiada.

    `git pull`

2.	**Cartafol de traballo:**
Aquí estamos cambiando el contenido de los archivos. Para esto tenemos que hacer un “git add”. De esta manera los estamos añadiendo al repositorio.

    `git add <archivo>`

3.	**Preparación:**
Para esto tenemos que hacer un commit, que tiene que llevar un mensaje claro identificándose. Después se hace un "push".

    `git commit -m “mensaje”`

    `git push`