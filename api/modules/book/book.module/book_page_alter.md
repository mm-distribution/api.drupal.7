# book_page_alter()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 908–914 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L908-L914)
- **Module/theme:** book
- **Implements:** [hook_page_alter()](../../system/system.api.php/hook_page_alter.md)

## Signature

```php
function book_page_alter(&$page)
```

## Documentation

```text
Implements hook_page_alter().

Adds the book menu to the list of menus used to build the active trail when
viewing a book page.
```

## Code

```php
function book_page_alter(&$page) {
  if (($node = menu_get_object()) && !empty($node->book['bid'])) {
    $active_menus = menu_get_active_menu_names();
    $active_menus[] = $node->book['menu_name'];
    menu_set_active_menu_names($active_menus);
  }
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
