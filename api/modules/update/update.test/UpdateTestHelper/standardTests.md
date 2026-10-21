# UpdateTestHelper::standardTests()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 52–56 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L52-L56)
- **Class:** [UpdateTestHelper](../UpdateTestHelper.md)
- **Module/theme:** update

## Signature

```php
protected function standardTests()
```

## Documentation

```text
Runs a series of assertions that are applicable to all update statuses.
```

## Code

```php
  protected function standardTests() {
    $this->assertRaw('<h3>' . t('Drupal core') . '</h3>');
    $this->assertRaw(l(t('Drupal'), 'http://example.com/project/drupal'), 'Link to the Drupal project appears.');
    $this->assertNoText(t('No available releases found'));
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
