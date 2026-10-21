# _book_add_form_elements()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 519–598 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L519-L598)
- **Module/theme:** book

## Signature

```php
function _book_add_form_elements(&$form, &$form_state, $node)
```

## Documentation

```text
Builds the common elements of the book form for the node and outline forms.

@param $node
  The node whose form is being viewed.
```

## Code

```php
function _book_add_form_elements(&$form, &$form_state, $node) {
  // If the form is being processed during the Ajax callback of our book bid
  // dropdown, then $form_state will hold the value that was selected.
  if (isset($form_state['values']['book'])) {
    $node->book = $form_state['values']['book'];
  }

  $form['book'] = array(
    '#type' => 'fieldset',
    '#title' => t('Book outline'),
    '#weight' => 10,
    '#collapsible' => TRUE,
    '#collapsed' => TRUE,
    '#group' => 'additional_settings',
    '#attributes' => array(
      'class' => array('book-outline-form'),
    ),
    '#attached' => array(
      'js' => array(drupal_get_path('module', 'book') . '/book.js'),
    ),
    '#tree' => TRUE,
  );
  foreach (array('menu_name', 'mlid', 'nid', 'router_path', 'has_children', 'options', 'module', 'original_bid', 'parent_depth_limit') as $key) {
    $form['book'][$key] = array(
      '#type' => 'value',
      '#value' => $node->book[$key],
    );
  }

  $form['book']['plid'] = _book_parent_select($node->book);

  // @see _book_admin_table_tree(). The weight may be larger than 15.
  $form['book']['weight'] = array(
    '#type' => 'weight',
    '#title' => t('Weight'),
    '#default_value' => $node->book['weight'],
    '#delta' => max(15, abs($node->book['weight'])),
    '#weight' => 5,
    '#description' => t('Pages at a given level are ordered first by weight and then by title.'),
  );
  $options = array();
  $nid = isset($node->nid) ? $node->nid : 'new';

  if (isset($node->nid) && ($nid == $node->book['original_bid']) && ($node->book['parent_depth_limit'] == 0)) {
    // This is the top level node in a maximum depth book and thus cannot be moved.
    $options[$node->nid] = $node->title;
  }
  else {
    foreach (book_get_books() as $book) {
      $options[$book['nid']] = $book['title'];
    }
  }

  if (user_access('create new books') && ($nid == 'new' || ($nid != $node->book['original_bid']))) {
    // The node can become a new book, if it is not one already.
    $options = array($nid => '<' . t('create a new book') . '>') + $options;
  }
  if (!$node->book['mlid']) {
    // The node is not currently in the hierarchy.
    $options = array(0 => '<' . t('none') . '>') + $options;
  }

  // Add a drop-down to select the destination book.
  $form['book']['bid'] = array(
    '#type' => 'select',
    '#title' => t('Book'),
    '#default_value' => $node->book['bid'],
    '#options' => $options,
    '#access' => (bool) $options,
    '#description' => t('Your page will be a part of the selected book.'),
    '#weight' => -5,
    '#attributes' => array('class' => array('book-title-select')),
    '#ajax' => array(
      'callback' => 'book_form_update',
      'wrapper' => 'edit-book-plid-wrapper',
      'effect' => 'fade',
      'speed' => 'fast',
    ),
  );
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
