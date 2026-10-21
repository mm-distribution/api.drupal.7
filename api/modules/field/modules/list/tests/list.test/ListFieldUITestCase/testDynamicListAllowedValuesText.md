# ListFieldUITestCase::testDynamicListAllowedValuesText()

- **Type:** Method
- **File:** [`modules/field/modules/list/tests/list.test`](../_file.md), lines 427–434 · [local source](../../../../../../../../source/modules/field/modules/list/tests/list.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test#L427-L434)
- **Class:** [ListFieldUITestCase](../ListFieldUITestCase.md)
- **Module/theme:** list_test

## Signature

```php
function testDynamicListAllowedValuesText()
```

## Documentation

```text
List (text) : test 'allowed values function' input.
```

## Code

```php
  function testDynamicListAllowedValuesText() {
    $this->field_name = 'field_list_text';
    $this->createListField('list_text', array(
      'allowed_values_function' => 'list_test_dynamic_values_callback',
      'allowed_values' => '',
    ));
    $this->drupalGet($this->admin_path);
  }
```

---
_Drupal 7.103 · [modules/field/modules/list/tests/list.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test) · Licensed GPL-2.0-or-later (see LICENSE)._
