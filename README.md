# FoodCampus
#3. Bug Report (bug_report.md)
ID	Модуль и метод	Входные данные	Ожидаемый результат	Фактический результат
BUG-01	DiscountModule.apply_student_discount	Номер билета: "ABC-1234" (текст вместо цифр, ровно 8 символов)	Скидка 0% или сообщение о неверном формате номера.	Возвращена скидка 15% — модуль проверяет только длину строки, а не её формат.
BUG-02	DiscountModule.apply_student_discount	card_id = None	Корректная обработка: скидка 0% и/или сообщение о неверном формате.	Программа упала с ошибкой TypeError: object of type 'NoneType' has no len().
