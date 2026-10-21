# rdf_schema()

- **Type:** Function
- **File:** [`modules/rdf/rdf.install`](_file.md), lines 11–39 · [local source](../../../../source/modules/rdf/rdf.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.install#L11-L39)
- **Module/theme:** rdf
- **Implements:** [hook_schema()](../../system/system.api.php/hook_schema.md)

## Signature

```php
function rdf_schema()
```

## Documentation

```text
Implements hook_schema().
```

## Code

```php
function rdf_schema() {
  $schema['rdf_mapping'] = array(
    'description' => 'Stores custom RDF mappings for user defined content types or overriden module-defined mappings',
    'fields' => array(
      'type' => array(
        'type' => 'varchar',
        'length' => 128,
        'not null' => TRUE,
        'description' => 'The name of the entity type a mapping applies to (node, user, comment, etc.).',
      ),
      'bundle' => array(
        'type' => 'varchar',
        'length' => 128,
        'not null' => TRUE,
        'description' => 'The name of the bundle a mapping applies to.',
      ),
      'mapping' => array(
        'description' => 'The serialized mapping of the bundle type and fields to RDF terms.',
        'type' => 'blob',
        'not null' => FALSE,
        'size' => 'big',
        'serialize' => TRUE,
      ),
    ),
    'primary key' => array('type', 'bundle'),
  );

  return $schema;
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.install](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.install) · Licensed GPL-2.0-or-later (see LICENSE)._
