# DisabledNodeTypeTestCase::testDisabledNodeTypeUpgrade()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.node.test`](../_file.md), lines 82–88 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.node.test#L82-L88)
- **Class:** [DisabledNodeTypeTestCase](../DisabledNodeTypeTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testDisabledNodeTypeUpgrade()
```

## Documentation

```text
Tests a successful upgrade.
```

## Code

```php
  public function testDisabledNodeTypeUpgrade() {
    if ($this->skipUpgradeTest) {
      return;
    }
    $this->assertTrue($this->performUpgrade(), 'The upgrade was completed successfully.');
    $this->assertTrue(field_info_instance('comment', 'comment_body', 'comment_node_broken'), 'Comment body field instance was created for comments attached to the disabled broken node type');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.node.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
