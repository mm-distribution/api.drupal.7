# field_test_schema()

- **Type:** Function
- **File:** [`modules/field/tests/field_test.install`](_file.md), lines 22–114 · [local source](../../../../../source/modules/field/tests/field_test.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.install#L22-L114)
- **Module/theme:** field_test_schema_alter
- **Implements:** [hook_schema()](../../../system/system.api.php/hook_schema.md)

## Signature

```php
function field_test_schema()
```

## Documentation

```text
Implements hook_schema().
```

## Code

```php
function field_test_schema() {
  $schema['test_entity'] = array(
    'description' => 'The base table for test_entities.',
    'fields' => array(
      'ftid' => array(
        'description' => 'The primary identifier for a test_entity.',
        'type' => 'serial',
        'unsigned' => TRUE,
        'not null' => TRUE,
      ),
      'ftvid' => array(
        'description' => 'The current {test_entity_revision}.ftvid version identifier.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
      ),
      'fttype' => array(
        'description' => 'The type of this test_entity.',
        'type' => 'varchar',
        'length' => 32,
        'not null' => TRUE,
        'default' => '',
      ),
      'ftlabel' => array(
        'description' => 'The label of this test_entity.',
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
      ),
    ),
    'unique keys' => array(
      'ftvid' => array('ftvid'),
    ),
    'primary key' => array('ftid'),
  );
  $schema['test_entity_bundle_key'] = array(
    'description' => 'The base table for test entities with a bundle key.',
    'fields' => array(
      'ftid' => array(
        'description' => 'The primary identifier for a test_entity_bundle_key.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
      ),
      'fttype' => array(
        'description' => 'The type of this test_entity.',
        'type' => 'varchar',
        'length' => 32,
        'not null' => FALSE,
        'default' => '',
      ),
    ),
  );
  $schema['test_entity_bundle'] = array(
    'description' => 'The base table for test entities with a bundle.',
    'fields' => array(
      'ftid' => array(
        'description' => 'The primary identifier for a test_entity_bundle.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
      ),
    ),
  );
  $schema['test_entity_revision'] = array(
    'description' => 'Stores information about each saved version of a {test_entity}.',
    'fields' => array(
      'ftid' => array(
        'description' => 'The {test_entity} this version belongs to.',
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
      ),
      'ftvid' => array(
        'description' => 'The primary identifier for this version.',
        'type' => 'serial',
        'unsigned' => TRUE,
        'not null' => TRUE,
      ),
    ),
    'indexes' => array(
      'nid' => array('ftid'),
    ),
    'primary key' => array('ftvid'),
  );

  return $schema;
}
```

---
_Drupal 7.103 · [modules/field/tests/field_test.install](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field_test.install) · Licensed GPL-2.0-or-later (see LICENSE)._
