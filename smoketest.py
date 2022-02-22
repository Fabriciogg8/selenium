from unittest import TestLoader, TestSuite 
from pyunitreport import HTMLTestRunner # Para generar el reporte correspondiente
# Importamos las clases de nuestros archivos
from assertions import AssertionsTest 
from searchtestb import SearchTest

# Variales que vamos a utilizar
assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)

# Construimos nuestra suite de pruebas, pasando una lista con las variables de pruebas
smoke_test = TestSuite([assertions_test, search_test])

# Parametros para generar el reporte
kwargs = {
    'output':'smoke-report'
}

# Variable para que se genere el reporte como queremos
runner = HTMLTestRunner(**kwargs)

# Corremos el runner, llamando a la suite de testing
runner.run(smoke_test)