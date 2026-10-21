# hook_schema_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 3294–3302 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L3294-L3302)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md), [schemaapi](../../../topics/schemaapi.md)

## Signature

```php
function hook_schema_alter(&$schema)
```

## Documentation

```text
Perform alterations to existing database schemas.

When a module modifies the database structure of another module (by
changing, adding or removing fields, keys or indexes), it should
implement hook_schema_alter() to update the default $schema to take its
changes into account.

See hook_schema() for details on the schema definition structure.

@param $schema
  Nested array describing the schemas for all modules.

@ingroup schemaapi
```

## Code

```php
function hook_schema_alter(&$schema) {
  // Add field to existing schema.
  $schema['users']['fields']['timezone_id'] = array(
    'type' => 'int',
    'not null' => TRUE,
    'default' => 0,
    'description' => 'Per-user timezone configuration.',
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_schema_alter()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
