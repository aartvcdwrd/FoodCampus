"""FoodCampus. Модуль скидок (DiscountModule).

User Story: как студент-льготник, я хочу подтвердить студбилет,
чтобы получить скидку 15%.

Интерфейс: apply_student_discount(card_id)
"""


class DiscountModule:
    """Проверка валидности номера студбилета и расчёт процента льготы."""
    external_verification = "Stub"

    STUDENT_DISCOUNT = 0.15      # скидка 15%
    CARD_LENGTH = 8              # ожидаемая длина номера билета

    def apply_student_discount(self, card_id):
        """Возвращает коэффициент скидки: 0.15 или 0.0."""
        if len(card_id) == self.CARD_LENGTH:
            return self.STUDENT_DISCOUNT
        return 0.0
