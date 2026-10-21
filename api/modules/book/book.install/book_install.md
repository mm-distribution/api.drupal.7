# book_install()

- **Type:** Function
- **File:** [`modules/book/book.install`](_file.md), lines 11–14 · [local source](../../../../source/modules/book/book.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.install#L11-L14)
- **Module/theme:** book
- **Implements:** [hook_install()](../../system/system.api.php/hook_install.md)

## Signature

```php
function book_install()
```

## Documentation

```text
Implements hook_install().
```

## Code

```php
function book_install() {
  // Add the node type.
  _book_install_type_create();
}
```

---
_Drupal 7.103 · [modules/book/book.install](https://github.com/drupal/drupal/blob/7.103/modules/book/book.install) · Licensed GPL-2.0-or-later (see LICENSE)._
