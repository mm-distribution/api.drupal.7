# SessionTestCase::assertSessionEmpty()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 525–532 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L525-L532)
- **Class:** [SessionTestCase](../SessionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function assertSessionEmpty($empty)
```

## Documentation

```text
Assert whether $_SESSION is empty at the beginning of the request.
```

## Code

```php
  function assertSessionEmpty($empty) {
    if ($empty) {
      $this->assertIdentical($this->drupalGetHeader('X-Session-Empty'), '1', 'Session was empty.');
    }
    else {
      $this->assertIdentical($this->drupalGetHeader('X-Session-Empty'), '0', 'Session was not empty.');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
