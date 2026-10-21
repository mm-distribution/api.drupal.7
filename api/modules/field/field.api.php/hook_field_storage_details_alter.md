# hook_field_storage_details_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/field/field.api.php`](_file.md), lines 1769–1784 · [local source](../../../../source/modules/field/field.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php#L1769-L1784)
- **Module/theme:** field
- **Topics:** [hooks](../../../topics/hooks.md), [field_storage](../../../topics/field_storage.md)

## Signature

```php
function hook_field_storage_details_alter(&$details, $field)
```

## Documentation

```text
Perform alterations on Field API storage details.

@param $details
  An array of storage details for fields as exposed by
  hook_field_storage_details() implementations.
@param $field
  A field structure.

@see hook_field_storage_details()
```

## Code

```php
function hook_field_storage_details_alter(&$details, $field) {
  if ($field['field_name'] == 'field_of_interest') {
    $columns = array();
    foreach ((array) $field['columns'] as $column_name => $attributes) {
      $columns[$column_name] = $column_name;
    }
    $details['drupal_variables'] = array(
      FIELD_LOAD_CURRENT => array(
        'moon' => $columns,
      ),
      FIELD_LOAD_REVISION => array(
        'mars' => $columns,
      ),
    );
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_field_storage_details_alter()".

- [field_test_field_storage_details_alter()](../tests/field_test.storage.inc/field_test_field_storage_details_alter.md) — `modules/field/tests/field_test.storage.inc`

---
_Drupal 7.103 · [modules/field/field.api.php](https://github.com/drupal/drupal/blob/7.103/modules/field/field.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
