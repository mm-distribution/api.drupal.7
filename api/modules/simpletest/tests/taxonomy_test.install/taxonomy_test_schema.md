# taxonomy_test_schema()

- **Type:** Function
- **File:** [`modules/simpletest/tests/taxonomy_test.install`](_file.md), lines 11–34 · [local source](../../../../../source/modules/simpletest/tests/taxonomy_test.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.install#L11-L34)
- **Module/theme:** batch_test
- **Implements:** [hook_schema()](../../../system/system.api.php/hook_schema.md)

## Signature

```php
function taxonomy_test_schema()
```

## Documentation

```text
Implements hook_schema().
```

## Code

```php
function taxonomy_test_schema() {
  $schema['taxonomy_term_antonym'] = array(
    'description' => 'Stores term antonym.',
    'fields' => array(
      'tid' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
        'description' => 'The {taxonomy_term_data}.tid of the term.',
      ),
      'name' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
        'description' => 'The name of the antonym.',
      ),
    ),
    'primary key' => array('tid'),
  );

  return $schema;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/taxonomy_test.install](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/taxonomy_test.install) · Licensed GPL-2.0-or-later (see LICENSE)._
