# DrupalWebTestCase::drupalGetAJAX()

- **Type:** Method
- **File:** [`modules/simpletest/drupal_web_test_case.php`](../_file.md), lines 2290–2292 · [local source](../../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L2290-L2292)
- **Class:** [DrupalWebTestCase](../DrupalWebTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
protected function drupalGetAJAX($path, array $options = array(), array $headers = array())
```

## Documentation

```text
Retrieve a Drupal path or an absolute path and JSON decode the result.
```

## Code

```php
  protected function drupalGetAJAX($path, array $options = array(), array $headers = array()) {
    return drupal_json_decode($this->drupalGet($path, $options, $headers));
  }
```

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
