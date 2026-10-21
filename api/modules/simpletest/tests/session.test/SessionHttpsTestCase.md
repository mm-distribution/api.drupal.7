# SessionHttpsTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/session.test`](_file.md), lines 552–840 · [local source](../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L552-L840)
- **Module/theme:** batch_test

## Signature

```php
class SessionHttpsTestCase extends DrupalWebTestCase
```

## Documentation

```text
Ensure that when running under HTTPS two session cookies are generated.
```

## Methods (derived index)

- [getInfo()](SessionHttpsTestCase/getInfo.md)
- [setUp()](SessionHttpsTestCase/setUp.md)
- [testHttpsSession()](SessionHttpsTestCase/testHttpsSession.md)
- [testEmptySessionId()](SessionHttpsTestCase/testEmptySessionId.md) — Tests that empty session IDs do not cause unrelated sessions to load.
- [assertSessionIds()](SessionHttpsTestCase/assertSessionIds.md) — Test that there exists a session with two specific session IDs.
- [httpsUrl()](SessionHttpsTestCase/httpsUrl.md) — Builds a URL for submitting a mock HTTPS request to HTTP test environments.
- [httpUrl()](SessionHttpsTestCase/httpUrl.md) — Builds a URL for submitting a mock HTTP request to HTTPS test environments.

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
