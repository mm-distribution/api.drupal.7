# template_preprocess_book_export_html()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 1218–1227 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L1218-L1227)
- **Module/theme:** book

## Signature

```php
function template_preprocess_book_export_html(&$variables)
```

## Documentation

```text
Processes variables for book-export-html.tpl.php.

@param $variables
  An associative array containing the following keys:
  - title
  - contents
  - depth

@see book-export-html.tpl.php
```

## Code

```php
function template_preprocess_book_export_html(&$variables) {
  global $base_url, $language;

  $variables['title'] = check_plain($variables['title']);
  $variables['base_url'] = $base_url;
  $variables['language'] = $language;
  $variables['language_rtl'] = ($language->direction == LANGUAGE_RTL);
  $variables['head'] = drupal_get_html_head();
  $variables['dir'] = $language->direction ? 'rtl' : 'ltr';
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
