# book_node_load()

- **Type:** Function
- **File:** [`modules/book/book.module`](_file.md), lines 874–882 · [local source](../../../../source/modules/book/book.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module#L874-L882)
- **Module/theme:** book
- **Implements:** [hook_node_load()](../../node/node.api.php/hook_node_load.md)

## Signature

```php
function book_node_load($nodes, $types)
```

## Documentation

```text
Implements hook_node_load().
```

## Code

```php
function book_node_load($nodes, $types) {
  $result = db_query("SELECT * FROM {book} b INNER JOIN {menu_links} ml ON b.mlid = ml.mlid WHERE b.nid IN (:nids)", array(':nids' =>  array_keys($nodes)), array('fetch' => PDO::FETCH_ASSOC));
  foreach ($result as $record) {
    $nodes[$record['nid']]->book = $record;
    $nodes[$record['nid']]->book['href'] = $record['link_path'];
    $nodes[$record['nid']]->book['title'] = $record['link_title'];
    $nodes[$record['nid']]->book['options'] = unserialize($record['options']);
  }
}
```

---
_Drupal 7.103 · [modules/book/book.module](https://github.com/drupal/drupal/blob/7.103/modules/book/book.module) · Licensed GPL-2.0-or-later (see LICENSE)._
