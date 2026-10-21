# taxonomy_field_schema()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.install`](_file.md), lines 229–248 · [local source](../../../../source/modules/taxonomy/taxonomy.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install#L229-L248)
- **Module/theme:** taxonomy
- **Implements:** [hook_field_schema()](../../field/field.api.php/hook_field_schema.md)

## Signature

```php
function taxonomy_field_schema($field)
```

## Documentation

```text
Implements hook_field_schema().
```

## Code

```php
function taxonomy_field_schema($field) {
  return array(
    'columns' => array(
      'tid' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => FALSE,
      ),
    ),
    'indexes' => array(
      'tid' => array('tid'),
    ),
    'foreign keys' => array(
      'tid' => array(
        'table' => 'taxonomy_term_data',
        'columns' => array('tid' => 'tid'),
      ),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.install](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.install) · Licensed GPL-2.0-or-later (see LICENSE)._
