# NodeQueryAlter::testNodeQueryAlterWithUI()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 2298–2318 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L2298-L2318)
- **Class:** [NodeQueryAlter](../NodeQueryAlter.md)
- **Module/theme:** node

## Signature

```php
function testNodeQueryAlterWithUI()
```

## Documentation

```text
Tests that node access permissions are followed.
```

## Code

```php
  function testNodeQueryAlterWithUI() {
    // Verify that a user with access permission can see at least one node.
    $this->drupalLogin($this->accessUser);
    $this->drupalGet('node_access_test_page');
    $this->assertText('Yes, 4 nodes', "4 nodes were found for access user");
    $this->assertNoText('Exception', "No database exception");

    // Test the content overview page.
    $this->drupalGet('admin/content');
    $table_rows = $this->xpath('//tbody/tr');
    $this->assertEqual(4, count($table_rows), "4 nodes were found for access user");

    // Verify that a user with no access permission cannot see nodes.
    $this->drupalLogin($this->noAccessUser);
    $this->drupalGet('node_access_test_page');
    $this->assertText('No nodes', "No nodes were found for no access user");
    $this->assertNoText('Exception', "No database exception");

    $this->drupalGet('admin/content');
    $this->assertText(t('No content available.'));
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
