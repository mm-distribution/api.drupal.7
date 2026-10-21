# NodeAccessRebuildTestCase::testNodeAccessRebuild()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 1783–1788 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L1783-L1788)
- **Class:** [NodeAccessRebuildTestCase](../NodeAccessRebuildTestCase.md)
- **Module/theme:** node

## Signature

```php
function testNodeAccessRebuild()
```

## Documentation

```text
Tests rebuilding the node access permissions table.
```

## Code

```php
  function testNodeAccessRebuild() {
    $this->drupalGet('admin/reports/status');
    $this->clickLink(t('Rebuild permissions'));
    $this->drupalPost(NULL, array(), t('Rebuild permissions'));
    $this->assertText(t('Content permissions have been rebuilt.'));
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
