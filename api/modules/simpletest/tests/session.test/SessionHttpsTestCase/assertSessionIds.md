# SessionHttpsTestCase::assertSessionIds()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 805–811 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L805-L811)
- **Class:** [SessionHttpsTestCase](../SessionHttpsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function assertSessionIds($sid, $ssid, $assertion_text)
```

## Documentation

```text
Test that there exists a session with two specific session IDs.

@param $sid
  The insecure session ID to search for.
@param $ssid
  The secure session ID to search for.
@param $assertion_text
  The text to display when we perform the assertion.

@return
  The result of assertTrue() that there's a session in the system that
  has the given insecure and secure session IDs.
```

## Code

```php
  protected function assertSessionIds($sid, $ssid, $assertion_text) {
    $args = array(
      ':sid' => drupal_session_id($sid),
      ':ssid' => !empty($ssid) ? drupal_session_id($ssid) : '',
    );
    return $this->assertTrue(db_query('SELECT timestamp FROM {sessions} WHERE sid = :sid AND ssid = :ssid', $args)->fetchField(), $assertion_text);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
