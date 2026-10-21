# book_type_is_allowed()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 1316–1318 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L1316-L1318)
- **Module/theme:** book

## Signature

```php
function book_type_is_allowed($type)
```

## Documentation

```text
Determine if a given node type is in the list of types allowed for books.

@param $type
  A node type.

@return
  A Boolean TRUE if the node type can be included in books; otherwise, FALSE.
```

## Code

```php
function book_type_is_allowed($type) {
  return in_array($type, variable_get('book_allowed_types', array('book')));
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
