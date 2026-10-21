# UpdatePathTestCase::prepareD7Session()

- **Type:** Method
- **File:** [`modules/simpletest/tests/upgrade/upgrade.test`](../_file.md), lines 322–332 · [local source](../../../../../../../source/modules/simpletest/tests/upgrade/upgrade.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test#L322-L332)
- **Class:** [UpdatePathTestCase](../UpdatePathTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
protected function prepareD7Session()
```

## Documentation

```text
Overrides UpgradePathTestCase::prepareD7Session().
```

## Code

```php
  protected function prepareD7Session() {
    // Generate and set a D7-compatible session cookie.
    $this->curlInitialize();
    $sid = drupal_hash_base64(uniqid(mt_rand(), TRUE) . drupal_random_bytes(55));
    curl_setopt($this->curlHandle, CURLOPT_COOKIE, rawurlencode(session_name()) . '=' . rawurlencode($sid));

    // Force our way into the session of the child site.
    drupal_save_session(TRUE);
    _drupal_session_write($sid, '');
    drupal_save_session(FALSE);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/upgrade/upgrade.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/upgrade/upgrade.test) · Licensed GPL-2.0-or-later (see LICENSE)._
