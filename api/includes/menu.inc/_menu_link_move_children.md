# _menu_link_move_children()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 3536–3577 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L3536-L3577)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function _menu_link_move_children($item, $existing_item)
```

## Documentation

```text
Updates the children of a menu link that is being moved.

The menu name, parents (p1 - p6), and depth are updated for all children of
the link, and the has_children status of the previous parent is updated.
```

## Code

```php
function _menu_link_move_children($item, $existing_item) {
  $query = db_update('menu_links');

  $query->fields(array('menu_name' => $item['menu_name']));

  $p = 'p1';
  $expressions = array();
  for ($i = 1; $i <= $item['depth']; $p = 'p' . ++$i) {
    $expressions[] = array($p, ":p_$i", array(":p_$i" => $item[$p]));
  }
  $j = $existing_item['depth'] + 1;
  while ($i <= MENU_MAX_DEPTH && $j <= MENU_MAX_DEPTH) {
    $expressions[] = array('p' . $i++, 'p' . $j++, array());
  }
  while ($i <= MENU_MAX_DEPTH) {
    $expressions[] = array('p' . $i++, 0, array());
  }

  $shift = $item['depth'] - $existing_item['depth'];
  if ($shift > 0) {
    // The order of expressions must be reversed so the new values don't
    // overwrite the old ones before they can be used because "Single-table
    // UPDATE assignments are generally evaluated from left to right"
    // see: http://dev.mysql.com/doc/refman/5.0/en/update.html
    $expressions = array_reverse($expressions);
  }
  foreach ($expressions as $expression) {
    $query->expression($expression[0], $expression[1], $expression[2]);
  }

  $query->expression('depth', 'depth + :depth', array(':depth' => $shift));
  $query->condition('menu_name', $existing_item['menu_name']);
  $p = 'p1';
  for ($i = 1; $i <= MENU_MAX_DEPTH && $existing_item[$p]; $p = 'p' . ++$i) {
    $query->condition($p, $existing_item[$p]);
  }

  $query->execute();

  // Check the has_children status of the parent, while excluding this item.
  _menu_update_parental_status($existing_item, TRUE);
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
