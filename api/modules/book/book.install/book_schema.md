# book_schema()

- **Type:** Function
- **File:** [`modules/book/book.install`](_file.md), lines 59–95 · [local source](../../../../source/modules/book/book.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.install#L59-L95)
- **Module/theme:** book
- **Implements:** [hook_schema()](../../system/system.api.php/hook_schema.md)

## Signature

```php
function book_schema()
```

## Documentation

```text
Implements hook_schema().
```

## Code

```php
function book_schema() {
  $schema['book'] = array(
  'description' => 'Stores book outline information. Uniquely connects each node in the outline to a link in {menu_links}',
    'fields' => array(
      'mlid' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
        'description' => "The book page's {menu_links}.mlid.",
      ),
      'nid' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
        'description' => "The book page's {node}.nid.",
      ),
      'bid' => array(
        'type' => 'int',
        'unsigned' => TRUE,
        'not null' => TRUE,
        'default' => 0,
        'description' => "The book ID is the {book}.nid of the top-level page.",
      ),
    ),
    'primary key' => array('mlid'),
    'unique keys' => array(
      'nid' => array('nid'),
    ),
    'indexes' => array(
      'bid' => array('bid'),
    ),
  );

  return $schema;
}
```

---
_Drupal 7.103 · [modules/book/book.install](https://github.com/drupal/drupal/blob/7.103/modules/book/book.install) · Licensed GPL-2.0-or-later (see LICENSE)._
