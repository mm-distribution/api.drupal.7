# SessionTestCase::assertSessionCookie()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 513–520 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L513-L520)
- **Class:** [SessionTestCase](../SessionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function assertSessionCookie($sent)
```

## Documentation

```text
Assert whether the SimpleTest browser sent a session cookie.
```

## Code

```php
  function assertSessionCookie($sent) {
    if ($sent) {
      $this->assertNotNull($this->session_id, 'Session cookie was sent.');
    }
    else {
      $this->assertNull($this->session_id, 'Session cookie was not sent.');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
