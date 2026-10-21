# _menu_router_save()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 3851–3926 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L3851-L3926)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function _menu_router_save($menu, $masks)
```

## Documentation

```text
Saves data from menu_router_build() to the router table.
```

## Code

```php
function _menu_router_save($menu, $masks) {
  // Delete the existing router since we have some data to replace it.
  db_truncate('menu_router')->execute();

  // Prepare insert object.
  $insert = db_insert('menu_router')
    ->fields(array(
      'path',
      'load_functions',
      'to_arg_functions',
      'access_callback',
      'access_arguments',
      'page_callback',
      'page_arguments',
      'delivery_callback',
      'fit',
      'number_parts',
      'context',
      'tab_parent',
      'tab_root',
      'title',
      'title_callback',
      'title_arguments',
      'theme_callback',
      'theme_arguments',
      'type',
      'description',
      'position',
      'weight',
      'include_file',
    ));

  $num_records = 0;

  foreach ($menu as $path => $item) {
    // Fill in insert object values.
    $insert->values(array(
      'path' => $item['path'],
      'load_functions' => $item['load_functions'],
      'to_arg_functions' => $item['to_arg_functions'],
      'access_callback' => $item['access callback'],
      'access_arguments' => serialize($item['access arguments']),
      'page_callback' => $item['page callback'],
      'page_arguments' => serialize($item['page arguments']),
      'delivery_callback' => $item['delivery callback'],
      'fit' => $item['_fit'],
      'number_parts' => $item['_number_parts'],
      'context' => $item['context'],
      'tab_parent' => $item['tab_parent'],
      'tab_root' => $item['tab_root'],
      'title' => $item['title'],
      'title_callback' => $item['title callback'],
      'title_arguments' => ($item['title arguments'] ? serialize($item['title arguments']) : ''),
      'theme_callback' => $item['theme callback'],
      'theme_arguments' => serialize($item['theme arguments']),
      'type' => $item['type'],
      'description' => $item['description'],
      'position' => $item['position'],
      'weight' => (int) $item['weight'],
      'include_file' => $item['include file'],
    ));

    // Execute in batches to avoid the memory overhead of all of those records
    // in the query object.
    if (++$num_records == 20) {
      $insert->execute();
      $num_records = 0;
    }
  }
  // Insert any remaining records.
  $insert->execute();
  // Store the masks.
  variable_set('menu_masks', $masks);

  return $menu;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
