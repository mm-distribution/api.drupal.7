# node_access_test_page()

- **Type:** Function
- **File:** [`modules/node/tests/node_access_test.module`](_file.md), lines 106–135 · [local source](../../../../../source/modules/node/tests/node_access_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.module#L106-L135)
- **Module/theme:** node_test

## Signature

```php
function node_access_test_page()
```

## Documentation

```text
Page callback for node access test page.

Page should say "No nodes" if there are no nodes, and "Yes, # nodes" (with
the number filled in) if there were nodes the user could access. Also, the
database query is shown, and a list of the node IDs, for debugging purposes.
And if there is a query exception, the page says "Exception" and gives the
error.
```

## Code

```php
function node_access_test_page() {
  $output = '';

  try {
    $query = db_select('node', 'mytab')
      ->fields('mytab');
    $query->addTag('node_access');
    $result = $query->execute()->fetchAll();

    if (count($result)) {
      $output .= '<p>Yes, ' . count($result) . ' nodes</p>';
      $output .= '<ul>';
      foreach ($result as $item) {
        $output .= '<li>' . $item->nid . '</li>';
      }
      $output .= '</ul>';
    }
    else {
      $output .= '<p>No nodes</p>';
    }

    $output .= '<p>' . ((string) $query ) . '</p>';
  }
  catch (Exception $e) {
    $output = '<p>Exception</p>';
    $output .= '<p>' . $e->getMessage() . '</p>';
  }

  return $output;
}
```

---
_Drupal 7.103 · [modules/node/tests/node_access_test.module](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
