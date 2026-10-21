# CommentUpgradePathTestCase::testCommentUpgrade()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.comment.test`](../_file.md), lines 29–34 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.comment.test#L29-L34)
- **Class:** [CommentUpgradePathTestCase](../CommentUpgradePathTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testCommentUpgrade()
```

## Documentation

```text
Test a successful upgrade.
```

## Code

```php
  public function testCommentUpgrade() {
    if ($this->skipUpgradeTest) {
      return;
    }
    $this->assertTrue($this->performUpgrade(), 'The upgrade was completed successfully.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.comment.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
