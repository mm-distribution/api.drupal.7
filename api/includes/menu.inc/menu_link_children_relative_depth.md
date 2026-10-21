# menu_link_children_relative_depth()

- **Type:** Function
- **File:** [`includes/menu.inc`](_file.md), lines 3511–3528 · [local source](../../../source/includes/menu.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc#L3511-L3528)
- **Topics:** [menu](../../topics/menu.md)

## Signature

```php
function menu_link_children_relative_depth($item)
```

## Documentation

```text
Finds the depth of an item's children relative to its depth.

For example, if the item has a depth of 2, and the maximum of any child in
the menu link tree is 5, the relative depth is 3.

@param $item
  An array representing a menu link item.

@return
  The relative depth, or zero.
```

## Code

```php
function menu_link_children_relative_depth($item) {
  $query = db_select('menu_links');
  $query->addField('menu_links', 'depth');
  $query->condition('menu_name', $item['menu_name']);
  $query->orderBy('depth', 'DESC');
  $query->range(0, 1);

  $i = 1;
  $p = 'p1';
  while ($i <= MENU_MAX_DEPTH && $item[$p]) {
    $query->condition($p, $item[$p]);
    $p = 'p' . ++$i;
  }

  $max_depth = $query->execute()->fetchField();

  return ($max_depth > $item['depth']) ? $max_depth - $item['depth'] : 0;
}
```

---
_Drupal 7.103 · [includes/menu.inc](https://github.com/drupal/drupal/blob/7.103/includes/menu.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
