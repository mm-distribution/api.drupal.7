# _book_parent_select()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 473–511 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L473-L511)
- **Module/theme:** book

## Signature

```php
function _book_parent_select($book_link)
```

## Documentation

```text
Builds the parent selection form element for the node form or outline tab.

This function is also called when generating a new set of options during the
Ajax callback, so an array is returned that can be used to replace an
existing form element.

@param $book_link
  A fully loaded menu link that is part of the book hierarchy.

@return
  A parent selection form element.
```

## Code

```php
function _book_parent_select($book_link) {
  if (variable_get('menu_override_parent_selector', FALSE)) {
    return array();
  }
  // Offer a message or a drop-down to choose a different parent page.
  $form = array(
    '#type' => 'hidden',
    '#value' => -1,
    '#prefix' => '<div id="edit-book-plid-wrapper">',
    '#suffix' => '</div>',
  );

  if ($book_link['nid'] === $book_link['bid']) {
    // This is a book - at the top level.
    if ($book_link['original_bid'] === $book_link['bid']) {
      $form['#prefix'] .= '<em>' . t('This is the top-level page in this book.') . '</em>';
    }
    else {
      $form['#prefix'] .= '<em>' . t('This will be the top-level page in this book.') . '</em>';
    }
  }
  elseif (!$book_link['bid']) {
    $form['#prefix'] .= '<em>' . t('No book selected.') . '</em>';
  }
  else {
    $form = array(
      '#type' => 'select',
      '#title' => t('Parent item'),
      '#default_value' => $book_link['plid'],
      '#description' => t('The parent page in the book. The maximum depth for a book and all child pages is !maxdepth. Some pages in the selected book may not be available as parents if selecting them would exceed this limit.', array('!maxdepth' => MENU_MAX_DEPTH)),
      '#options' => book_toc($book_link['bid'], $book_link['parent_depth_limit'], array($book_link['mlid'])),
      '#attributes' => array('class' => array('book-title-select')),
      '#prefix' => '<div id="edit-book-plid-wrapper">',
      '#suffix' => '</div>',
    );
  }

  return $form;
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
