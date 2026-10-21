# _book_admin_table_tree()

- **Type:** Function
- **File:** [`modules/book/book.admin.inc`](_file.md), lines 201–240 · [local source](../../../../source/modules/book/book.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.admin.inc#L201-L240)
- **Module/theme:** book

## Signature

```php
function _book_admin_table_tree($tree, &$form)
```

## Documentation

```text
Helps build the main table in the book administration page form.

@param $tree
  A subtree of the book menu hierarchy.
@param $form
  The form that is being modified, passed by reference.

@return
  The modified form array.

@see book_admin_edit()
```

## Code

```php
function _book_admin_table_tree($tree, &$form) {
  // The delta must be big enough to give each node a distinct value.
  $count = count($tree);
  $delta = ($count < 30) ? 15 : intval($count / 2) + 1;

  foreach ($tree as $data) {
    $form['book-admin-' . $data['link']['nid']] = array(
      '#item' => $data['link'],
      'nid' => array('#type' => 'value', '#value' => $data['link']['nid']),
      'depth' => array('#type' => 'value', '#value' => $data['link']['depth']),
      'href' => array('#type' => 'value', '#value' => $data['link']['href']),
      'title' => array(
        '#type' => 'textfield',
        '#default_value' => $data['link']['link_title'],
        '#maxlength' => 255,
        '#size' => 40,
      ),
      'weight' => array(
        '#type' => 'weight',
        '#default_value' => $data['link']['weight'],
        '#delta' => max($delta, abs($data['link']['weight'])),
        '#title' => t('Weight for @title', array('@title' => $data['link']['title'])),
        '#title_display' => 'invisible',
      ),
      'plid' => array(
        '#type' => 'hidden',
        '#default_value' => $data['link']['plid'],
      ),
      'mlid' => array(
        '#type' => 'hidden',
        '#default_value' => $data['link']['mlid'],
      ),
    );
    if ($data['below']) {
      _book_admin_table_tree($data['below'], $form);
    }
  }

  return $form;
}
```

---
_Drupal 7.103 · [modules/book/book.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/book/book.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
