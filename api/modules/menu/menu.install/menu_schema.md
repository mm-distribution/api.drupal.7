# menu_schema()

- **Type:** Function
- **File:** [`modules/menu/menu.install`](_file.md), lines 11–41 · [local source](../../../../source/modules/menu/menu.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.install#L11-L41)
- **Module/theme:** menu
- **Implements:** [hook_schema()](../../system/system.api.php/hook_schema.md)

## Signature

```php
function menu_schema()
```

## Documentation

```text
Implements hook_schema().
```

## Code

```php
function menu_schema() {
  $schema['menu_custom'] = array(
    'description' => 'Holds definitions for top-level custom menus (for example, Main menu).',
    'fields' => array(
      'menu_name' => array(
        'type' => 'varchar',
        'length' => 32,
        'not null' => TRUE,
        'default' => '',
        'description' => 'Primary Key: Unique key for menu. This is used as a block delta so length is 32.',
      ),
      'title' => array(
        'type' => 'varchar',
        'length' => 255,
        'not null' => TRUE,
        'default' => '',
        'description' => 'Menu title; displayed at top of block.',
        'translatable' => TRUE,
      ),
      'description' => array(
        'type' => 'text',
        'not null' => FALSE,
        'description' => 'Menu description.',
        'translatable' => TRUE,
      ),
    ),
    'primary key' => array('menu_name'),
  );

  return $schema;
}
```

---
_Drupal 7.103 · [modules/menu/menu.install](https://github.com/drupal/drupal/blob/7.103/modules/menu/menu.install) · Licensed GPL-2.0-or-later (see LICENSE)._
