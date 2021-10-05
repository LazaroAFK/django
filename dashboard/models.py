from django.db import models


class Almacenaje(models.Model):
    clavealmacenaje = models.IntegerField(db_column='ClaveAlmacenaje', primary_key=True)  # Field name made lowercase.
    tipoalmacenaje = models.CharField(db_column='TipoAlmacenaje', max_length=100)  # Field name made lowercase.
    ciudadalmacenaje = models.CharField(db_column='CiudadAlmacenaje', max_length=100)  # Field name made lowercase.
    ciudadalmacenaje2 = models.CharField(db_column='CiudadAlmacenaje2', max_length=100)  # Field name made lowercase.
    paisalmacenaje = models.CharField(db_column='PaisAlmacenaje', max_length=50)  # Field name made lowercase.
    total_sqft = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'almacenaje'


class Clientes(models.Model):
    clavecliente = models.IntegerField(db_column='ClaveCliente', primary_key=True)  # Field name made lowercase.
    nombrecliente = models.CharField(db_column='NombreCliente', max_length=100)  # Field name made lowercase.
    fechanacimientocliente = models.DateField(db_column='FechaNacimientoCliente')  # Field name made lowercase.
    comprasanualescliente = models.CharField(db_column='ComprasAnualesCliente', max_length=100)  # Field name made lowercase.   
    clavegenero = models.ForeignKey('Generos', models.DO_NOTHING, db_column='ClaveGenero')  # Field name made lowercase.        
    hijoscliente = models.IntegerField(db_column='HijosCliente')  # Field name made lowercase.
    clavetipotarjeta = models.ForeignKey('Tipotarjeta', models.DO_NOTHING, db_column='ClaveTipoTarjeta')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clientes'


class Datos(models.Model):
    clavedato = models.AutoField(db_column='ClaveDato', primary_key=True)  # Field name made lowercase.
    fechatransaccion = models.DateField(db_column='FechaTransaccion')  # Field name made lowercase.
    claveproducto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='ClaveProducto')  # Field name made lowercase.  
    clavecliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='ClaveCliente')  # Field name made lowercase.       
    clavealmacenaje = models.ForeignKey(Almacenaje, models.DO_NOTHING, db_column='ClaveAlmacenaje')  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad')  # Field name made lowercase.
    salesrevenue = models.IntegerField(db_column='SalesRevenue')  # Field name made lowercase.
    costo = models.IntegerField(db_column='Costo')  # Field name made lowercase.
    gananciasperdidas = models.IntegerField(db_column='GananciasPerdidas')  # Field name made lowercase.
    margenganancia = models.DecimalField(db_column='MargenGanancia', max_digits=18, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'datos'


class Generos(models.Model):
    clavegenero = models.CharField(db_column='ClaveGenero', primary_key=True, max_length=2)  # Field name made lowercase.       
    descripciongenero = models.CharField(db_column='DescripcionGenero', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'generos'


class Marcas(models.Model):
    clavemarca = models.IntegerField(db_column='ClaveMarca', primary_key=True)  # Field name made lowercase.
    marcaproducto = models.CharField(db_column='MarcaProducto', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'marcas'


class Productos(models.Model):
    claveproducto = models.IntegerField(db_column='ClaveProducto', primary_key=True)  # Field name made lowercase.
    clavemarca = models.ForeignKey(Marcas, models.DO_NOTHING, db_column='ClaveMarca', blank=True, null=True)  # Field name made lowercase.
    nombreproducto = models.CharField(db_column='NombreProducto', max_length=100)  # Field name made lowercase.
    precioreventa = models.DecimalField(db_column='PrecioReventa', max_digits=18, decimal_places=2)  # Field name made lowercase.
    costoproducto = models.DecimalField(db_column='CostoProducto', max_digits=18, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productos'


class Tipotarjeta(models.Model):
    clavetipotarjeta = models.CharField(db_column='ClaveTipoTarjeta', primary_key=True, max_length=2)  # Field name made lowercase.
    tipotarjetacliente = models.CharField(db_column='TipoTarjetaCliente', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipotarjeta'