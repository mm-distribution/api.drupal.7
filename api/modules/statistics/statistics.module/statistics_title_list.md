# statistics_title_list()

- **Type:** Function
- **File:** [`modules/statistics/statistics.module`](_file.md), lines 280–297 · [local source](../../../../source/modules/statistics/statistics.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module#L280-L297)
- **Module/theme:** statistics

## Signature

```php
function statistics_title_list($dbfield, $dbrows)
```

## Documentation

```text
Returns the most viewed content of all time, today, or the last-viewed node.

@param $dbfield
  The database field to use, one of:
  - 'totalcount': Integer that shows the top viewed content of all time.
  - 'daycount': Integer that shows the top viewed content for today.
  - 'timestamp': Integer that shows only the last viewed node.
@param $dbrows
  The number of rows to be returned.

@return SelectQuery|FALSE
  A query result containing the node ID, title, user ID that owns the node,
  and the username for the selected node(s), or FALSE if the query could not
  be executed correctly.
```

## Code

```php
function statistics_title_list($dbfield, $dbrows) {
  if (in_array($dbfield, array('totalcount', 'daycount', 'timestamp'))) {
    $query = db_select('node', 'n');
    $query->addTag('node_access');
    $query->join('node_counter', 's', 'n.nid = s.nid');
    $query->join('users', 'u', 'n.uid = u.uid');

    return $query
      ->fields('n', array('nid', 'title'))
      ->fields('u', array('uid', 'name'))
      ->condition($dbfield, 0, '<>')
      ->condition('n.status', 1)
      ->orderBy($dbfield, 'DESC')
      ->range(0, $dbrows)
      ->execute();
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [modules/statistics/statistics.module](https://github.com/drupal/drupal/blob/7.103/modules/statistics/statistics.module) · Licensed GPL-2.0-or-later (see LICENSE)._
