# _menu_update_parental_status()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 3582–3601 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L3582-L3601)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function _menu_update_parental_status($item, $exclude = FALSE)
```

## Documentation

```text
Checks and updates the 'has_children' status for the parent of a link.
```

## Code

```php
function _menu_update_parental_status($item, $exclude = FALSE) {
  // If plid == 0, there is nothing to update.
  if ($item['plid']) {
    // Check if at least one visible child exists in the table.
    $query = db_select('menu_links');
    $query->addField('menu_links', 'mlid');
    $query->condition('menu_name', $item['menu_name']);
    $query->condition('hidden', 0);
    $query->condition('plid', $item['plid']);
    $query->range(0, 1);
    if ($exclude) {
      $query->condition('mlid', $item['mlid'], '<>');
    }
    $parent_has_children = ((bool) $query->execute()->fetchField()) ? 1 : 0;
    db_update('menu_links')
      ->fields(array('has_children' => $parent_has_children))
      ->condition('mlid', $item['plid'])
      ->execute();
  }
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
