"""
Может ли кортеж, содержащий список, быть ключом словаря? Почему?


Да может, потому как кортеж является неизменяемым типом данных, за исключением того, что если в кортеже содержится
изменяемый объект, например список, и после использования как ключом, список может изменится и тогда словарь не
сможет найти этот ключ.

"""
