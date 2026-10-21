# DatabaseSchema_sqlite::getFieldTypeMap()

- **Type:** Method
- **File:** [`includes/database/sqlite/schema.inc`](../_file.md), lines 192–231 · [local source](../../../../../../source/includes/database/sqlite/schema.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc#L192-L231)
- **Class:** [DatabaseSchema_sqlite](../DatabaseSchema_sqlite.md)

## Signature

```php
public function getFieldTypeMap()
```

## Documentation

```text
This maps a generic data type in combination with its data size
to the engine-specific data type.
```

## Code

```php
  public function getFieldTypeMap() {
    // Put :normal last so it gets preserved by array_flip. This makes
    // it much easier for modules (such as schema.module) to map
    // database types back into schema types.
    // $map does not use drupal_static as its value never changes.
    static $map = array(
      'varchar:normal'  => 'VARCHAR',
      'char:normal'     => 'CHAR',

      'text:tiny'       => 'TEXT',
      'text:small'      => 'TEXT',
      'text:medium'     => 'TEXT',
      'text:big'        => 'TEXT',
      'text:normal'     => 'TEXT',

      'serial:tiny'     => 'INTEGER',
      'serial:small'    => 'INTEGER',
      'serial:medium'   => 'INTEGER',
      'serial:big'      => 'INTEGER',
      'serial:normal'   => 'INTEGER',

      'int:tiny'        => 'INTEGER',
      'int:small'       => 'INTEGER',
      'int:medium'      => 'INTEGER',
      'int:big'         => 'INTEGER',
      'int:normal'      => 'INTEGER',

      'float:tiny'      => 'FLOAT',
      'float:small'     => 'FLOAT',
      'float:medium'    => 'FLOAT',
      'float:big'       => 'FLOAT',
      'float:normal'    => 'FLOAT',

      'numeric:normal'  => 'NUMERIC',

      'blob:big'        => 'BLOB',
      'blob:normal'     => 'BLOB',
    );
    return $map;
  }
```

---
_Drupal 7.103 · [includes/database/sqlite/schema.inc](https://github.com/drupal/drupal/blob/7.103/includes/database/sqlite/schema.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
