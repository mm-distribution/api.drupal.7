# UserUpdatePathTestCase::testFilledUpgrade()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/update.user.test`](../_file.md), lines 31–34 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/update.user.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/update.user.test#L31-L34)
- **Class:** [UserUpdatePathTestCase](../UserUpdatePathTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
public function testFilledUpgrade()
```

## Documentation

```text
Tests that the update is successful.
```

## Code

```php
  public function testFilledUpgrade() {
    $this->assertTrue($this->performUpgrade(), 'The update was completed successfully.');
    $this->assertTrue(db_index_exists('users', 'picture'), 'The {users}.picture column has an index.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/update.user.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/update.user.test) · Licensed GPL-2.0-or-later (see LICENSE)._
