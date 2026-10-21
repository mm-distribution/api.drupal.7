# book_export()

- **Type:** Function
- **File:** [`modules/book/book.pages.inc`](_file.md), lines 47–68 · [local source](../../../../source/modules/book/book.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.pages.inc#L47-L68)
- **Module/theme:** book

## Signature

```php
function book_export($type, $nid)
```

## Documentation

```text
Menu callback; Generates representations of a book page and its children.

The function delegates the generation of output to helper functions. The
function name is derived by prepending 'book_export_' to the given output
type. So, e.g., a type of 'html' results in a call to the function
book_export_html().

@param $type
  A string encoding the type of output requested. The following types are
  currently supported in book module:
  - html: Printer-friendly HTML.
  Other types may be supported in contributed modules.
@param $nid
  An integer representing the node id (nid) of the node to export

@return
  A string representing the node and its children in the book hierarchy in a
  format determined by the $type parameter.

@see book_menu()
```

## Code

```php
function book_export($type, $nid) {
  // Check that the node exists and that the current user has access to it.
  $node = node_load($nid);
  if (!$node) {
    return MENU_NOT_FOUND;
  }
  if (!node_access('view', $node)) {
    return MENU_ACCESS_DENIED;
  }

  $type = drupal_strtolower($type);

  $export_function = 'book_export_' . $type;

  if (function_exists($export_function)) {
    print call_user_func($export_function, $nid);
  }
  else {
    drupal_set_message(t('Unknown export format.'));
    drupal_not_found();
  }
}
```

---
_Drupal 7.103 · [modules/book/book.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/book/book.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
