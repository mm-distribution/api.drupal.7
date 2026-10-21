# ListFieldUITestCase

- **Type:** Class
- **File:** [`modules/field/modules/list/tests/list.test`](_file.md), lines 212–490 · [local source](../../../../../../../source/modules/field/modules/list/tests/list.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test#L212-L490)
- **Module/theme:** list_test

## Signature

```php
class ListFieldUITestCase extends FieldTestCase
```

## Documentation

```text
List module UI tests.
```

## Properties

### $type

```php
protected $type;
```

### $hyphen_type

```php
protected $hyphen_type;
```

### $field_name

```php
protected $field_name;
```

### $admin_path

```php
protected $admin_path;
```

## Methods (derived index)

- [getInfo()](ListFieldUITestCase/getInfo.md)
- [setUp()](ListFieldUITestCase/setUp.md)
- [testListAllowedValuesInteger()](ListFieldUITestCase/testListAllowedValuesInteger.md) — List (integer) : test 'allowed values' input.
- [testListAllowedValuesFloat()](ListFieldUITestCase/testListAllowedValuesFloat.md) — List (float) : test 'allowed values' input.
- [testListAllowedValuesText()](ListFieldUITestCase/testListAllowedValuesText.md) — List (text) : test 'allowed values' input.
- [testListAllowedValuesBoolean()](ListFieldUITestCase/testListAllowedValuesBoolean.md) — List (boolen) : test 'On/Off' values input.
- [testDynamicListAllowedValuesText()](ListFieldUITestCase/testDynamicListAllowedValuesText.md) — List (text) : test 'allowed values function' input.
- [createListField()](ListFieldUITestCase/createListField.md) — Helper function to create list field of a given type.
- [assertAllowedValuesInput()](ListFieldUITestCase/assertAllowedValuesInput.md) — Tests a string input for the 'allowed values' form element.

---
_Drupal 7.103 · [modules/field/modules/list/tests/list.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test) · Licensed GPL-2.0-or-later (see LICENSE)._
