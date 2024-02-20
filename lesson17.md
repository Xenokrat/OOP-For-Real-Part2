# Занятие 17

## Пример 1

Допустим у нас есть базовый класс `Отчёт`.
Отчеты могут сохранятся в разных форматах, например в `.csv` или `.xlsx`, поэтому кажется логичным создать классы-наследники:
`XLSXОтчёт`, `CSVОтчёт` и т.д.

Однако у нас возникнет проблема в случае, если есть например, еженедельный и ежедневные отчеты.
И каждый из этих типов отчетов могут сохраняться в любом формате.

Тогда при каждом новом типе отчета нам нужно будет создавать под него дополнительный класс, вроде `XLSXЕжемесячныйОтчет`.
Чтобы избежать этого, возможно стоит реализовать механизм сохранения отчёта в определенном формате через композицию, когда отчётыэ
будут иметь атрибут `saver: Saver`, где `Saver` - АТД для разничных классов, реализующих сохранение.

## Пример 2

Схожая ситуация, если есть необходимость продавать чай в виде пакетиков, или листовой.
(классы `Чай`
    `ПакетированныйЧай` < `Чай`
    `ЛистовойЧай`       < `Чай`)

Чай скорее всего бывает множества сортов, при реализации такой иерархии нам придется реализовывать дополнительные классы под каждый сорт.
В таком случае, вероятно, наиболее эффективно также реализовать формат хранения чая в виде атрибута класса и композицию.