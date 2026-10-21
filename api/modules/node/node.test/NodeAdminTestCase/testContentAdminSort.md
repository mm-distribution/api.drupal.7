# NodeAdminTestCase::testContentAdminSort()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 1825–1859 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1825-L1859)
- **Class:** [NodeAdminTestCase](../NodeAdminTestCase.md)
- **Module/theme:** node

## Signature

```php
function testContentAdminSort()
```

## Documentation

```text
Tests that the table sorting works on the content admin pages.
```

## Code

```php
  function testContentAdminSort() {
    $this->drupalLogin($this->admin_user);
    foreach (array('dd', 'aa', 'DD', 'bb', 'cc', 'CC', 'AA', 'BB') as $prefix) {
      $this->drupalCreateNode(array('title' => $prefix . $this->randomName(6)));
    }

    // Test that the default sort by node.changed DESC actually fires properly.
    $nodes_query = db_select('node', 'n')
      ->fields('n', array('nid'))
      ->orderBy('changed', 'DESC')
      ->execute()
      ->fetchCol();

    $nodes_form = array();
    $this->drupalGet('admin/content');
    foreach ($this->xpath('//table/tbody/tr/td/div/input/@value') as $input) {
      $nodes_form[] = $input;
    }
    $this->assertEqual($nodes_query, $nodes_form, 'Nodes are sorted in the form according to the default query.');

    // Compare the rendered HTML node list to a query for the nodes ordered by
    // title to account for possible database-dependent sort order.
    $nodes_query = db_select('node', 'n')
      ->fields('n', array('nid'))
      ->orderBy('title')
      ->execute()
      ->fetchCol();

    $nodes_form = array();
    $this->drupalGet('admin/content', array('query' => array('sort' => 'asc', 'order' => 'Title')));
    foreach ($this->xpath('//table/tbody/tr/td/div/input/@value') as $input) {
      $nodes_form[] = $input;
    }
    $this->assertEqual($nodes_query, $nodes_form, 'Nodes are sorted in the form the same as they are in the query.');
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
