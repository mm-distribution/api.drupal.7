# book_permission()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 68–84 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L68-L84)
- **Module/theme:** book
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function book_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function book_permission() {
  return array(
    'administer book outlines' => array(
      'title' => t('Administer book outlines'),
    ),
    'create new books' => array(
      'title' => t('Create new books'),
    ),
    'add content to books' => array(
      'title' => t('Add content and child pages to books'),
    ),
    'access printer-friendly version' => array(
      'title' => t('View printer-friendly books'),
      'description' => t('View a book page and all of its sub-pages as a single document for ease of printing. Can be performance heavy.'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
