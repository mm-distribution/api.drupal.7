# node_build_filter_query()

- **Type:** Function
- **File:** [`modules/node/node.admin.inc`](_file.md), lines 127–142 · [local source](../../../../source/modules/node/node.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc#L127-L142)
- **Module/theme:** node

## Signature

```php
function node_build_filter_query(SelectQueryInterface $query)
```

## Documentation

```text
Applies filters for node administration filters based on session.

@param $query
  A SelectQuery to which the filters should be applied.
```

## Code

```php
function node_build_filter_query(SelectQueryInterface $query) {
  // Build query
  $filter_data = isset($_SESSION['node_overview_filter']) ? $_SESSION['node_overview_filter'] : array();
  foreach ($filter_data as $index => $filter) {
    list($key, $value) = $filter;
    switch ($key) {
      case 'status':
        // Note: no exploitable hole as $key/$value have already been checked when submitted
        list($key, $value) = explode('-', $value, 2);
      case 'type':
      case 'language':
        $query->condition('n.' . $key, $value);
        break;
    }
  }
}
```

---
_Drupal 7.103 · [modules/node/node.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
