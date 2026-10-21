# DrupalWebTestCase::drupalGetToken()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 1380–1383 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L1380-L1383)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function drupalGetToken($value = '')
```

## Documentation

```text
Generate a token for the currently logged in user.
```

## Code

```php
  protected function drupalGetToken($value = '') {
    $private_key = drupal_get_private_key();
    return drupal_hmac_base64($value, $this->session_id . $private_key);
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
