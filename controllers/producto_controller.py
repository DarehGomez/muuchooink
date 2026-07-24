from models.producto import Producto


class ProductoController:
    """
    Controlador encargado de gestionar las operaciones relacionadas con los productos.

    Este controlador valida la información recibida desde la vista y coordina
    las operaciones de registro, consulta, actualización y eliminación de
    productos mediante el modelo Producto.
    """

    def registrar_producto(self, producto):
        """
        Valida y registra un nuevo producto en el sistema.

        Args:
            producto (Producto): Objeto que contiene la información del producto.

        Returns:
            tuple: Una tupla (bool, str) donde el primer valor indica si la
            operación fue exitosa y el segundo contiene un mensaje descriptivo.
        """

        if not producto.codigo_barras or not producto.nombre or producto.precio is None or producto.stock_actual is None:
            return False, "Complete todos los campos"

        if len(str(producto.codigo_barras)) < 3:
            return False, "El codigo de barras debe tener al menos 3 caracteres"

        if len(producto.nombre) < 3:
            return False, "El nombre debe tener al menos 3 caracteres"

        try:
            producto.precio = float(producto.precio)
            producto.stock_actual = int(producto.stock_actual)
        except ValueError:
            return False, "Precio y stock deben ser valores numéricos"

        if producto.precio < 0:
            return False, "El precio debe ser mayor o igual a 0"

        if producto.stock_actual < 0:
            return False, "El stock actual debe ser mayor o igual a 0"

        try:
            resultado = producto.guardar()
            if resultado:
                return True, "Producto registrado exitosamente"
            else:
                return False, "No se pudo guardar el producto"
        except Exception as e:
            if "UNIQUE" in str(e):
                return False, "El codigo de barras ya existe"
            return False, f"Error: {str(e)}"

    def obtener_productos(self):
        """
        Obtiene todos los productos registrados en la base de datos.

        Returns:
            list: Lista de objetos Producto.
        """
        return Producto.obtener_todos()

    def actualizar_producto(self, producto):
        """
        Valida y actualiza la información de un producto existente.

        Args:
            producto (Producto): Objeto con la información actualizada del producto.

        Returns:
            tuple: Una tupla (bool, str) indicando el resultado de la operación
            y el mensaje correspondiente.
        """

        if not producto.codigo_barras or not producto.nombre or producto.precio is None or producto.stock_actual is None:
            return False, "Complete todos los campos"

        if len(str(producto.codigo_barras)) < 3:
            return False, "El codigo de barras debe tener al menos 3 caracteres"

        if len(producto.nombre) < 3:
            return False, "El nombre debe tener al menos 3 caracteres"

        try:
            producto.precio = float(producto.precio)
            producto.stock_actual = int(producto.stock_actual)
        except ValueError:
            return False, "Precio y stock deben ser valores numéricos"

        if producto.precio < 0:
            return False, "El precio debe ser mayor o igual a 0"

        if producto.stock_actual < 0:
            return False, "El stock actual debe ser mayor o igual a 0"

        try:
            resultado = producto.guardar()
            if resultado:
                return True, "Producto actualizado exitosamente"
            else:
                return False, "No se pudo actualizar el producto"
        except Exception as e:
            if "UNIQUE" in str(e):
                return False, "El codigo de barras ya existe"
            return False, f"Error: {str(e)}"

    def eliminar_producto(self, producto_id):
        """
        Elimina un producto mediante su identificador.

        Args:
            producto_id (int): Identificador único del producto.

        Returns:
            tuple: Una tupla (bool, str) indicando si la eliminación fue
            exitosa y el mensaje correspondiente.
        """

        if not producto_id:
            return False, "Seleccione un producto"

        resultado = Producto.eliminar(producto_id)

        if resultado:
            return True, "Producto eliminado exitosamente"

        return False, "Error al eliminar el producto"

    def obtener_producto_por_id(self, producto_id):
        """
        Obtiene un producto específico mediante su identificador.

        Args:
            producto_id (int): Identificador único del producto.

        Returns:
            Producto | None: Objeto Producto si existe; en caso contrario,
            devuelve None.
        """
        return Producto.buscar_por_id(producto_id)