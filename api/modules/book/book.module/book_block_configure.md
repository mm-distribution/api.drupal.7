# book_block_configure()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 329–344 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L329-L344)
- **Module/theme:** book
- **Implements:** [hook_block_configure()](../../block/block.api.php/hook_block_configure.md)

## Signature

```php
function book_block_configure($delta = '')
```

## Documentation

```text
Implements hook_block_configure().
```

## Code

```php
function book_block_configure($delta = '') {
  $block = array();
  $options = array(
    'all pages' => t('Show block on all pages'),
    'book pages' => t('Show block only on book pages'),
  );
  $form['book_block_mode'] = array(
    '#type' => 'radios',
    '#title' => t('Book navigation block display'),
    '#options' => $options,
    '#default_value' => variable_get('book_block_mode', 'all pages'),
    '#description' => t("If <em>Show block on all pages</em> is selected, the block will contain the automatically generated menus for all of the site's books. If <em>Show block only on book pages</em> is selected, the block will contain only the one menu corresponding to the current page's book. In this case, if the current page is not in a book, no block will be displayed. The <em>Page specific visibility settings</em> or other visibility settings can be used in addition to selectively display this block."),
    );

  return $form;
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
