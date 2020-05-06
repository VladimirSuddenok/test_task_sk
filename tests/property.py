class UserProperty:
    '''Helper class for tests P_user'''
    @staticmethod
    def setter(p_user):
        p_user.id = 'id1'
        p_user.firstname = 'firstname1'
        p_user.surname = 'surname1'
        p_user.middlename = 'middlename'
        p_user.fio = 'fio1'
        p_user.sex = 'sex1'
        p_user.age = 50

    @staticmethod
    def getter(p_user):
        id = p_user.id
        firstname = p_user.firstname
        surname = p_user.surname
        middlename = p_user.middlename
        fio = p_user.fio
        sex = p_user.sex
        age = p_user.age

        return (id, firstname, surname, 
                middlename, fio, sex, age)

class FriendRecordPropertry:
    '''Helper class for tests Friend_record'''
    @staticmethod
    def setter(friend_record, user_id, friend_id):
        friend_record.id = 'id1'
        friend_record.user_id = user_id
        friend_record.friend_id = friend_id

    @staticmethod
    def getter(friend_record):
        id = friend_record.id
        user_id = friend_record.user_id
        friend_id = friend_record.friend_id

        return (id, firstname, surname)

class TypeCurrencyProperty:
    '''Helper class for tests Type_currency'''
    @staticmethod
    def setter(type_currency):
        type_currency.id = 'id1'
        type_currency.name = 'name'

    @staticmethod
    def getter(type_currency):
        id = type_currency.id
        name = type_currency.name

        return (id, name)

class OrderProperty:
    '''Helper class for tests Order'''
    @staticmethod
    def setter(p_order, user_id):
        p_order.id = 'id1'
        p_order.number = '1'
        p_order.user_id = user_id

    @staticmethod
    def getter(p_order):
        id = p_order.id
        number = p_order.number
        user_id = p_order.user_id

        return (id, number, user_id)

class ProductProperty:
    '''Helper class for tests Product'''
    @staticmethod
    def setter(product):
        product.id = 'id1'
        product.name = 'name'
        product.descriptions = 'descriptions'
        product.left_in_stock = 1

    @staticmethod
    def getter(product):
        id = product.id
        name = product.name
        description = product.description
        left_in_stock = product.left_in_stock

        return (id, name, description, left_in_stock)

class PriceProperty:
    '''Helper class for tests Price'''
    @staticmethod
    def setter(price, product_id, type_currency_id):
        price.id = 'id1'
        price.product_id = product_id
        price.amount = 1
        price.type_currency_id = type_currency_id

    @staticmethod
    def getter(price):
        id = price.id
        product_id = price.product_id
        amount = price.amount
        type_currency_id = price.type_currency_id

        return (id, product_id, amount, type_currency_id)

class ProductRecordProperty:
    '''Helper class for tests ProductRecord'''
    @staticmethod
    def setter(product_record, product_id, order_id):
        product_record.id = 'id1'
        product_record.product_id = product_id
        product_record.order_id = order_id

    @staticmethod
    def getter(product_record):
        id = product_record.id
        product_id = product_record.product_id
        order_id = product_record.order_id

        return (id, product_id, order_id)