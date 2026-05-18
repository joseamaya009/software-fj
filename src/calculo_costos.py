def calcular_costo(tarifa, duracion, impuesto=0, descuento=0):  # Define una función flexible para calcular costos.
    if tarifa <= 0:  # Valida que la tarifa sea positiva.
        raise ValueError("La tarifa debe ser mayor que cero.")  # Lanza error si la tarifa es inválida.
    if duracion <= 0:  # Valida que la duración sea positiva.
        raise ValueError("La duración debe ser mayor que cero.")  # Lanza error si la duración es inválida.
    if impuesto < 0:  # Valida que el impuesto no sea negativo.
        raise ValueError("El impuesto no puede ser negativo.")  # Lanza error si el impuesto es inválido.
    if descuento < 0 or descuento > 1:  # Valida que el descuento esté entre cero y uno.
        raise ValueError("El descuento debe estar entre 0 y 1.")  # Lanza error si el descuento es inválido.
    subtotal = tarifa * duracion  # Calcula el costo base antes de ajustes.
    valor_impuesto = subtotal * impuesto  # Calcula el valor del impuesto.
    valor_descuento = subtotal * descuento  # Calcula el valor del descuento.
    total = subtotal + valor_impuesto - valor_descuento  # Calcula el total final.
    if total < 0:  # Verifica que el total no quede negativo.
        raise ValueError("El costo final no puede ser negativo.")  # Lanza error si el total es incoherente.
    return total  # Retorna el costo final calculado.


costo_base = calcular_costo(50000, 2)  # Calcula un costo sin impuesto ni descuento.
costo_con_impuesto = calcular_costo(50000, 2, impuesto=0.19)  # Calcula un costo con impuesto.
costo_con_descuento = calcular_costo(50000, 2, descuento=0.10)  # Calcula un costo con descuento.
