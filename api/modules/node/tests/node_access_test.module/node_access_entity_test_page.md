# node_access_entity_test_page()

- **Type:** Function
- **File:** [`modules/node/tests/node_access_test.module`](_file.md), lines 148–171 · [local source](../../../../../source/modules/node/tests/node_access_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/tests/node_access_test.module#L148-L171)
- **Module/theme:** node_test

## Signature

```php
function node_access_entity_test_page()
```

## Documentation

```text
Page callback for node access entity test page.

Page should say "No nodes" if there are no nodes, and "Yes, # nodes" (with
the number filled in) if there were nodes the user could access. Also, the
database query is shown, and a list of the node IDs, for debugging purposes.
And if there is a query exception, the page says "Exception" and gives the
error.

@see node_access_test_menu()
```

## Code

```php
function node_access_entity_test_page() {
  $output = '';
  try {
    $query = new EntityFieldQuery;
    $result = $query->fieldCondition('body', 'value', 'A', 'STARTS_WITH')->execute();
    if (!empty($result['node'])) {
      $output .= '<p>Yes, ' . count($result['node']) . ' nodes</p>';
      $output .= '<ul>';
      foreach ($result['node'] as $nid => $v) {
        $output .= '<li>' . $nid . '</li>';
      }
      $output .= '</ul>';
    }
    else {
      $output .= '<p>No nodes</p>';
    }
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
