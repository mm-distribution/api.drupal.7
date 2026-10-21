# _forum_get_topic_order()

- **Type:** Function
- **File:** [`modules/forum/forum.module`](_file.md), lines 1317–1332 · [local source](../../../../source/modules/forum/forum.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module#L1317-L1332)
- **Module/theme:** forum

## Signature

```php
function _forum_get_topic_order($sortby)
```

## Documentation

```text
Gets topic sorting information based on an integer code.

@param $sortby
  One of the following integers indicating the sort criteria:
  - 1: Date - newest first.
  - 2: Date - oldest first.
  - 3: Posts with the most comments first.
  - 4: Posts with the least comments first.

@return
  An array with the following values:
  - field: A field for an SQL query.
  - sort: 'asc' or 'desc'.
```

## Code

```php
function _forum_get_topic_order($sortby) {
  switch ($sortby) {
    case 1:
      return array('field' => 'f.last_comment_timestamp', 'sort' => 'desc');
      break;
    case 2:
      return array('field' => 'f.last_comment_timestamp', 'sort' => 'asc');
      break;
    case 3:
      return array('field' => 'f.comment_count', 'sort' => 'desc');
      break;
    case 4:
      return array('field' => 'f.comment_count', 'sort' => 'asc');
      break;
  }
}
```

---
_Drupal 7.103 · [modules/forum/forum.module](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.module) · Licensed GPL-2.0-or-later (see LICENSE)._
