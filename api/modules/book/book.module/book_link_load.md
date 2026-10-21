# book_link_load()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 1359–1368 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L1359-L1368)
- **Module/theme:** book

## Signature

```php
function book_link_load($mlid)
```

## Documentation

```text
Gets a book menu link by its menu link ID.

Like menu_link_load(), but adds additional data from the {book} table.

Do not call when loading a node, since this function may call node_load().

@param $mlid
  The menu link ID of the menu item.

@return
  A menu link, with the link translated for rendering and data added from the
  {book} table. FALSE if there is an error.
```

## Code

```php
function book_link_load($mlid) {
  if ($item = db_query("SELECT * FROM {menu_links} ml INNER JOIN {book} b ON b.mlid = ml.mlid LEFT JOIN {menu_router} m ON m.path = ml.router_path WHERE ml.mlid = :mlid", array(
      ':mlid' => $mlid,
    ))->fetchAssoc()) {
    _menu_link_translate($item);
    return $item;
  }

  return FALSE;
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
