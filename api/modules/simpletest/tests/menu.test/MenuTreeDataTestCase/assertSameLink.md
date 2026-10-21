# MenuTreeDataTestCase::assertSameLink()

- **Type:** Method
- **File:** [`modules/simpletest/tests/menu.test`](../_file.md), lines 978–980 · [local source](../../../../../../source/modules/simpletest/tests/menu.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test#L978-L980)
- **Class:** [MenuTreeDataTestCase](../MenuTreeDataTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function assertSameLink($link1, $link2, $message = '')
```

## Documentation

```text
Check that two menu links are the same by comparing the mlid.

@param $link1
  A menu link item.
@param $link2
  A menu link item.
@param $message
  The message to display along with the assertion.
@return
  TRUE if the assertion succeeded, FALSE otherwise.
```

## Code

```php
  protected function assertSameLink($link1, $link2, $message = '') {
    return $this->assert($link1['mlid'] == $link2['mlid'], $message ? $message : 'First link is identical to second link');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/menu.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/menu.test) · Licensed GPL-2.0-or-later (see LICENSE)._
