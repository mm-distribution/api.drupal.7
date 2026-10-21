# book_admin_edit_submit()

- **Type:** Function
- **File:** [`modules/book/book.admin.inc`](_file.md), lines 117–151 · [local source](../../../../source/modules/book/book.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.admin.inc#L117-L151)
- **Module/theme:** book

## Signature

```php
function book_admin_edit_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for book_admin_edit().

This function takes care to save parent menu items before their children.
Saving menu items in the incorrect order can break the menu tree.

@see book_admin_edit_validate()
@see menu_overview_form_submit()
```

## Code

```php
function book_admin_edit_submit($form, &$form_state) {
  // Save elements in the same order as defined in post rather than the form.
  // This ensures parents are updated before their children, preventing orphans.
  $order = array_flip(array_keys($form_state['input']['table']));
  $form['table'] = array_merge($order, $form['table']);

  foreach (element_children($form['table']) as $key) {
    if ($form['table'][$key]['#item']) {
      $row = $form['table'][$key];
      $values = $form_state['values']['table'][$key];

      // Update menu item if moved.
      if ($row['plid']['#default_value'] != $values['plid'] || $row['weight']['#default_value'] != $values['weight']) {
        $row['#item']['plid'] = $values['plid'];
        $row['#item']['weight'] = $values['weight'];
        menu_link_save($row['#item']);
      }

      // Update the title if changed.
      if ($row['title']['#default_value'] != $values['title']) {
        $node = node_load($values['nid']);
        $langcode = LANGUAGE_NONE;
        $node->title = $values['title'];
        $node->book['link_title'] = $values['title'];
        $node->revision = 1;
        $node->log = t('Title changed from %original to %current.', array('%original' => $node->title, '%current' => $values['title']));

        node_save($node);
        watchdog('content', 'book: updated %title.', array('%title' => $node->title), WATCHDOG_NOTICE, l(t('view'), 'node/' . $node->nid));
      }
    }
  }

  drupal_set_message(t('Updated book %title.', array('%title' => $form['#node']->title)));
}
```

---
_Drupal 7.103 · [modules/book/book.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/book/book.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
