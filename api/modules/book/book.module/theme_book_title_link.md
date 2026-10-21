# theme_book_title_link()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 363–369 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L363-L369)
- **Module/theme:** book
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_book_title_link($variables)
```

## Documentation

```text
Returns HTML for a link to a book title when used as a block title.

@param $variables
  An associative array containing:
  - link: An array containing title, href and options for the link.

@ingroup themeable
```

## Code

```php
function theme_book_title_link($variables) {
  $link = $variables['link'];

  $link['options']['attributes']['class'] = array('book-title');

  return l($link['title'], $link['href'], $link['options']);
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
