# aggregator_save_category()

- **Type:** Function
- **File:** [`modules/aggregator/aggregator.module`](_file.md), lines 440–491 · [local source](../../../../source/modules/aggregator/aggregator.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module#L440-L491)
- **Module/theme:** aggregator

## Signature

```php
function aggregator_save_category($edit)
```

## Documentation

```text
Adds/edits/deletes aggregator categories.

@param $edit
  An associative array describing the category to be added/edited/deleted.
```

## Code

```php
function aggregator_save_category($edit) {
  $link_path = 'aggregator/categories/';
  if (!empty($edit['cid'])) {
    $link_path .= $edit['cid'];
    if (!empty($edit['title'])) {
      db_merge('aggregator_category')
        ->key(array('cid' => $edit['cid']))
        ->fields(array(
          'title' => $edit['title'],
          'description' => $edit['description'],
        ))
        ->execute();
      $op = 'update';
    }
    else {
      db_delete('aggregator_category')
        ->condition('cid', $edit['cid'])
        ->execute();
      // Remove category from feeds.
      db_delete('aggregator_category_feed')
        ->condition('cid', $edit['cid'])
        ->execute();
      // Remove category from feed items.
      db_delete('aggregator_category_item')
        ->condition('cid', $edit['cid'])
        ->execute();
      // Make sure there is no active block for this category.
      if (module_exists('block')) {
        db_delete('block')
          ->condition('module', 'aggregator')
          ->condition('delta', 'category-' . $edit['cid'])
          ->execute();
      }
      $edit['title'] = '';
      $op = 'delete';
    }
  }
  elseif (!empty($edit['title'])) {
    // A single unique id for bundles and feeds, to use in blocks.
    $link_path .= db_insert('aggregator_category')
      ->fields(array(
        'title' => $edit['title'],
        'description' => $edit['description'],
        'block' => 5,
      ))
      ->execute();
    $op = 'insert';
  }
  if (isset($op)) {
    menu_link_maintain('aggregator', $op, $link_path, $edit['title']);
  }
}
```

---
_Drupal 7.103 · [modules/aggregator/aggregator.module](https://github.com/drupal/drupal/blob/7.103/modules/aggregator/aggregator.module) · Licensed GPL-2.0-or-later (see LICENSE)._
