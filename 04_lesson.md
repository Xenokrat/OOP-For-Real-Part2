# Основополагающий принцип открытости-закрытости модуля

Рассмотрим следующий набор классов:

```python
class Document(ABC):
    """Абстрактный класс документов"""

class WorkingDocument(Docuemnt): ...

class AccountingDocument(Docuemnt): ...
```

Эти классы представляют собой различные виды документов, обладающие разными своствами.
Однако все они "происходят" от одного родительского класса `Document`.
Если нам нужен документ с поведением, которое не реализовано на данный момент, мы:

1. Не должны пытаться изменить существующие классы, т.к они уже могут использоваться в продакшене (принцип `Close`).
2. Вместо этого, за счет наследования, мы создаем новый подкласс `Docuemnt`а и реализуем все необходимое там (принцип `Open` реализуется за счет наследования).

Также, допустим, у нас есть класс `SignMethod`, который реализует механизм подписание документов выше.
Допустим, этим классом пользуются абсолютно все документы выше, для реализации подписания.
Тогда этот класс (модуль) должен быть строго закрытым, т.к. на него завязана целая другая иерерхия классов.

Однако и тут можно также следать код менее связным, если мы также создадим абстрактный класс для подписания, но при этом на проде будут использовать конкретные реализации, и при необходимости мы также создадим наследника `SignMethod` с новым поведением, если будет такая необходимость.