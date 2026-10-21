# SessionTestCase::sessionReset()

- **Type:** Method
- **File:** [`modules/simpletest/tests/session.test`](../_file.md), lines 497–508 · [local source](../../../../../../source/modules/simpletest/tests/session.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test#L497-L508)
- **Class:** [SessionTestCase](../SessionTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function sessionReset($uid = 0)
```

## Documentation

```text
Reset the cookie file so that it refers to the specified user.

@param $uid User id to set as the active session.
```

## Code

```php
  function sessionReset($uid = 0) {
    // Close the internal browser.
    $this->curlClose();
    $this->loggedInUser = FALSE;

    // Change cookie file for user.
    $this->cookieFile = file_stream_wrapper_get_instance_by_scheme('temporary')->getDirectoryPath() . '/cookie.' . $uid . '.txt';
    $this->additionalCurlOptions[CURLOPT_COOKIEFILE] = $this->cookieFile;
    $this->additionalCurlOptions[CURLOPT_COOKIESESSION] = TRUE;
    $this->drupalGet('session-test/get');
    $this->assertResponse(200, 'Session test module is correctly enabled.', 'Session');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/session.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/session.test) · Licensed GPL-2.0-or-later (see LICENSE)._
