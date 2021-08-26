CREATE OR REPLACE PROCEDURE TRABAJO_2.INSERTAR_PRODUCTO(
    CODIGO_PRODUCTO_ENTRADA IN PRODUCTO.CODIGO_PRODUCTO%TYPE,
    NOMBRE_ENTRADA IN PRODUCTO.NOMBRE%TYPE,
    PRECIO_ENTRADA IN PRODUCTO.PRECIO%TYPE,
    CODIGO_CATEGORIA_ENTRADA IN PRODUCTO.CODIGO_CATEGORIA%TYPE,
    STOCK_ENTRADA IN PRODUCTO.STOCK%TYPE
)
IS
    REPETICION_CODIGO_PRODUCTO NUMBER;
    REPETICION_NOMBRE NUMBER;
    REPETICION_CODIGO_CATEGORIA NUMBER;
    CODIGO_PRODUCTO_ES_NULL EXCEPTION;
    NOMBRE_ES_NULL EXCEPTION;
    PRECIO_ES_NULL EXCEPTION;
    CODIGO_CATEGORIA_ES_NULL EXCEPTION;
    STOCK_ES_NULL EXCEPTION;
    CODIGO_INVALIDO EXCEPTION;
    CODIGO_PRODUCTO_YA_EN_USO EXCEPTION;
    NOMBRE_YA_EN_USO EXCEPTION;
    PRECIO_INVALIDO EXCEPTION;
    CODIGO_CATEGORIA_INVALIDO EXCEPTION;
    STOCK_INVALIDO EXCEPTION;
BEGIN
    LOCK TABLE PRODUCTO IN ROW EXCLUSIVE MODE;
    SELECT COUNT(*) INTO REPETICION_CODIGO_PRODUCTO
    FROM PRODUCTO
    WHERE CODIGO_PRODUCTO = CODIGO_PRODUCTO_ENTRADA;
    SELECT COUNT(*) INTO REPETICION_NOMBRE
    FROM PRODUCTO
    WHERE NOMBRE = NOMBRE_ENTRADA;
    SELECT COUNT(*) INTO REPETICION_CODIGO_CATEGORIA
    FROM CATEGORIA
    WHERE CODIGO_CATEGORIA = CODIGO_CATEGORIA_ENTRADA;
    -- VALORES NULL
    IF CODIGO_PRODUCTO_ENTRADA IS NULL OR NOMBRE_ENTRADA IS NULL OR PRECIO_ENTRADA IS NULL OR CODIGO_CATEGORIA_ENTRADA IS NULL OR STOCK_ENTRADA IS NULL THEN 
        IF CODIGO_PRODUCTO_ENTRADA IS NULL THEN 
            RAISE CODIGO_PRODUCTO_ES_NULL;
        ELSIF NOMBRE_ENTRADA IS NULL THEN
            RAISE NOMBRE_ES_NULL;
        ELSIF PRECIO_ENTRADA IS NULL THEN 
            RAISE PRECIO_ES_NULL;
        ELSIF CODIGO_CATEGORIA_ENTRADA IS NULL THEN 
            RAISE CODIGO_CATEGORIA_ES_NULL;
        ELSE 
            RAISE STOCK_ES_NULL;
        END IF;
    -- CODIGO PRODUCTO
    ELSIF REPETICION_CODIGO_PRODUCTO < 0 THEN
        RAISE CODIGO_INVALIDO;
    ELSIF REPETICION_CODIGO_PRODUCTO = 1 THEN
        RAISE CODIGO_PRODUCTO_YA_EN_USO;
    -- NOMBRE
    ELSIF REPETICION_NOMBRE = 1 THEN
        RAISE NOMBRE_YA_EN_USO;
    -- PRECIO
    ELSIF PRECIO_ENTRADA < 1 THEN
        RAISE PRECIO_INVALIDO;
    -- CODIGO CATEGORIA
    ELSIF REPETICION_CODIGO_CATEGORIA = 0 THEN
        RAISE CODIGO_CATEGORIA_INVALIDO;
    -- STOCK
    ELSIF STOCK_ENTRADA < 0 THEN
        RAISE STOCK_INVALIDO;
    ELSE
        INSERT INTO PRODUCTO VALUES(CODIGO_PRODUCTO_ENTRADA,NOMBRE_ENTRADA,PRECIO_ENTRADA,CODIGO_CATEGORIA_ENTRADA,STOCK_ENTRADA);
        DBMS_OUTPUT.PUT_LINE('DATOS INGRESADOS');
        COMMIT;
    END IF;

    EXCEPTION
        -- NULL
        WHEN CODIGO_PRODUCTO_ES_NULL THEN
            DBMS_OUTPUT.PUT_LINE('EL CODIGO DEL PRODUCTO ES NULL');
            ROLLBACK;
        WHEN NOMBRE_ES_NULL THEN
            DBMS_OUTPUT.PUT_LINE('EL NOMBRE DE LA CATEGORIA ES NULL');
            ROLLBACK;
        WHEN PRECIO_ES_NULL THEN
            DBMS_OUTPUT.PUT_LINE('PRECIO DEL PRODUCTO ES NULL');
            ROLLBACK;
        WHEN CODIGO_CATEGORIA_ES_NULL THEN
            DBMS_OUTPUT.PUT_LINE('EL CODIGO DE LA CCATEGORIA ES NULL');
            ROLLBACK;
        WHEN STOCK_ES_NULL THEN
            DBMS_OUTPUT.PUT_LINE('EL STOCK ES NULL');
            ROLLBACK;
        -- CODIGO PRODUCTO
        WHEN CODIGO_INVALIDO THEN
            DBMS_OUTPUT.PUT_LINE('NO PUEDE INGRESAR ESE CODIGO');
            ROLLBACK;
        WHEN CODIGO_PRODUCTO_YA_EN_USO THEN
            DBMS_OUTPUT.PUT_LINE('ESE CODIGO YA SIENDO USADO POR OTRO PRODUCTO');
            ROLLBACK;
        -- NOMBRE
        WHEN NOMBRE_YA_EN_USO THEN 
            DBMS_OUTPUT.PUT_LINE('UN PRODUCTO YA TIENE ESE NOMBRE');
            ROLLBACK;
        -- PRECIO
        WHEN PRECIO_INVALIDO THEN
            DBMS_OUTPUT.PUT_LINE('EL PRODUCTO DEBE VALER 1 O MAS');
            ROLLBACK;
        -- CODIGO CATEGORIA
        WHEN CODIGO_CATEGORIA_INVALIDO THEN
            DBMS_OUTPUT.PUT_LINE('NO EXISTE ESE CODIGO DE CATEGORIA');
            ROLLBACK;
        -- STOCK
        WHEN STOCK_INVALIDO THEN
            DBMS_OUTPUT.PUT_LINE('NO SE PUEDE TENER STOCK NEGETIVO');
            ROLLBACK;
        WHEN OTHERS THEN
            DBMS_OUTPUT.PUT_LINE('ERROR NO IDENTIFICADO');
            ROLLBACK;
END;