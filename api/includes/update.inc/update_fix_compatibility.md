# update_fix_compatibility()

- **Type:** Function
- **File:** [`includes/update.inc`](_file.md), lines 24–38 · [local source](../../../source/includes/update.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/update.inc#L24-L38)

## Signature

```php
function update_fix_compatibility()
```

## Documentation

```text
Disable any items in the {system} table that are not core compatible.
```

## Code

```php
function update_fix_compatibility() {
  $incompatible = array();
  $result = db_query("SELECT name, type, status FROM {system} WHERE status = 1 AND type IN ('module','theme')");
  foreach ($result as $row) {
    if (update_check_incompatibility($row->name, $row->type)) {
      $incompatible[] = $row->name;
    }
  }
  if (!empty($incompatible)) {
    db_update('system')
      ->fields(array('status' => 0))
      ->condition('name', $incompatible, 'IN')
      ->execute();
  }
}
```

---
_Drupal 7.103 · [includes/update.inc](https://github.com/drupal/drupal/blob/7.103/includes/update.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
