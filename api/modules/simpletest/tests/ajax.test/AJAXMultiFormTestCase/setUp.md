# AJAXMultiFormTestCase::setUp()

- **Type:** Method
- **File:** [`modules/simpletest/tests/ajax.test`](../_file.md), lines 449–470 · [local source](../../../../../../source/modules/simpletest/tests/ajax.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test#L449-L470)
- **Class:** [AJAXMultiFormTestCase](../AJAXMultiFormTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp(array('form_test'));

    // Create a multi-valued field for 'page' nodes to use for Ajax testing.
    $field_name = 'field_ajax_test';
    $field = array(
      'field_name' => $field_name,
      'type' => 'text',
      'cardinality' => FIELD_CARDINALITY_UNLIMITED,
    );
    field_create_field($field);
    $instance = array(
      'field_name' => $field_name,
      'entity_type' => 'node',
      'bundle' => 'page',
    );
    field_create_instance($instance);

    // Login a user who can create 'page' nodes.
    $this->web_user = $this->drupalCreateUser(array('create page content'));
    $this->drupalLogin($this->web_user);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/ajax.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/ajax.test) · Licensed GPL-2.0-or-later (see LICENSE)._
